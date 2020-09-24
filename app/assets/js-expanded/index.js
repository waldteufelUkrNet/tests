let controller = new AbortController(),
    signal     = controller.signal;

console.log("controller", controller);

signal.addEventListener('abort', () => console.log('скасовано!'));

controller.abort();

console.log(signal.aborted);