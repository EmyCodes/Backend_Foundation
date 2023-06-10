#!/usr/bin/node

setTimeout(
    function() {
        console.log("Done!!!");
    },
    3000
)

setTimeout(
    () => {
        console.log("Done!!!");
    },
    6000
)