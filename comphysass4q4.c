
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define NUM_SAMPLES 10000 

// Transformation Method 
double generate_exponential(double mean) 
{
    double u = (double)rand() / RAND_MAX;
    return -log(u) * mean;
}

int main() 
{
    double samples[NUM_SAMPLES];
    double mean = 0.5; 
    srand((unsigned)time(NULL)); 

    for (int i = 0; i < NUM_SAMPLES; i++) 
    {
        samples[i] = generate_exponential(mean); 
    }

    FILE *file = fopen("exponential_samples.txt", "w");
    for (int i = 0; i < NUM_SAMPLES; i++) 
    {
        fprintf(file, "%f\n", samples[i]);
    }
    fclose(file);
    return 0;
}
