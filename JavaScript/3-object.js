#!/usr/bin/node
function Person (name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}

const pelumi = new Person('pelumi');
pelumi.name;
pelumi.introduceSelf();

const Emy = new Person('EmyCodes');
Emy.name;
Emy.introduceSelf();
