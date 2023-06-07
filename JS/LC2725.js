/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
  let time = 0;
  let timerId;
  let res = [];

  function run() {
    var val = fn.apply(null, args);
    res.push({ time: time, returned: val });
    time += t;
  }

  function cancel() {
    clearInterval(timerId);
  }
  run();
  timerId = setInterval(run, t);
  return cancel;
};

/**
 *  const result = []
 *
 *  const fn = (x) => x * 2
 *  const args = [4], t = 20, cancelT = 110
 *
 *  const log = (...argsArr) => {
 *      result.push(fn(...argsArr))
 *  }
 *
 *  const cancel = cancellable(fn, args, t);
 *
 *  setTimeout(() => {
 *     cancel()
 *     console.log(result) // [
 *                         //      {"time":0,"returned":8},
 *                         //      {"time":20,"returned":8},
 *                         //      {"time":40,"returned":8},
 *                         //      {"time":60,"returned":8},
 *                         //      {"time":80,"returned":8},
 *                         //      {"time":100,"returned":8}
 *                         //  ]
 *  }, cancelT)
 */
