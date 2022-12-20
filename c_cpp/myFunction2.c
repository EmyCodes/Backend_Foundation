#include <stdio.h>

void myfunc(char name[], int age) {
	printf("Hello %s.\nYou're of age %d\n", name, age);
}

int main(void) {
	myfunc("Emmy", 13);
	myfunc("Inno", 26);
	return(0);
}
