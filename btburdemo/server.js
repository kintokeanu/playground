// Import required modules
import express from 'express';
import bodyParser from 'body-parser';
import { datadog, connectLogsToConsole } from 'datadog-logs';
// import { datadogLogs } from '@datadog/browser-logs';

// Create an instance of Express
const app = express();
const port = 3000;

datadogLogs.init({
    apiKey: '';
});



// Middleware to parse JSON requests
app.use(bodyParser.json());

// GET endpoint
app.get('/', (req, res) => {
  res.send('Hello, this is a GET request!');
});

// POST endpoint
app.post('/post', (req, res) => {
  const data = req.body;
  res.json({ message: 'Received a POST request', data });
});

// PUT endpoint
app.put('/put/:id', (req, res) => {
  const { id } = req.params;
  res.send(`Received a PUT request for ID: ${id}`);
});

// DELETE endpoint
app.delete('/delete/:id', (req, res) => {
  const { id } = req.params;
  res.send(`Received a DELETE request for ID: ${id}`);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
