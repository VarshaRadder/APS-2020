#include<stdio.h>
main()
{
int test,n,c,i,k;
scanf("%d",&test);
for(i=1;i<=test;i++)
{
scanf("%d%d",&n,&c);
int a[n],sum=0;
for(k=0;k<n;k++)
{
scanf("%d",&a[k]);
sum=sum+a[k];
}
if(sum<=c)
printf("Yes\n");
else
printf("No\n");
}
}
