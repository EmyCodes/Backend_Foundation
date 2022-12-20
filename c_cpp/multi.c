#include <stdio.h>

int multi(int, int);

int main(void) {
	int result1 = multi(5, 5);
	int result2 = multi(6, 4);
	printf("\nResult = %d\nResult = %d\n", result1, result2);
	return(0);
}

int multi(int x, int y) {
	int a = x*y;
	int b = x+y;
	printf("%d\n", a);
	return b;
}
