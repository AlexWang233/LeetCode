/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
  if (object === null) {
    return "null";
  }
  if (typeof object === "string") {
    return '"' + object + '"';
  }
  if (typeof object === "boolean" || typeof object === "number") {
    return String(object);
  }
  if (Array.isArray(object)) {
    const items = object.map((item) => jsonStringify(item));
    return "[" + items.join(",") + "]";
  }
  if (typeof object === "object") {
    const keys = Object.keys(object);
    const pairs = keys.map(
      (key) => '"' + key + '":' + jsonStringify(object[key])
    );
    return "{" + pairs.join(",") + "}";
  }
  return object;
};
