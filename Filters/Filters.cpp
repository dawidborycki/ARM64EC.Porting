#include "Filters.h"

void generateSignal() {
    auto phaseStep = 2 * M_PI / SIGNAL_LENGTH;

    for (int i = 0; i < SIGNAL_LENGTH; i++) {
        auto phase = i * phaseStep;
        auto noise = rand() % NOISE_AMPLITUDE;

        inputSignal[i] = SIGNAL_AMPLITUDE * sin(phase) + noise;
    }
}

void truncate() {
    for (int i = 0; i < SIGNAL_LENGTH; i++) {
        inputSignalAfterFilter[i] = min(inputSignal[i], (double)THRESHOLD);
    }
}

double* getInputSignal() {
    return inputSignal;
}

double* getInputSignalAfterFilter() {
    return inputSignalAfterFilter;
}

int getSignalLength() {
    return SIGNAL_LENGTH;
}
