export default function cleanSet(set, startString) {
  const word = [];
  if (typeof set !== 'object'
  || typeof startString !== 'string'
  || startString.length === 0) {
    return '';
  }
  for (const iterator of set) {
    if (iterator.startsWith(startString)) {
      word.push(iterator.slice(startString.length, iterator.length));
    }
  }

  return word.join('-');
}
