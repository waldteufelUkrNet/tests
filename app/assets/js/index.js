"use strict";

// чи відкриті ще вікна такого ж джерела?
var data = '{a:1}'; // let targetOrigin = 'file:///D:/work_area/test/app/assets/html/';

var targetOrigin = '*';
window.postMessage(data, targetOrigin); // window.addEventListener('message', (e) => {
//   console.log(`
//     e.data: ${e.data},
//     e.origin: ${e.origin},
//     e.source: ${e.source}`);
// });