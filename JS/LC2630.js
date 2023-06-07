/**
 * @param {Function} fn
 */
function memoize(fn) {
  const cache = new Map();
  const id = Symbol();
  return function (...args) {
    let curCache = cache;
    for (const arg of args) {
      if (!curCache.has(arg)) {
        curCache.set(arg, new Map());
      }
      curCache = curCache.get(arg);
    }
    if (curCache.has(id)) {
      return curCache.get(id);
    }
    res = fn(...args);
    curCache.set(id, res);
    return res;
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
