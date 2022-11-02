#include<stdio.h>

int main()
{
  int coins = 0, k;
  printf("Enter a number: ");
  scanf("%d", &k);
  while (k > 0)
  {
    while (k >= 5)
    {
      coins++;
      k -= 5;
    }
    while (k >= 2)
    {
      coins++;
      k -= 2;
    }
    while (k > 0)
    {
      coins++;
      k -= 1;
    }
  }
  printf("The minimum numbers of coins needed is: %d\n", coins);
  return 0;
}
