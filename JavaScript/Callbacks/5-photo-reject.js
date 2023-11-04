#!/usr/bin/node

export default function uploadPhoto(filename) {
	return Promise.reject(`${filename} cannot be processed`)
	.catch((error) => console.log(error));
}
