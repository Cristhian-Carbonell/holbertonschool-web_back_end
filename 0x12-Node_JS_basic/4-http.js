const app = require('http');

const port = 1245;

app.createServer((req, res) => {
  res.end('Hello Holberton School!');
}).listen(port);

module.exports = { app };
