/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  // array containing all key value pairs
  const arr3 = arr1.concat(arr2);
  // dict to keep track of existing ids
  const ids = {};
  arr3.forEach((obj) => {
    const id = obj.id;
    if (!ids[id]) {
      // init key if not exist
      ids[id] = { ...obj };
    } else {
      // add or override key value pairs on exisiting key
      ids[id] = { ...ids[id], ...obj };
    }
  });
  // return sorted solution
  const res = Object.values(ids);
  res.sort((a, b) => a.id - b.id);
  return res;
};
