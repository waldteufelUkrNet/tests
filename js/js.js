setInterval(function(){

  let date = new Date();
  let hh = date.getHours();
  let mm = date.getMinutes();
  let ss = date.getSeconds();
  if ( hh < 10 ) hh = '0' + hh;
  if ( mm < 10 ) mm = '0' + mm;
  if ( ss < 10 ) ss = '0' + ss;

  document.getElementsByClassName('hour')[0].innerHTML = hh;
  document.getElementsByClassName('min')[0].innerHTML  = mm;
  document.getElementsByClassName('sec')[0].innerHTML  = ss;

},1000);