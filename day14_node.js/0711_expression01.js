/**
 * 
 */
const express = require('express');
const app = express()
const port = 3300;

app.get('/', (req, res) => res.send("Hello World!"))

app.get('/para', (req, res) => {
	res.send('PARA<br />a = ' + req.query.a);
	console.log(req.query);
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
