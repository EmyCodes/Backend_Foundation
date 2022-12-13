#include <stdio.h>

int main(void)
{
	char firstName[20];

	printf("What is your first name: ");
	scanf("%s", firstName);
	
	printf("Hello %s!\n", firstName);
	return(0);
}
