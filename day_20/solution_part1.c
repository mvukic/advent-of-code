#include <stdio.h>
#include <math.h>

void main(){
	int sumOfPresents = 34000000;
	int houseNumber=1;
	printf("Working...\n");
	while (1==1){
		int i = 1;
		int houseNumberPresents=0;
		while(i <= sqrt(houseNumber))
		{
			if(houseNumber%i==0) {
				houseNumberPresents += i*10;
				if (i != (houseNumber / i)) {
					houseNumberPresents += (houseNumber/i)*10;
				}
			} 
			// printf("House number %d has %d presents.\n",houseNumber,houseNumberPresents);
			i++;
		}
		// printf("House number %d has %d presents.\n",houseNumber,houseNumberPresents);
		if (houseNumberPresents >= sumOfPresents){
			printf("House number %d has %d presents.\n",houseNumber,houseNumberPresents);
			break;
		}
		houseNumber++;
	}
}