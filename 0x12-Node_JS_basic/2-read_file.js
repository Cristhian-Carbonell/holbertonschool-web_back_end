const fs = require('fs');
const readline = require('readline');

module.exports =  function countStudents(path) {
  try{
    let countTotal = 0;
    const obj = {};
    const listObj = [];
    fs.accessSync(path, fs.F_OK);
    processLineByLine(path);
    async function processLineByLine(path) {
      const fileStraeam = fs.createReadStream(path);
      const readLine = readline.createInterface({
        input: fileStraeam,
        crlfDelay: Infinity,
      });
      for await (const line of readLine) {
        const list = line.split(',');
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
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  
};
