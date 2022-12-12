#include <stdio.h>

int main(){
   int num1, num2, *p, *q, sum=0;

   printf("Enter two integers: \n");
   scanf("%d %d", &num1, &num2);

   p = &num1;
   q = &num2;

   sum = *p + *q;
   printf("Sum of the numbers = %d\n", sum);

   return 0;
}
