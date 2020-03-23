#include<stdio.h>
int cutrod(int );
int max(int ,int,int);
main()
{
    int n,result;
    scanf("%d",&n);
    result=cutrod(n);
    printf("%d",result);

}
int cutrod(int n)
{
    int a[n+1],i,j,m;
    a[0]=0;
    a[1]=0;
    for(i=2;i<=n;i++)
    {
        a[i]=0;
        for(j=1;j<=i/2;j++)
        {
          a[i]=max(a[i],j*(i-j),j*a[i-j]);
        }
    }
    return a[i-1];
}
int max(int a,int b,int c)
{
    if(a>b)
    {
        if(a>c)
            return a;
        else
            return c;
    }
    else
    {
        if(b>c)
            return b;
        else
            return c;
    }
}
