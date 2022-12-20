#include <stdio.h>

struct myStructure {
	int myNum;
	char myLetter;
};

int main(void) {
	struct myStructure s1;
	s1.myNum = 13;
	s1.myLetter = 'D';
	printf("My number = %d\n", s1.myNum);
	printf("My Letter = %c\n", s1.myLetter);
	return(0);
}
