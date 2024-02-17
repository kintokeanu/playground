#!/usr/bin/env node
const express = require('express');
const { Pool } = require('pg');
const winston = require('winston');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });
const ExcelJS = require('exceljs');

const app = express();
app.use(express.json());
api='0203d076ffa2cb298e39b881ef343d98'
app='43b89cb87ea39a638c8dd4e2d179eba801833d63'

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'bursary_app',
    password: 'virus13sting',
    port: 5432,
})

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: 'logfile.log' }),
    ],
});


app.get('/', (req, res) => {
    try {
        logger.info('Welcome to the Bursary App');
    }
    catch (error) {
        logger.error('Error retrieving welcome message ${error}');
    }
});

app.get('/applicants', async (req, res) => {
    try {
        const {rows} = await pool.query('SELECT * FROM applicants');
        res.json(rows);
        logger.info('Applicants retrieved successfully');
    } catch (error) {
        logger.error('Error retrieving applicants ${error}');
        res.status(500).json({error: 'internal server error'})
    }
});

app.get('/applicants/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const {rows} = await pool.query('SELECT * FROM applicants WHERE id = $1', [id]);
        res.json(rows);
        logger.info('Applicant retrieved successfully');
    } catch (error) {
        logger.error('Error retrieving applicant ${error}');
        res.status(500).json({error: 'internal server error'})
    }
});

app.post('/applicants', async (req, res) => {
    const { name, email, education_level } = req.body;
    try {
        const {rows} = await pool.query('INSERT INTO applicants (name, email, education_level) VALUES ($1, $2, $3) RETURNING *', [name, email, education_level]);
        res.json(rows);
        logger.info('New applicant added: ${name}');
    } catch (error) {
        logger.error('Error adding new applicant ${error}');
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.post('/upload', upload.single('file'), (req, res) => {
    if (!req.file) {
        res.status(400).json({ error: 'No file uploaded' });
    }
    logger.info('File uploaded: ${req.file.originalname}');
    res.json({ message: 'File uploaded successfully' });
});

app.get('/report', async (req, res) => {
    try {
        const { rows } = await pool.query('SELECT * FROM applicanst');
        const workbook = new ExcelJS.Workbook();
        const worksheet = workbook.addWorksheet('Applicants');

        worksheet.addRow(['ID', 'Name', 'Email', 'Education Level', 'Applied At']);
        rows.forEach(applicant => {
            worksheet.addRow(Object, values(applicant));
        });

        res.setHeader('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
        res.setHeader('Content-Disposition', 'attachment; filename=applicants.xlsx');

        await workbook.xlsx.write(res);
        logger.info('Report generated successfully');
    } catch (error) {
        logger.error('Error generating report ${error}');
        res.status(500).json({ error: 'Internal server error' });
    }
});




const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
