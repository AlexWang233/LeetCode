/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
  let ready = true;
  let data;
  function run() {
    if (ready && data) {
      fn(...data);
      data = null;
      ready = false;
      setTimeout(() => {
        ready = true;
        run(data);
      }, t);
    }
  }
  return function (...args) {
    data = args;
    run();
  };
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
