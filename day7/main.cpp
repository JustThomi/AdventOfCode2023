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

map<string, int> mapValues() {
    ifstream file("input.txt");
    string text;
    map<string, int> values;

    while (getline(file, text)) {
        std::istringstream iss(text);
        std::string key;
        int value;

        // Extract key and value from each line
        if (iss >> key >> value) {
            values[key] = value;
        } else {
            std::cerr << "Error parsing line: " << text << std::endl;
        }
    }

    return values;
}

void getHandStrenght(string hand) {}

int solve(map<string, int> games) {
    for (const auto& pair : games) {
        std::cout << "key: \"" << pair.first << "\", value: " << pair.second
                  << std::endl;
    }
}

int main() {
    map<string, int> games = mapValues();
    int solution = solve(games);

    cout << solution << endl;
    return 0;
}
