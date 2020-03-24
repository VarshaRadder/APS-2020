#include<stdio.h>
#include<string.h>
int max(int, int);
main()
{

char a[100],b[100],lc[100][100];
int i,j,n,m;
scanf("%s",a);
scanf(" %s",b);
n=strlen(a);
m=strlen(b);
for(i=0;i<=n;i++)
{
for(j=0;j<=m;j++)
{
    lc[i][j]=0;
}
}
for(i=1;i<=n;i++)
{
for(j=1;j<=m;j++)
{
if(a[i-1]==b[j-1])
lc[i][j]=lc[i-1][j-1]+1;

else
lc[i][j]=max(lc[i-1][j],lc[i][j-1]);
}}

printf("%d",lc[n][m]);
}
int max(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;

}
