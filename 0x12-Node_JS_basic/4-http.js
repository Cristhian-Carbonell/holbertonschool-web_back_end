const app = require('http');

const port = 1245;

app.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
}).listen(port);

module.exports = { app };
