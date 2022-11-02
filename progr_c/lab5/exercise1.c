#include <stdio.h>

int max_matrix(int a[10][10], int n, int m){
	int maxim=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++)
			if(a[i][j]>maxim)
				maxim=a[i][j];
	}
	//printf(maxim);
	return maxim;
}

int main(){
	int n,m,a[10][10]={0};
	scanf("Enter an integers: %d", &n);
	scanf("Enter an integer: %d", &m);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			scanf("%d",&a[i][j]);
	printf(max_matrix(a,n,m));
	return 0;
}
