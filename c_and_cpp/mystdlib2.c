#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *string;
	char str1, str2, str3, str4, str5;
	str1 = "Happy";
	str2 = "are you";
	str4 = "Emycodes";

	printf("%s %s\n", str1, str2);
	strcpy(str5, str4);
	printf("%s", str5);
	strcat(str5, ".com.ng");
	printf("%s", str5);
	return(0);
}
