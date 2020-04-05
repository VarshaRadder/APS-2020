#include <stdio.h>

int josephus(int n, int k)
{
 int res = 0;
 for (int i = 1; i <= n; ++i)
 res = (res + k) % i;
 return res + 1;
}


int main() {
	int a,n,k;

	scanf("%d%d",&n,&k);
	a=josephus(n,k);
	printf("%d",a);
	return 0;
}
