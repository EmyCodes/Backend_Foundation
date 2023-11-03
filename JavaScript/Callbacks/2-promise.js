#!/usr/bin/node

const myPromise = new Promise((myResolve, myReject) => {
  const x = 0;

  if (x == 0) {
	    myResolve('OK');
  } else {
    	myReject('Error');
  }
});

myPromise.then(
  (value) => console.log(value),
  (error) => console.log(error)
);
