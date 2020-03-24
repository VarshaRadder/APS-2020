#include<stdio.h>
int bc(int ,int);
main()
{
    int n,k,res;
    scanf("%d%d",&n,&k);
    printf("%d",bc(n,k));
}
int bc(int n,int k)
{
    if(n==k || k==0)
        return 1;
    else
        return bc(n-1,k-1)+bc(n-1,k);
}
