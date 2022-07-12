EmpDao = require('./empdao.js')

var ed = new EmpDao();
list = ed.selects();

console.log(list);

list = ed.select(1);
console.log(list);
