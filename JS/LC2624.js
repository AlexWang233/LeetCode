/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
  if (rowsCount * colsCount != this.length) {
    return [];
  }
  let res = Array(rowsCount)
    .fill()
    .map(() => []);
  // console.log(res);
  for (let i = 0; i < this.length; i++) {
    const j = Math.floor(i / rowsCount);
    if (j % 2 == 0) {
      res[i % rowsCount].push(this[i]);
    } else {
      res[rowsCount - (i % rowsCount) - 1].push(this[i]);
    }
  }
  return res;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
