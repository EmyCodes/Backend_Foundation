#!/usr/bin/node
const person = {
  name: ['Bob', 'Smith'],
  /* name: {
	  'first': 'Bob',
	  'last': 'Smith',
  } */
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old`);
  },
  intoduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  }
};

person.name;
person.name[0]; // person.name.first; person.name[1] === person.name.last;
person.age;
person.bio();
person.intoduceSelf();

function logProperty (propertyName) {
  console.log(person[propertyName]);
}

logProperty('name');
logProperty('age');
