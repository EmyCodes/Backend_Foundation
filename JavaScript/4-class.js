#!/usr/bin/node
//Class Definition

class Person {
	
	name;
	constructor(name) {
		this.name = name;
	}
	introduceSelf() {
		console.log(`Hi! I'm ${this.name}`)
	}
}
//class Declaration
const giles = new Person('Giles');
giles.introduceSelf();


//Inheritance

class Professor extends Person {

	subject;

	constructor(name, subject) {
		super(name);
		this.subject = subject;
	}

	introduceSelf() {
		console.log(`My name is ${this.name}, and I will be your ${this.subject} professor.`);
	}

	grade(paper) {
		const grade = Math.floor(Math.random() * (5-1) + 1);
		console.log(grade);
	}
}

const walsh = new Professor('Walsh', 'Psychology');
walsh.introduceSelf();
walsh.grade();

//Encapsulation

class Student extends Person {
	#year;

	constructor(name, year) {
		super(name);
		this.#year = year;
	}

	introduceSelf() {
		console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
	}

	canStudyArchery() {
		return this.#year > 1;
	}
}
//Declaration
const summers = new Student('Summers', 2);

summers.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
summers.canStudyArchery(); // true

//summers.#year; // SyntaxError
