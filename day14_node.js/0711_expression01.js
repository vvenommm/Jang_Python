/**
 * 
 */
const express = require('express');
const app = express()
const port = 3300;
const http = require('http');
const ejs = require('ejs');
const server = http.createServer(app);
const path = require('path');

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true }));
app.use('/static', express.static(path.join(__dirname, '/static')));

app.get('/', (req, res) => res.send("Hello World!"))

app.get('/para', (req, res) => {
	res.send('PARA<br />a = ' + req.query.a);
	console.log(req.query);
})

app.post('/post', (req, res) => {
	var abcde = req.body.abcde
	res.send('POST : ' + abcde)
})


app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/ejs', (req, res) => {
	a = "홍길동"
	b = ["홍길동", "전우치", "이순신"]
	c = [
		{'e_id' : '1', 'e_name' : '1', 'sex' : '1', 'addr' : '1'},
		{'e_id' : '2', 'e_name' : '2', 'sex' : '2', 'addr' : '2'}
	]
	res.render('abcd', {a : a, b:b, c:c});
})

app.get('/ajax', (req, res) => {
	res.render("ajax");
})

app.post('/emp_list.ajax', (req, res) => {
	var myJson = {'result' : 'OK', 'babo' : '바보'};
	res.json(myJson);
})

	
app.listen(port, () => console.log(`Example app listening on port ${port}!`))


