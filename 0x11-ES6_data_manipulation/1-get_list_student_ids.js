export default function getListStudentIds(getListStudents) {
  if (typeof getListStudents !== 'object') {
    return [];
  }
  const map1 = getListStudents.map((obj) => obj.id);

  return map1;
}
