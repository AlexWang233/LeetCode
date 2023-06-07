/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function (obj) {
  if (obj === null) {
    return null;
  }
  if (Array.isArray(obj)) {
    return obj.filter(Boolean).map(compactObject);
  }
  if (typeof obj !== "object") {
    return obj;
  }
  const res = {};
  for (const key in obj) {
    const val = compactObject(obj[key]);
    if (Boolean(val)) {
      res[key] = val;
    }
  }
  return res;
};
