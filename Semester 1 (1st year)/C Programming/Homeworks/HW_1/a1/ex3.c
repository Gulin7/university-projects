#include <stdio.h>

int main(){
	int a,max,min;
	printf("Enter a number: ");
	scanf("%d", &a);
	max = a;
	min = a;
	for(int i=1;i<=4;i++){
		printf("Enter a number: ");
		scanf("%d", &a);
		if(a<min)
			min=a;
		if(a>max)
			max=a;
	}
	printf("The maximum is %d and the minimum is %d!\n",max,min);
	return 0;
}
