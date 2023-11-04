#!/usr/bin/node

import { signUpUser } from "./4-user-promise"
import { uploadPhoto } from "./5-photo-reject"

export default function handleProfileSignup(firstName, lastName, fileName) {
	const myPromise = Promise.allSettle([
		signUpUser(), uploadPhoto()
	])
	.then((value) => {
		console.log
	})
	.catch(() => 
		
	);
}
