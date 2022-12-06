#include <stdio.h>

int main(void)
{
	char name;
	int age;
	char address;
	char* name2 = name;
	int* age2 = &age;

	printf("What is your name? ");
	scanf("%s", name2);

	printf("How old are you? ");
	scanf("%s", age2);

	printf("Welcome %s!\nYou are %iyears old", name2, age2);
	return(0);
}
