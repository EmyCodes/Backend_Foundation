#include <stdio.h>

int main(void) {
	int scores[5], i;
	float sum=0, avg;
	for (i=0; i <5; i++) {
		printf("Type the members of the array according to their INDEX: ");
		scanf("%d", &scores[i]);
		printf("\n");
	}
	for (i=0; i <5; i++) {
		sum = sum + scores[i];
	}
	avg=sum/5;
	printf("%f\n", avg);
	printf("%f\n", sum);
	for (i=0; i<5; i++) {
		printf("%i ", scores[i]);
	}
	printf("\n");
	return(0);
}
