#include <stdio.h>

void fibonacci(int n)
{
    int x1 = 1, x2 = 1, aux;
    if (n == 1)
        printf("%d", x1);
    else if (n > 1)
    {
        printf("%d %d ", x1, x2);
        for (int i = 3; i <= n; i++)
        {
            aux = x1 + x2;
            x1 = x2;
            x2 = aux;
            printf("%d ", x2);
        }
        printf("\n");
    }
}
int main()
{
    int n, m, b[1000] = {0};
    printf("Enter a number: ");
    scanf("%d", &n);
    fibonacci(n);
    printf("Enter another number: ");
    scanf("%d", &m);
    b[1] = 1;
    b[2] = 1;
    for (int i = 3; i <= m; i++)
    {
        b[i] = b[i - 1] + b[i - 2];
    }
    for (int i = 1; i <= m; i++)
    {
        printf("%d ", b[i]);
    }
    printf("\n");
}