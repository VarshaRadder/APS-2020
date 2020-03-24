#include<stdio.h>
int min(int,int);
int bc(int,int);
main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    printf("%d",bc(n,k));
}
int bc(int n,int k)
{
    int i,j;
    int c[n+1];
    c[0]=1;
    for(j=1;j<n+1;j++)
    c[j]=0;
    for(i=1;i<=n;i++)
    {
    for(j=min(i,k);j>=1;j--)
        c[j]=c[j]+c[j-1];
    }
    return c[k];
}
int min(int a,int b)
{
if(a<b)
return a;
else
return b;
}
