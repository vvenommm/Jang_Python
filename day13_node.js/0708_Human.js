import Animal from './animal.js';

class Human extends Animal{
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

export default Animal;
