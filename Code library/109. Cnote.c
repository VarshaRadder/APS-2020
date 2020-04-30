#include <stdio.h>

int main(void) {
	int j,m,x,y,k,n,p,c,t,flag=0;
	scanf("%d",&t);
	while(t--)
	{
	    flag=0;
	    scanf("%d%d%d%d",&x,&y,&k,&n);
	    for(j=0;j<n;j++)
	    {
	        scanf("%d%d",&p,&c);
	        m=x-y;
	        if(p>=m&&k>=c)
	        {
	            flag++;

	        }

	    }
	        if(flag>0)
	        printf("LuckyChef\n");
	        else
	        printf("UnluckyChef\n");

	}
	return 0;
}
