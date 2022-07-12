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
		return result[0];
	}
	
	insert(e_name, sex, addr){
		var sql = `insert into emp (e_name, sex, addr) values('${e_name}', '${sex}', '${addr}')`;
		let result = this.connection.query(sql);
		return result.affectedRows;
	}
	
	update(e_id, e_name, addr){
		var sql = `update emp set e_name = '${e_name}', addr = '${addr}' where e_id = '${e_id}'`;
		let result = this.connection.query(sql);
		return result.affectedRows;
	}
	
	delete(e_id){
		var sql = `delete from emp where e_id = '${e_id}'`;
		let result = this.connection.query(sql);
		return result.affectedRows;
	}
}

module.exports = EmpDao
