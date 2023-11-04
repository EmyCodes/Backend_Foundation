#!/usr/bin/node

export function getResponseFromAPI() {
	const myPromise = new Promise((myResolve, myReject) => 
		{
		myResolve("OK")});
	return myPromise
}
