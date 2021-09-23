export default function cleanSet(set, startString) {
  const setIterator = set[Symbol.iterator]();
  console.log(setIterator.next().value)
}