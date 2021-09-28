const app = require('http');

const port = 1245;

app.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Conten-Type', 'text/plain');
  res.write('Hello Holberton School!');
  res.end();
}).listen(port);

module.exports = { app };
