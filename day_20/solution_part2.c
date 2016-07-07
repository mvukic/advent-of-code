#include <stdio.h>
#include <math.h>
#define n 1000000

void main(){
	int sumOfPresents = 34000000;
	int houses[n]={0};
	printf("Working...\n");
	for(int i=1;i<n;i++){
		int count=0;
		for(int j=i;j<n;j+=i){
			houses[j] += i*11;
			count++;
			if (count == 50){
				break;
			}
		}
	}
	for(int i=0;i<n;i++){
		if(houses[i] >= sumOfPresents){
			printf("House number is %d.\n",i);
			break;
		}
	}
}