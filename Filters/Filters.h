#pragma once
#define _USE_MATH_DEFINES

#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define SIGNAL_LENGTH 1024
#define SIGNAL_AMPLITUDE 100
#define NOISE_AMPLITUDE 50
#define THRESHOLD 70

// Global variables
double inputSignal[SIGNAL_LENGTH];
double inputSignalAfterFilter[SIGNAL_LENGTH];

// Exports
extern "C" __declspec(dllexport) int getSignalLength();

extern "C" __declspec(dllexport) void generateSignal();
extern "C" __declspec(dllexport) void truncate();

extern "C" __declspec(dllexport) double* getInputSignal();
extern "C" __declspec(dllexport) double* getInputSignalAfterFilter();