#include<stdio.h>

void quicksort(int set[1001],int first,int last){
   	int i, j, pivot, temp;
   	if(first<last){
      		pivot=first;
      		i=first;
      		j=last;
		while(i<j){
        		while(set[i]<=set[pivot] && i<last)
        			i++;
        		while(set[j]>set[pivot])
         			j--;
         		if(i<j){
				int aux = set[i];
				set[i] = set[j];
				set[j]=aux;
			}
		}
		int aux = set[pivot];
		set[pivot]=set[j];
		set[j]=aux;
		quicksort(set,first,j-1);
		quicksort(set,j+1,last);
	}
}
// -------------------------------
int main(){

   	int length, set[1001]={0};

	printf("Number of elements: ");
   	scanf("%d",&length);

   	printf("Enter %d elements: ", length);
   	for(int i=0;i<length;i++)
   		scanf("%d",&set[i]);

   	quicksort(set,0,length-1);
   	printf("The sorted list is: ");

	for(int i=0;i<length;i++)
  		printf(" %d",set[i]);
	printf("\n");

	return 0;
}
