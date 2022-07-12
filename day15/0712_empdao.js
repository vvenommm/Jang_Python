var mysql = require('sync-mysql');

class EmpDao{
	constructor(){
		this.connection = new mysql({
			host : '127.0.0.1',
			user : 'root',
			password : 'aa',
			database : 'python',
			port : '3305'
		});
	}
	
	selects(){
		var sql = `select e_id, e_name, sex, addr from emp`;
		let result = this.connection.query(sql);
		return result;
	}
	
	select(id){
		var sql = `select e_id, e_name, sex, addr from emp where e_id = '${id}'`;
		let result = this.connection.query(sql);
		return result;
	}
}

module.exports = EmpDao
