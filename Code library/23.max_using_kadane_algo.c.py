#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<limits.h>

int start_end[2]={0};


int kadane(int a[],int size)
{
    int max=INT_MIN,tmax=0;
    int beg=0,start,end;
    
    for (int i=0;i<size;i++)
    {
        tmax=tmax+a[i];
        if (max < tmax)
        {
            max=tmax;
            start_end[0] = beg;
            start_end[1] = i;
        }
        if (tmax<0)
        {
            tmax=0;
            beg = i + 1;
        }
    }
    return max;
}
    
int main()
{
    int n,i,ans;
    int *arr;
    arr=(int*)malloc(n*sizeof(int));
    
    scanf("%d",&n);
    
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    ans=kadane(arr,n);
    printf("%d\n",ans);
    
    if(start_end[0]==0 && start_end[1]==n-1)
        ans=0;
    else{
    
    for(i=start_end[0];i<=start_end[1];i++)
    {
        free(arr+i);
    }
    
    ans=kadane(arr,n);
    
    }
    
    printf("%d\n",ans);
   
   
}