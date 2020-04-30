#include<stdio.h>
#include<stdlib.h>
//using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        long int n,k,i,sum=0;
        scanf("%ld %ld",&n,&k);
        long int b[n];
        for(i=0;i<n;i++)
        {
            scanf("%ld",&b[i]);
        }
        for(i=0;i<n;i++)
        {
            if(b[i]%k==0)
                sum=sum+0;
            else
                sum=sum+(b[i]%k);
        }
        while(1)
        {
            if(sum<k)
            {
                printf("%ld\n",sum);
                break;
            }
            else
            {
              sum=sum%k;
            }
        }

    }
    return 0;
}
