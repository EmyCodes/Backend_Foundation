#include <stdio.h>
#include <string.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char *string;
	
	string = (char *)malloc(80);
	if(string==NULL)
	{
	puts("Not enough memory");
	return(0);
	}
	strcpy(string,"Howdy! Howdy! Hi!");
	printf("%s\n",string);
	return(0);
}
