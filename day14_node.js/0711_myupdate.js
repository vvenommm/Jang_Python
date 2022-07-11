const mysql = require('mysql');

const connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: 'aa', //mysql 설치시 설정했던 비번
    database: 'python', // db 이름
	port: 3305
});


connection.connect();
	var e_id = 14;
	var e_name = "남";
	var sex = "M";
	var addr = "탄";
	
	var sql = `update emp set e_name = '${e_name}', sex = '${sex}', addr =  '${addr}' where e_id = '${e_id}'`;
	
connection.query(sql, function(err, results, fields){
	console.log("결과", results.affectedRows); 
	connection.end();
});
