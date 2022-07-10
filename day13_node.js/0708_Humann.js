Animall = require('./animall.js')

class Humann extends Animal{
	constructor(){
		super();
		this.height = 0;
	}
	
	//메소드
	taller(){
		this.height += 10;
		return this.height;
	}
}
module.exports = Humann;
