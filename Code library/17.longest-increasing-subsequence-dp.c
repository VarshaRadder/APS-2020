#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lis(int a[], int n)
{
    int i, j,lst[n],max=0;
    for(i = 0; i < n; i++)
        lst[i] = 1;

    for(i = 1; i < n; i++) {
        for(j = 0; j < i; j++) {
            if(a[i] > a[j] && lst[i] < lst[j]+1)
                lst[i] = lst[j]+1;
        }
    }

    for(i = 0; i < n; i++)
    {
        if(lst[i] > max)
            max = lst[i];
    }
    return max;
}

int main()
{
    int n,res,i;
    printf("Enter the array size");
    scanf("%d",&n);
    int *arr=(int *)malloc(n*sizeof(int));
    for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
    res=lis(arr,n);
    printf("%d\n", res);
    return 0;
}
