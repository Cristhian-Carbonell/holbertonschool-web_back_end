const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('should round a and b and return the sum of it ', function() {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
  