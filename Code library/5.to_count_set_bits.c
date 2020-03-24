#include <stdio.h>

main()
{
    int n,count=0;
    printf("Enter a number");
    scanf("%d",&n);
    while(n)
    {
        count++;
        n = n & n-1;
    }
    printf("The number of set bits are %d\n",count);
}
