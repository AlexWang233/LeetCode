/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
  res = init;
  for (const n of nums) {
    res = fn(res, n);
  }
  return res;
};
