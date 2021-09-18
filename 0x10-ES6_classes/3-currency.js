export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this.viewcode();
  }

  set code(code) {
    this._code = code;
  }

  viewcode() {
    return this._code;
  }

  get name() {
    return this.viewname();
  }

  set name(name) {
    this._name = name;
  }

  viewname() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
