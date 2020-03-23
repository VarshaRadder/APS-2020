#include<stdio.h>
main()
{
    char a;
    printf("Enter a character:");
    scanf("%c",&a);
    a = a | 32;
    printf("Lowercase of character:%c", a);
}
