#include<stdio.h>
int main()
{
int i,n,j,k,ta,m;
long int a[1000],b[1000][1000];
//n: an integer, the amount to make change for
//m: the number of coin types
scanf("%d%d",&n,&m);
for(i=0;i<m;i++)
scanf("%ld",&a[i]);  //a: an array of integers representing available denominations
for(i=0;i<=m;i++)
{
b[i][0]=1;
for(j=1;j<=n;j++)
b[i][j]=0;
}
for(i=1;i<=m;i++)
{
for(j=1;j<=n;j++)
b[i][j]=b[i-1][j]+b[i][j-a[i-1]];
}
printf("%ld\t",b[m][n]);
return 0;
}
