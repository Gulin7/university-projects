#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int matrix1_rows, matrix1_cols, matrix2_rows, matrix2_cols;
    int **matrix1, **matrix2, **result;

    printf("Enter the number of rows of matrix 1: ");
    scanf("%d", &matrix1_rows);
    printf("Enter the number of columns of matrix 1: ");
    scanf("%d", &matrix1_cols);
    printf("Enter the number of rows of matrix 2: ");
    scanf("%d", &matrix2_rows);
    printf("Enter the number of columns of matrix 2: ");
    scanf("%d", &matrix2_cols);
    if (matrix1_cols != matrix2_rows)
    {
        printf("The matrices can't be multiplied!!! :( \n");
        return 1;
    }
    matrix1 = malloc(matrix1_rows * sizeof(int*));
    if (matrix1 == NULL)
    {
        printf("Can't allocate memory for the first matrix.\n");
        return 1;
    }
    matrix2 = malloc(matrix2_rows * sizeof(int*));
    if (matrix2 == NULL)
    {
        printf("Can't allocate memory for the second matrix.\n");
        return 1;
    }
    result = malloc(matrix1_rows * sizeof(int*));
    if (result == NULL)
    {
        printf("Can't allocate memory for the result matrix.\n");
        return 1;
    }
    for (int i = 0; i < matrix1_rows; i++)
    {
        matrix1[i] = malloc(matrix1_cols * sizeof(int));
        if (matrix1[i] == NULL)
        {
            printf("Can't allocate memory for the first matrix.\n");
            return 1;
        }
    }
    for (int i = 0; i < matrix2_rows; i++)
    {
        matrix2[i] = malloc(matrix2_cols * sizeof(int));
        if (matrix2[i] == NULL)
        {
            printf("Can't allocate memory for the second matrix.\n");
            return 1;
        }
    }
    for (int i = 0; i < matrix1_rows; i++)
    {
        result[i] = malloc(matrix2_cols * sizeof(int));
        if (result[i] == NULL)
        {
            printf("Can't allocate memory for the result matrix.\n");
            return 1;
        }
    }

    printf("Enter the elements of matrix 1: \n");
    for (int i = 0; i < matrix1_rows; i++)
        for (int j = 0; j < matrix1_cols; j++)
            scanf("%d", &matrix1[i][j]);
    printf("Enter the elements of matrix 2: \n");
    for (int i = 0; i < matrix2_rows; i++)
        for (int j = 0; j < matrix2_cols; j++)
            scanf("%d", &matrix2[i][j]);
    for (int i = 0; i < matrix1_rows; i++)
        for (int j = 0; j < matrix2_cols; j++)
        {
            result[i][j] = 0;
            for (int k = 0; k < matrix1_cols; k++)
                result[i][j] += matrix1[i][k] * matrix2[k][j];
        }
    printf("Result: \n");
    for (int i = 0; i < matrix1_rows; i++)
        for (int j = 0; j < matrix2_cols; j++)
            printf("%d ", result[i][j]);
    printf("\n");
    for (int i = 0; i < matrix1_rows; i++)
    {
        free(matrix1[i]);
        free(result[i]);
    }
    for (int i = 0; i < matrix2_rows; i++)
        free(matrix2[i]);
    free(matrix1);
    free(matrix2);
    free(result);

    return 0;
}
