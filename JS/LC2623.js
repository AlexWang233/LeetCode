/**
 * @param {Function} fn
 */
function memoize(fn) {
  const cache = {};
  return function (...args) {
    if (args in cache) {
      return cache[args];
    }
    const res = fn.apply(this, args);
    cache[args] = res;
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
