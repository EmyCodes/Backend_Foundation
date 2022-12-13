 #include <stdio.h>

int main(void)
{
	char fullName[30];

	printf("Type your full name: ");
	scanf("%s", fullName);

	printf("Hello %s!\n", fullName);
	return(0);
}
