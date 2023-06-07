class EventEmitter {
  constructor() {
    this.events = new Map();
  }
  subscribe(event, cb) {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    const listeners = this.events.get(event);
    listeners.push(cb);
    return {
      unsubscribe: () => {
        const i = listeners.indexOf(cb);
        if (i != -1) {
          listeners.splice(i, 1);
        }
      },
    };
  }

  emit(event, args = []) {
    if (!this.events.has(event)) {
      return [];
    }
    const listeners = this.events.get(event);
    const res = [];
    for (const l of listeners) {
      res.push(l(...args));
    }
    return res;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
