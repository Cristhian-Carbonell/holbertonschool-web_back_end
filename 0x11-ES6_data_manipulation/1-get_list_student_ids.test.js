import getListStudentIds from "./1-get_list_student_ids.js";
import getListStudents from "./0-get_list_students.js";

test("getListStudentIds is implemented correctly", () => {
  expect(getListStudentIds(getListStudents()).length).toBe(3);
  expect(getListStudentIds(getListStudents())).toEqual([1, 2, 5]);
  expect(getListStudentIds(null)).toEqual([]);
  expect(getListStudentIds('TEST')).toEqual([]);
});