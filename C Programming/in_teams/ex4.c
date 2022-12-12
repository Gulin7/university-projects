#include <stdio.h>

int main(){
	int row, col, sum, matrix[101][101]={0};

	printf("Enter number of rows: ");
	scanf("%d", &row);
	printf("Enter number of columns: ");
	scanf("%d", &col);

	for(int i=1;i<=row;i++){
		sum=0;
		for(int j=1;j<=col;j++){
			printf("Enter element on row %d and column %d: ", i,j);
			scanf("%d", &matrix[i][j]);
			sum += matrix[i][j];
			}
		printf("Sum on row %d is = %d !!!\n", i, sum);
	}

	return 0;
}

