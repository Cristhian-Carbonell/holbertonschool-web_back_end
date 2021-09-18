export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a number');
    }
    if (students instanceof Array) {
      this._students = students;
    } else {
      throw new TypeError('students must be a array');
    }
  }

  get name() {
    return this.viewName();
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  viewName() {
    return this._name;
  }

  get length() {
    return this.viewLength();
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  viewLength() {
    return this._length;
  }

  get students() {
    return this.viewStudents();
  }

  set students(students) {
    if (students instanceof Array) {
      this._students = students;
    } else {
      throw new TypeError('students must be a array');
    }
  }

  viewStudents() {
    return this._students;
  }
}
