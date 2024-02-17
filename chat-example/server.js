import express from 'express';
import http from 'http'
import { Server } from 'socket.io';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const server = http.createServer(app);
const io = new Server(server);


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/server.html');
});

io.on('connection', (socket) => {
    console.log('A user connected');
    // listen for chat messages
    socket.on('chat message', (msg) => {
        //broadcast the message to everyone
        io.emit('chat message', msg);
    });
    // listen for disconnect
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});