#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// helper
struct Vector2 {
    int x;
    int y;
};

vector<string> loadData() {
    ifstream file("../inputs/day10.txt");
    vector<string> rows;

    string text;
    while (getline(file, text)) {
        std::istringstream iss(text);
        rows.push_back(text);
    }

    return rows;
}

// getting next step coords
Vector2 getNextStep(vector<string> pipeMap, Vector2 currentPos) {
    Vector2 nextPos;

    switch (pipeMap[currentPos.x][currentPos.y]) {
        case '|':
            /* code */
            break;
        case '-':
            /* code */
            break;
        case 'J':
            /* code */
            break;
        case 'L':
            /* code */
            break;
        case '7':
            /* code */
            break;
        case 'F':
            /* code */
            break;
        case 'S':
            /* code */
            break;
        case '.':
            /* code */
            break;
    }

    return nextPos;
}

int solve(vector<string> pipeMap) {
    Vector2 startPos;

    // find starting point
    for (int row = 0; row < pipeMap.size(); row++) {
        for (int col = 0; col < pipeMap[row].length(); col++) {
            if (pipeMap[row][col] == 'S') {
                startPos.x = row;
                startPos.y = col;
            }
        }
    }

    // get valid directions
    vector<int> validDirections;
    int left = pipeMap[startPos.x - 1][startPos.y],
        right = pipeMap[startPos.x + 1][startPos.y],
        up = pipeMap[startPos.x][startPos.y - 1],
        down = pipeMap[startPos.x][startPos.y + 1];

    if (left == 'F' || left == 'L' || left == '-') {
        validDirections.push_back(left);
    }
    if (right == 'J' || right == '7' || right == '-') {
        validDirections.push_back(right);
    }
    if (up == '|' || up == 'F' || up == '7') {
        validDirections.push_back(up);
    }
    if (down == 'J' || down == 'L' || down == '|') {
        validDirections.push_back(down);
    }

    return 0;
}

int main() {
    vector<string> pipeMap = loadData();

    int solution = solve(pipeMap);

    return 0;
}
