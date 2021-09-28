const app = require('http');

const localhost = '127.0.0.1';
const port = 1245;

app.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Conten-Type', 'text/plain');
  res.end('Hello Holberton School!');
}).listen(port, localhost);

module.exports = { app };
