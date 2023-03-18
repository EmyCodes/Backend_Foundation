#!/usr/bin/node
function turnIntoAMartian(myName) {
	function recallName(myName) {
		const martianName = myName + " Martian";
		return martianName;
	}
	const martianName = recallName(myName);
	return martianName;
}
console.log(turnIntoAMartian("MyName"));
