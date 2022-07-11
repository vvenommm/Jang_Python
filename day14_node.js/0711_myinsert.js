const mysql = require('mysql');

const connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: 'aa', //mysql 설치시 설정했던 비번
    database: 'python', // db 이름
	port: 3305
});


connection.connect();

	var e_name = "남";
	var sex = "M";
	var addr = "탄";
	
	var sql = `insert into emp ('e_name', 'sex', 'addr') values('${e_name}', '${sex}', '${addr}')`;

connection.query(sql, function(err, result, fields){
	console.log("결과", result); 
	connection.end();
});	
