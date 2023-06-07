/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
  const res = new Map();
  for (const i of this) {
    const key = fn(i);
    if (res.has(key)) {
      res.get(key).push(i);
    } else {
      res.set(key, [i]);
    }
  }
  return Object.fromEntries(res);
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
