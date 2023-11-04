#!/usr/bin/node

export function getFullResponseFromAPI(success) {
	const myPromise = new Promise((myResolve, myReject) => {
		if (success === true) {
			myResolve(
				{
					status: 200,
					body: 'Success'
				}
			)
		} else {
			myReject("The fake API is not working currently")
		}
	});
//	myPromise
//	.then((value) => console.log(value))
//	.catch((error) => console.log(error));
	return myPromise;
}
