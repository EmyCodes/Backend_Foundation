#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[20] = "Hello World";
	char str2[20];
	
	// Copy str1 to str2
	strcpy(str2, str1);
	printf("%s\n", str2);
	return(0);
}
