const mysql = require('mysql');

const connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: 'aa', //mysql 설치시 설정했던 비번
    database: 'python', // db 이름
	port: 3305
});

connection.connect((err) => {
    if (err) {
        console.log(err);
        connection.end();
        throw err;
    } else {
		const sql = "select e_id, e_name, sex, addr from emp"
		connection.query(sql, function(err, result, fields){
			if(err) throw err;
			console.log("결과", result);
			console.log("결과", result[0].E_ID);
		})
        console.log("DB 접속 성공");
    }
});


module.exports = connection;
