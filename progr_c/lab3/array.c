#include <stdio.h>
#define SIZE 100

int a[SIZE];
void print(int *x,int n){
	int i;
	for(i=0; i<n;i++)
		printf("%d ",x[i]);
	printf("\n");
	}

int main(){

	int i;
	int b[100]={1};
	int c[100];
	int d[100];
	for (i=0;i<SIZE;i++)
		d[i]=1;
	printf("a:\n");
	print(a, SIZE);
	printf("b:\n");
        print(b, SIZE);
	printf("c:\n");
        print(c, SIZE);
	printf("d:\n");
        print(d, SIZE);

	return 0;
}
