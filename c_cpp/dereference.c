#include <stdio.h>

int main(void)
{
	int myAge = 43;

	int* ptr = &myAge;

	printf("%p\n", ptr);
	printf("%d\n", *ptr);
	return(0);
}
