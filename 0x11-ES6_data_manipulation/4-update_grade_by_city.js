export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const newFilter = getListStudents.filter((word) => word.location === city);

  return newFilter.map((obj) => {
    const filter = newGrades.filter((grade) => grade.studentId === obj.id);
    let grade;
    if (filter[0]) {
      grade = filter[0].grade;
    } else {
      grade = 'N/A';
    }

    return { ...obj, grade };
  });
}
