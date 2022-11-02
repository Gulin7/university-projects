#include <stdio.h>

int fibonacci(int n){
	int x1=1, x2=1;
	for(int i=3; i<=n;i++){
		int aux=x1+x2;
		x1=x2;
		x2=aux;
	}
	return x2;
}

int main(){
	int n;
	scanf("Enter your number: %d", &n);
	printf("%d", fibonacci(n));
	return 0;
}
