let field = document.getElementById('field');
let ball  = document.getElementById('ball');

field.onmouseup = function(event){

  // координати кліку
  let clickTop  = event.clientY;
  let clickLeft = event.clientX;

  // координати внутрішної частини поля
  fieldTop    = field.offsetTop + field.clientTop;
  fieldLeft   = field.offsetLeft + field.clientLeft;
  fieldRight  = fieldLeft + field.clientWidth;
  fiefdBottom = fieldTop + field.clientHeight;


// console.log(`
// ==================================================
// координати зовнішнього лівого верхнього кута поля:
// field.offsetTop  : ${field.offsetTop}
// field.offsetLeft : ${field.offsetLeft}
// ==================================================
// товщина бортів:
// field.clientTop  : ${field.clientTop}
// field.clientLeft : ${field.clientLeft}
// ==================================================
// зовнішні розміри поля:
// field.offsetWidth  : ${field.offsetWidth}
// field.offsetHeight : ${field.offsetHeight}
// внутрішні розміри поля:
// field.clientWidth  : ${field.clientWidth}
// field.clientHeight : ${field.clientHeight}
// ==================================================
// координати внутрішної частини поля:
// fieldTop    : ${fieldTop}
// fieldLeft   : ${fieldLeft}
// fieldRight  : ${fieldRight}
// fiefdBottom : ${fiefdBottom}
// ==================================================
// `);

  // розміри м'яча
  let ballWidth        = ball.offsetWidth;

  let ballTop  = clickTop - fieldTop - ballWidth/2;
  let ballLeft = clickLeft - fieldLeft - ballWidth/2;

  if ( ballTop < 0 ) {
    ballTop = 0;
  } else if ( ballTop + ballWidth > field.clientHeight ) {
    ballTop = field.clientHeight - ballWidth;
  }

  if ( ballLeft < 0 ) {
    ballLeft = 0;
  } else if ( ballLeft + ballWidth > field.clientWidth ) {
    ballLeft = field.clientWidth - ballWidth;
  }

  ball.style.top  = ballTop + 'px';
  ball.style.left = ballLeft + 'px';
};