#!/usr/bin/node

import { uploadPhoto, createUser } from "./utils";

export function handleProfileSignup() {
	const myPromise = Promise.all([createUser(), uploadPhoto()]);
//	myPromise
//	return Promise.allSettled([createUser(), uploadPhoto()])
//		.then((value) => {
//			console.log(`${value[1].value.body} ${value[0].value.firstName} ${value[0].value.lastName}`);
//		})
//		.catch(() => 
//			console.log("Signup system offline"),
//		);
		// return myPromise;
	myPromise
	.then((value) => {
		console.log(`${value[1].value.body} ${value[0].value.firstName} ${value[0].value.lastName}`);
	})
	.catch(() => 
		console.log("Signup system offline"),
	);
}
