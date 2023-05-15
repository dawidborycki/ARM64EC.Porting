#pragma once

#include "Vectors.h"

int* generateRamp(int startValue, int len) {
    int* ramp = new int[len];

    for (int i = 0; i < len; i++) {
        ramp[i] = startValue + i;
    }

    return ramp;
}

double msElapsedTime(chrono::system_clock::time_point start) {
    auto end = chrono::system_clock::now();

    return chrono::duration_cast<chrono::milliseconds>(end - start).count();
}

double dotProduct(int* vector1, int* vector2, int len) {
    double result = 0;

    for (int i = 0; i < len; i++) {
        result += (double)vector1[i] * vector2[i];
    }

    return result;
}

double performCalculations() {
    // Ramp length and number of trials
    const int rampLength = 1024;
    const int trials = 100000;

    // Generate two input vectors
    // (0, 1, ..., rampLength - 1)
    // (100, 101, ..., 100 + rampLength-1)
    auto ramp1 = generateRamp(0, rampLength);
    auto ramp2 = generateRamp(100, rampLength);

    // Invoke dotProduct and measure performance    
    auto start = chrono::system_clock::now();

    for (int i = 0; i < trials; i++) {
        dotProduct(ramp1, ramp2, rampLength);
    }    

    return msElapsedTime(start);
}