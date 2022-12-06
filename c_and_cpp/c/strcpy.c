#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char* string;
	
	string = (char *)malloc(80);
/*	char str1 = "Happy";
	char str2 = "Month";
	char str3[20];
	char str4[20];
	char str5[] = "Emy";

	strcpy(str2, str1);
	strcpy(str4, str5);
*/
	strcpy(string, "He is Innocent");
/*	printf("str2 = %s\nstr3 = %s\nstr4 = %s\nstr1 = %s\nstr5 = %s", &str2, &str3, &str4, &str1, &str5);*/
	printf("%s\n", string);
	return(0);
}
