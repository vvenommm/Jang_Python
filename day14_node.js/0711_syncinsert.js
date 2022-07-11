var mysql = require('sync-mysql');

var connection = new mysql({
	host: '127.0.0.1',
    user: 'root',
    password: 'aa', //mysql 설치시 설정했던 비번
    database: 'python', // db 이름
	port: 3305
});

var e_name = "남";
var sex = "M";
var addr = "탄";

var sql = `insert into emp ('e_name', 'sex', 'addr') values('${e_name}', '${sex}', '${addr}')`;

let result = connection.query(sql);
console.log(result.affectedRows);
