// чи відкриті ще вікна такого ж джерела?
// парсинг фрейма?
// як звернутися до довільної вкладки?

let data = '{a:1}';
// let targetOrigin = 'file:///D:/work_area/test/app/assets/html/';
let targetOrigin = '*';
window.postMessage(data,targetOrigin);



// window.addEventListener('message', (e) => {
//   console.log(`
//     e.data: ${e.data},
//     e.origin: ${e.origin},
//     e.source: ${e.source}`);
// });