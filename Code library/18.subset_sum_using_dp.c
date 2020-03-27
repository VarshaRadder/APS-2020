#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int subset_sum(int a[], int n, int sum)
{
    int ss[n+1][sum+1];
    int i,j;
    for(i = 0; i <= n; i++)
        ss[i][0] = 1;
    for(j = 1; j <= sum; j++)
        ss[0][j] = 0;

    for(i = 1; i <= n; i++) {
        for(j = 1; j <= sum; j++){
            if(ss[i-1][j] == 1)
                ss[i][j] = 1;
            else
            {
                if(a[i-1] > j)
                    ss[i][j] = 0;
                else
                    ss[i][j] = ss[i - 1][j - a[i-1]];
            }
        }
    }

    return ss[n][sum];
}

int main()
{
    int n,sum;
    printf("Enter the array size\n");
    scanf("%d",&n);
    int *a=(int *)malloc(n*sizeof(int ));
    printf("Enter the array elements\n");
    for(int i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("Enter sum\n");
    scanf("%d",&sum);
    int result=subset_sum(a,n,sum);

    if(result)
        printf("Subset found\n");
    else
        printf("Subset not found\n");

    return 0;
}
