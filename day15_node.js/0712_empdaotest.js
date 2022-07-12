EmpDao = require('./empdao.js')

var ed = new EmpDao();
list = ed.selects();
console.log(list);
console.log("\n============================\n");

list = ed.select(1);
console.log(list);
console.log("\n============================\n");

cnt = ed.insert('규', '하하', '남');
console.log("cnt", cnt);
list = ed.selects();
console.log(list);
console.log("\n============================\n");
