const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should round a and b and return the sum of it ', function() {
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it('should round a and b and return the sum of it ', function() {
    assert.strictEqual(calculateNumber('1', 3.7), 5);
    assert.strictequal(calculateNumber(1, '3'), 4);
    assert.strictequal(calculateNumber('1.2', '3.7'), 5);
  });
});
