export default function getStudentsByLocation(getListStudents, city) {
  return getListStudents.filter((word) => word.location === city);
}
