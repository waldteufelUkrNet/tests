"use strict";

window.addEventListener('message', function (e) {
  console.log("\n    e.data: ".concat(e.data, ",\n    e.origin: ").concat(e.origin, ",\n    e.source: ").concat(e.source)); // e.source.postMessage('data');
});