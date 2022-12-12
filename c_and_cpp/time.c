#include <stdio.h>

int main(void)
{
	int time = 22;

	if (time < 10)
	{
		printf("Good Morning!\n");
	}
	else if (time < 20)
	{
		printf("Good Day!\n");
	}
	else
	{
		printf("Good Evening\n");
	}
}
