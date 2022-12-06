#include <stdio.h>
#define SIZE_1 50
#define SIZE_2 50

void main(int a)
{
	
	int apro = 300;
	int date = 400;
	int animal = 500;

	printf("\nShoprite Retail\n");
	printf("No 4, Lekki Phase 2, Gerrade Road, Lagos\n");

	a = 0;
	while(a < SIZE_1)
	{
		putchar('-');
		a++;
	}
	printf("\n\n");
	printf("Product\t\tPrice per pack\n");
	printf("Aprocot\t\t%i\n", apro);
	printf("Dates\t\t%d\n", date);
	printf("Animal\t\t%d\n", animal);
	printf("Combo-1\t\t%.1f\n", 630.0);
	printf("Combo-2\t\t%.1f\n", 810.0);
	printf("Combo-3\t\t%.1f\n", 720.0);
	printf("GiftBox\t\t%d\n\n", 900);
	
	a = 0;
	while(a < SIZE_2)
	{
		putchar('*');
		a++;
	}

	printf("\nFor Free Delivery, contact 080 300 4567 789\n");
	
	a = 0;
	while(a < SIZE_2)
	{
		putchar('*');
		a++;
	}
	printf("\n\n");
	return(0);
}
