#include <stdio.h>
#include <stdlib.h>

void sort_array(int *array, int length)
{
    for (int i = 0; i < length - 1; i++)
        for (int j = 0; j < length - i - 1; j++)
            if (*(array + j) > *(array + j + 1))
            {
                int swap = *(array + j);
                *(array + j) = *(array + j + 1);
                *(array + j + 1) = swap;
            }
}

void merge_sort(int *array1, int *array2, int *merged_array, int size1, int size2)
{
    int *point1 = array1; // representing the current position in array1
    int *point2 = array2; // representing the current position in array2
    int *point3 = merged_array; // the current position in the merged array
    while (point1 < array1 + size1 && point2 < array2 + size2)
        if (*point1 < *point2)
        {
            *point3 = *point1;
            point1++;
        }
        else
        {
            *point3 = *point2;
            point2++;
        }
        point3++;
    while (point1 < array1 + size1)
    {
        *point3 = *point1;
        point1++;
        point3++;
    }
    while (point2 < array2 + size2)
    {
        *point3 = *point2;
        point2++;
        point3++;
    }
}

int main()
{
    int array1[1005] = {}, array2[1005] = {}, merged_array[2010] = {},n,m;
    printf("Enter the length for the first array: ");
    scanf("%d", &n);
    printf("Enter the values for the first array: \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &array1[i]);
    printf("Enter the length for second array: ");
    scanf("%d", &m);
    printf("Enter the values for second array: \n");
    for (int i = 0; i < m; i++)
        scanf("%d", &*(array2+i));
    sort_array(array1, n);
    sort_array(array2, m);
    /*
    for(int i=0;i<n;i++)
        printf("%d ", array1[i]);
    printf("\n");
    for(int i=0;i<m;i++)
        printf("%d ", array2[i]);
    printf("\n");
    */
    merge_sort(array1, array2, merged_array, n, m);
    printf("The merged array is: \n");
    int *p = merged_array;
    for (int i = 0; i < n+m; i++)
        printf("%d ", *(p+i));
    return 0;
}



