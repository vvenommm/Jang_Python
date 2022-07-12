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

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true }));

app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => res.send("Hello World!"))
app.get('/emp_list', (req, res) => {
	var ep = new EmpDao();
	let list = ep.selects();
	
	res.render("emp_list", {list : list});
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
