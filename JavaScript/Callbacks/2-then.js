#!/usr/bin/python

export function handleResponseFromAPI(promise) {
	const myPromise = new Promise((myResolve, myReject) => {
		myResolve({
			status: 200,
			body: 'Success'
		})
	});
	myPromise
	.then((value) => console.log("Got a response from the API"))
	.catch((error) => console.log(error))
}
