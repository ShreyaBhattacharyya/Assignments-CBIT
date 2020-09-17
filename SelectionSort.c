#include<stdio.h>
#include<stdlib.h>
void SelectionSort(int A[] , int n)
{

    for(int i = 0;i<n-1;i++)
    {
        int min = i;
        for(int j = i+1;j<n;j++)
        {
            if(A[j]<A[min])
            min = j;
        }
        int t = A[i];
        A[i] = A[min];
        A[min] = t;
    }

    printf("Sorted Array:");
    for(int k = 0;k<=n-1;k++)
    {
        printf("%d \t",A[k]);
    }

}
int main()
{
    int B[] = {6,99,45,23,12,8};
    printf("Array before sorting");
    for(int i=0;i< 6;i++)
        printf("%d  ",B[i]);
    SelectionSort(B,6);
    return 0;

}
