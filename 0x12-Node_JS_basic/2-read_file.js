const fs = require('fs');

module.exports = function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
  console.log(content)
};
