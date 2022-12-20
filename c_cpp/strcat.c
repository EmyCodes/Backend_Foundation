#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[20] = "Hello ";
	char str2[] = "World!";

	// Concateate str2 to str1

	strcat(str1, str2);
	printf("%s\n", str1); 
}
