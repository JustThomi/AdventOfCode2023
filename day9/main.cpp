#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

// moved from python to cpp, realized I don't enjoy working with python rn
//
// using namespace for convenience
using namespace std;

vector<vector<int>> loadData() {
    ifstream file("input.txt");
    vector<vector<int>> values;

    string text;
    while (getline(file, text)) {
        std::istringstream iss(text);
        vector<int> temp;
        int value;

        // Extract key and value from each line
        while (iss >> value) {
            temp.push_back(value);
        }
        values.push_back(temp);
    }

    return values;
}

int findNextValue(vector<int> numbers) {
    vector<vector<int>> stepList;
    vector<int> currentSteps = numbers;
    vector<int> steps;
    bool status = false;

    // add initial numbers
    stepList.push_back(currentSteps);

    do {
        steps.clear();
        for (int i = 0; i < currentSteps.size() - 1; i++) {
            steps.push_back(currentSteps[i + 1] - currentSteps[i]);
        }

        stepList.push_back(steps);
        currentSteps.assign(steps.begin(), steps.end());

        // check if all back to 0
        status = std::all_of(steps.begin(), steps.end(),
                             [](int value) { return value == 0; });

    } while (!status);

    // get next value
    int nextValue = 0;
    for (auto step : stepList) {
        nextValue += step.back();
    }

    return nextValue;
}

int findPrewValue(vector<int> numbers) {
    vector<vector<int>> stepList;
    vector<int> currentSteps = numbers;
    vector<int> steps;
    bool status = false;

    do {
        steps.clear();
        for (int i = 0; i < currentSteps.size() - 1; i++) {
            steps.push_back(currentSteps[i + 1] - currentSteps[i]);
        }

        currentSteps.assign(steps.begin(), steps.end());
        reverse(steps.begin(), steps.end());
        stepList.push_back(steps);

        // check if all back to 0
        status = std::all_of(steps.begin(), steps.end(),
                             [](int value) { return value == 0; });

    } while (!status);
    reverse(stepList.begin(), stepList.end());

    // get last value
    int nextValue = 0;
    for (auto step : stepList) {
        nextValue = step.back() - nextValue;
    }

    return nextValue;
}

int main() {
    vector<vector<int>> values = loadData();

    int sum = 0;

    for (auto& list : values) {
        sum += findPrewValue(list);
    }
    cout << sum << endl;

    return 0;
}
