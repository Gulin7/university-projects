#include <stdio.h>

int factorial(int x){
	int y;
	if(x<0) return 0;
	for(y=1;x>0;x--)
		y=y*x;
	return y;
}

int main(){
	int factorial(int n), i;
	printf("Value of n, and n!\n\n");
	for(i=0;i<=5;i++)
		printf(" %2d  %4d\n",i, factorial(i));
	return 0;
}
