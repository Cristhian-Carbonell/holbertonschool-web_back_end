import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(getListStudents) {
  const array = getListStudentIds(getListStudents);
  const reducer = (previousValue, currentValue) => previousValue + currentValue;

  return array.reduce(reducer);
}
