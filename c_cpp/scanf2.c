#include <stdio.h>

int main(void)
{
	int myNum;
	char myChar;

	printf("Type a number and a character and hit ENTER: ");
	scanf("%d %c", &myNum, &myChar);
	printf("Your number is %d\n", myNum);
	printf("Your character is %c\n", myChar);
	return(0);
}
