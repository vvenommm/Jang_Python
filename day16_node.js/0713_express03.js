/**
 * 
 */
EmpDao = require('./empdao.js');

const express = require('express');
const app = express()
const port = 3300;
const http = require('http');
const ejs = require('ejs');
const server = http.createServer(app);
const bodyParser = require('body-parser');

var ep = new EmpDao();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended : false}));
app.use(bodyParser.json());
app.use(express.static(__dirname + '/'));


app.get('/', (req, res) => res.send("Hello World!"))

app.get('/emp', (req, res) => {
	res.render('emp', {});
})

app.post('/emp_list.ajax', function(req, res) {
	var list = ep.selects();
	res.json({'list' : list});
})

app.post('/emp_detail.ajax', function(req, res) {
	const e_id = req.body.e_id;
	var emp = ep.select(e_id);
	
	res.json({'emp' : emp});
})

app.post('/emp_update.ajax', function(req, res) {
	const e_id = req.body.e_id;
	const e_name = req.body.e_name;
	const addr = req.body.addr;
	var cnt = ep.update(e_id, e_name, addr);
	
	res.json({'cnt' : cnt});
})

app.post('/emp_insert.ajax', function(req, res) {
	const e_name = req.body.e_name;
	const sex = req.body.sex;
	const addr = req.body.addr;
	var cnt = ep.insert(e_name, sex, addr);
	
	res.json({'cnt' : cnt});
})

app.post('/emp_delete.ajax', function(req, res) {
	const e_id = req.body.e_id;
	var cnt = ep.delete(e_id);
	
	res.json({'cnt' : cnt});
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
