const fs = require('fs');
const readline = require('readline');

module.exports = async function countStudents(path) {
  let countTotal = 0;
  let list;
  const obj = {};
  let listKey;
  const listObj = [];
  const fileStream = fs.createReadStream(path);

  const read = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  for await (const line of read) {
    list = line.split(',');
    countTotal += 1;
    if (countTotal === 1) {
      for (const index of list) {
        obj[index] = '';
      }
      listKey = Object.keys(obj);
    } else {
      let number = 0;
      const newObj = {};
      for (const key of listKey) {
        newObj[key] = list[number];
        number += 1;
      }
      listObj.push(newObj);
    }
  }

  const CS = listObj.filter((value) => value.field === 'CS');
  let firstnameCS = CS.map((firstname) => {
    let list = '';
    list += firstname.firstname;
    return list;
  });
  firstnameCS = firstnameCS.join(', ');

  const SWE = listObj.filter((value) => value.field === 'SWE');
  let firstnameSWE = SWE.map((firstname) => {
    let list = '';
    list += firstname.firstname;
    return list;
  });
  firstnameSWE = firstnameSWE.join(', ');

  console.log(`Number of students: ${listObj.length}`);
  console.log(`Number of students in CS: ${CS.length}. List: ${firstnameCS}`);
  console.log(`Number of students in SWE: ${SWE.length}. List: ${firstnameSWE}`);
};
