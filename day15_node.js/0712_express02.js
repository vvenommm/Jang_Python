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

var ep = new EmpDao();

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true }));

app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => res.send("Hello World!"))
app.get('/emp_list', (req, res) => {
	let list = ep.selects();
	res.render("emp_list", {list : list});
})

app.get('/emp_detail', (req, res) => {
	var e_id = req.query.e_id;
	var emp = ep.select(e_id);
	
	res.render("emp_detail", {emp : emp});
})

app.get('/emp_mod', (req, res) => {
	var e_id = req.query.e_id;
	var emp = ep.select(e_id);
	
	res.render("emp_mod", {emp : emp});
})

app.post('/emp_mod_act', (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var addr = req.body.addr;
	
	var cnt = ep.update(e_id, e_name, addr);
	
	res.render("emp_mod_act", {cnt : cnt});
})

app.get('/emp_del_act', (req, res) => {
	var e_id = req.query.e_id;
	
	var cnt = ep.delete(e_id);
	
	res.render("emp_del_act", {cnt : cnt});
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
