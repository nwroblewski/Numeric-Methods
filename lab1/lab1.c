#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

int tab = 0;
double *array;
int N = 10000000;
double y = 0;
double t = 0;

float kahan(int N, float *arr){
	float sum = arr[0];
	float c  = 0.0;
	for(int i =1; i<N; i++){
		y = arr[i] - c;
		t = sum + y;
		c = (t - sum) - y;
		sum = t;
	}
	return sum;
}


float add(int how_much){
	if(how_much <= 0){
		return 0;	
	}
	if(how_much ==1){
		return array[tab++];	
	}
	int left = how_much/2;
	int right = how_much - left;

	return add(left) + add(right);
}

int main(){
	clock_t start1, end1, start2, end2, start3, end3;
	double cpu_time_used1;
	double cpu_time_used2;
	//0.551223
	//0.114758
	//0.002341
    double end = 0.002341;
    array = malloc(N*sizeof(double));
    double sum = 0;
    double sum_1 = 0;
	double sum_2 = 0;
    
    for(int i=0; i<N; i++){
		array[i] = end;
    }
	start1 = clock();
    for(int i=0; i<N; i++){
		if(i%50000 == 0){
	    	printf("%lf \n",sum - ((i+1) * end));	
	}	
	
	sum+=array[i];
    }
	end1 = clock();
	
	start2 = clock();
    sum_1 = add(N);	
	end2 = clock();

	start3 = clock();
    sum_2 = kahan(N,array);	
	end3 = clock();

	// printf("Wartosc sumowana wiele razy: %lf \n",end);
	// printf("Rozmiar tablicy: %d \n", N);

    // printf("Suma normalna to: %lf \n", sum);
    // printf("Suma rekursywna to: %lf \n", sum_1);
	// printf("Suma kahana to: %lf \n", sum_2);

    // printf("Przemnozone to: %lf \n",end*N);

	// printf("Błedy bezwgledne: \n");

     printf("Naiwnie: %lf \n", (end*N) - sum);
	// printf("Rekursywnie: %lf \n",(end*N) - sum_1);
	// printf("Kahana: %lf \n",(end*N) - sum_2);

	// printf("Bledy wzgledne: \n");
	// printf("Naiwnie: %lf \n", ((end*N) - sum)/(end*N));
	// printf("Rekursywnie:  %lf \n",((end*N) - sum_1)/(end*N));
	// printf("Kahana: %lf \n",((end*N) - sum_2)/(end*N));
	// printf("Czas dla normalnego: %lf \n", (double) (end1 - start1)/CLOCKS_PER_SEC);
	// printf("Czas dla rekursywnego: %lf \n", (double) (end2 - start2)/CLOCKS_PER_SEC);
	// printf("Czas dla kahana: %lf \n", (double) (end3 - start3)/CLOCKS_PER_SEC);
    return 0;
}
