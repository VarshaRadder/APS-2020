#include<stdio.h>
main()
{
int i,n,j,k,ta,a[100],b[100][100];
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%d",&a[i]);
for(i=0;i<=n;i++)
{
b[i][0]=1;
for(j=1;j<=n;j++)
b[i][j]=0;
}
for(i=1;i<=3;i++)
{
for(j=1;j<=n;j++)
b[i][j]=b[i-1][j]+b[i][j-a[i-1]];
}
for(i=0;i<=n;i++)
{
for(j=0;j<=n;j++)
printf("%d\t",b[i][j]);
printf("\n");
}
}