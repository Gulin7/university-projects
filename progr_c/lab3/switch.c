#include <stdio.h>
#include <string.h>


int main(){

	int vowels=0, nonvowels=0;

	char s[]="afjdHJIouaIk";
	int l=strlen(s);
	for(int i=0;i<l;i++)
		switch(s[i])
		{
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u': vowels ++;
				 break;
			default: nonvowels++;
		};
	printf("Vowels:%d ", vowels);
	printf("\n");
	printf("Nonvowels:%d\n", nonvowels);
	return 0;
}
