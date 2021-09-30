const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should round a and b and return the sum of it ', function() {
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
    assert.equal(calculateNumber('1.5', 3.7), undefined);
    assert.equal(calculateNumber(1.5, '3.7'), undefined);
    assert.equal(calculateNumber('1.5', '3.7'), undefined);
  });
  it('should round a and b and return the sum of it ', function() {
    assert.notEqual(calculateNumber('fuction', 3.7), 5);
    assert.notEqual(calculateNumber(1, 'fuction'), 4);
    assert.notEqual(calculateNumber('fuction', 'fuction'), 5);
  });
  it('should round a and b and return the sum of it ', function() {
    assert.deepStrictEqual(calculateNumber(false, false), undefined);
    assert.deepStrictEqual(calculateNumber(true, false), undefined);
    assert.deepStrictEqual(calculateNumber(true, true), undefined);
  });
});
