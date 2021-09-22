export default function getListStudentIds(getListStudents) {
  if (getListStudents && typeof getListStudents === 'object') {
    const map1 = getListStudents.map((obj) => obj.id);

    return map1;
  }

  return [];
}
