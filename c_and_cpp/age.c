#include <stdio.h>

int main(void)
{
	int myAge = 25;
	int votingAge = 18;

	if (myAge >= votingAge)
	{
		printf("Old enough to Vote!\n");
	}
	else
	{
		printf("Not Old Enough to vote!\n");
	}
	return(0);
}
