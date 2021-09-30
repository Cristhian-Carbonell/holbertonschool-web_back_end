const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should round a and b and return the sum of it', function() {
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(false, 7), 7);
    assert.equal(calculateNumber(true, 7), 8);
  });
});
