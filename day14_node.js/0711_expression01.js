/**
 * 
 */
const express = require('express');
const app = express()
const port = 3300;
const http = require('http');
const ejs = require('ejs');
const server = http.createServer(app);

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true }));

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
  res.render('abcd');
})
	
app.listen(port, () => console.log(`Example app listening on port ${port}!`))


