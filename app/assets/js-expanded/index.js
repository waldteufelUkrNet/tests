let str = '<h1>Hello, world!</h1>';

let tag = str.match(/<(.*?)>/);
console.log("tag", tag);

console.log( tag[0] ); // <h1>
console.log( tag[1] ); // h1