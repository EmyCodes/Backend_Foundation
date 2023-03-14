#!/usr/bin/node
function createPerson (name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
  return obj;
}

const pelumi = createPerson('pelumi');
pelumi.name;
pelumi.introduceSelf();

const Emy = createPerson('EmyCodes');
Emy.name;
Emy.introduceSelf();
