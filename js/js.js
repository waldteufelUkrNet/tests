// Напишите функцию, которая умеет генерировать календарь для заданной пары (месяц, год).
// Календарь должен быть таблицей, где каждый день – это TD. У таблицы должен быть заголовок с названиями дней недели, каждый день – TH.
// Синтаксис: createCalendar(id, year, month).
// Такой вызов должен генерировать текст для календаря месяца month в году year, а затем помещать его внутрь элемента с указанным id.
// Например: createCalendar("cal", 2012, 9) сгенерирует в <div id=„cal“></div> следующий календарь:

function createCalendar(id, year, month) {
  let elem = document.getElementById(id);

  let table = document.createElement('table');
  elem.appendChild(table);

  table.innerHTML  = '<thead>\
                        </tr>\
                          <th>пн</h>\
                          <th>вв</h>\
                          <th>ср</h>\
                          <th>чт</h>\
                          <th>пт</h>\
                          <th>сб</h>\
                          <th>нд</h>\
                        </tr>\
                      </thead>\
                      <tbody></tbody>';

  let tbody = table.getElementsByTagName('tbody')[0];

  let date = new Date(year, month-1, 1);
  // день тижня для першого числа
  let weekDay = date.getDay();
  // кількість днів в цьому місяці
  let daysInMonth = (new Date(year, month, 1) - date)/(24*60*60*1000);

  let tbodyHTML = '<tr>';
  let weekCount = 0;

  // заповнюємо пустими місцями початок місяця
  if ( weekDay != 0 ) {
    for ( let i=0; i<weekDay-1; i++ ) {
      tbodyHTML += '<td></td>';
      weekCount++;
    }
  }

  for ( let i=1; i<daysInMonth+1; i++ ) {
    tbodyHTML += '<td>' + i + '</td>';
    weekCount++;

    if ( weekCount > 6 && i != daysInMonth ) {
      tbodyHTML += '</tr><tr>';
      weekCount = 0;
    } else if ( weekCount > 6 && i == daysInMonth ) {
      tbodyHTML += '</tr>';
    }
  }

  tbody.innerHTML = tbodyHTML;
  // добиваємо залишок пустих чарунок
  if ( tbody.lastChild.children.length < 7 ) {

    let count = 7-tbody.lastChild.children.length;
    console.log("count", count);

    for ( let i = 0; i < count; i++ ) {
      let cell = document.createElement('td');
      tbody.lastChild.append(cell);
    }
  }
}

createCalendar('calendar', 2019, 4)