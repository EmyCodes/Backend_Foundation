#include <stdio.h>

int main(void) {
	int numbers[10], i;
	int even=0, odd=0;

	for (i=0; i<10; i++) {
		printf("ENTER THE ARRAY ACCORDING TO THEIR RESPECTIVE INDEX: ");
		scanf("%d", &numbers[i]);
/*		if (numbers[i]%2 == 0) {
			even = even + 1;
		}
		else {
			odd = odd + 1;
		}
		printf("The number of Even in the Array is %d\n", even);
		printf("The number of Odd in the Array is %d\n", odd);
*/
	}
	for (i = 0; i< 10; i++) {
		if (numbers[i]%2 == 0) {
			even = even + 1;
		}
		else {
			odd = odd + 1;
		}
	}
	printf("The number of Even in the Array is %d\n", even);
	printf("The number of Odd in the Array is %d\n", odd);
	return(0);
}
