#include <stdio.h>

void check_big_case(char *, char *);
void check_small_case(char *, char *);

char bc[100], sc[100];
int main()
{
    char s[100];
    printf("Enter a string: ");
    gets(s);
    check_big_case(&s[0], &bc[0]);
    printf(bc);
    printf("\n");
    check_small_case(&s[0], &sc[0]);
    printf(sc);
    return 0;
}