const weakMap = new WeakMap();

function queryAPI(endpoint) {
  const count = weakMap.get(endpoint) || 0;

  if (weakMap.get(endpoint) >= 5) {
    throw Error('Endpoint load is high');
  }

  return weakMap.set(endpoint, count + 1);
}

export { queryAPI, weakMap };
