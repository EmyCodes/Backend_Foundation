#include <stdio.h>

void myName(char names[]) {
	for (int i = 0; i <3; i++) {
		printf("%s\t", names[i]);
	}
}

int main(void) {
	char names = {"Ogundare", "Olamide", "Emmanuel"};
	myName(names);
	return(0);
}
