#include <stdio.h>

void myFunction() {
	printf("I just got executed!\n");
}

int main(void) {
	myFunction();
	myFunction();
	myFunction();
	return(0);
}
