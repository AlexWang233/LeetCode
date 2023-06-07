/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function (functions, n) {
  const results = [];
  const cur = [];
  let i = 0;
  while (i < functions.length || cur.length > 0) {
    while (cur.length < n && i < functions.length) {
      const promise = functions[i]();
      const pRes = promise.then((res) => {
        results[i] = res;
        cur.splice(cur.indexOf(pRes), 1);
      });
      cur.push(pRes);
      i++;
    }
    await Promise.race(cur);
  }
  return results;
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
