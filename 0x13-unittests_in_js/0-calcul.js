function calculateNumber(a, b) {
  if (typeof a === 'number' && typeof b === 'number') {
    a = Math.round(a);
    b = Math.round(b);
    return a + b;
  }
}

module.exports = calculateNumber;
