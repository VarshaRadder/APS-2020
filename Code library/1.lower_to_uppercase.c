#include<stdio.h>
int main()
{
    char a;
    printf("Enter a character:");
    scanf("%c",&a);
    a=a & (~32);
    printf("Uppercase of character:%c",a);
    return 0;
}
