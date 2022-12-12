#include <stdio.h>

void reciprocal(int x){
	x=(float)x;
	printf("%.2f\n",(float)1/x);
}

void square(int x){
	printf("%d\n", x*x);
}

void performtask(int n1, int n2, void (*f)(int)){
	for(int i=n1;i<=n2;i++){
		f(i);
	}
}
int main(){
	performtask(1,3,reciprocal);
	performtask(2,5,square);
return 0;
}
