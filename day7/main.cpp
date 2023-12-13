#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

// moved from python to cpp, realized I don't enjoy working with python rn
// soooo convoluted lol
//
// using namespace for convenience
using namespace std;

class Game {
   public:
    Game(string hand, int bet, map<char, int> values) {
        this->hand = hand;
        this->bet = bet;
        // part 1
        // setHandStrenght();
        // part 2
        setHandStrenghtJoker();
        setCardValues(values);
    }

    ~Game();

    void setHandStrenghtJoker() {
        map<char, int> countMap;
        vector<int> nrOfCards;
        int totalJokers = 0;

        // initi map
        for (char c : this->hand) {
            if (c != 'J') countMap[c] = 0;
        }
        // count cards and J's
        for (char c : this->hand) {
            if (c == 'J')
                totalJokers++;
            else
                countMap[c]++;
        }

        // exctranct items for convenience
        for (auto item : countMap) {
            nrOfCards.push_back(item.second);
        }

        // add nr of jokers to highest nr of cards
        int maxNr = 0;
        for (int i = 0; i < nrOfCards.size(); i++) {
            if (nrOfCards[i] > nrOfCards[maxNr]) {
                maxNr = i;
            }
        }
        // cout << "Nr: " << maxNr << "Size: " << nrOfCards.size() << endl;
        // cout << nrOfCards[maxNr] << endl;

        if (nrOfCards.size() > 0)
            nrOfCards[maxNr] += totalJokers;
        else
            nrOfCards.push_back(totalJokers);

        // assume it's high card from the start
        int value = 0;

        // 5 of a kind
        if (find(nrOfCards.begin(), nrOfCards.end(), 5) != nrOfCards.end()) {
            value = 50;
        }
        // 4 of a kind
        else if (find(nrOfCards.begin(), nrOfCards.end(), 4) !=
                 nrOfCards.end()) {
            value = 40;
        }
        // 3 of a kind
        else if (find(nrOfCards.begin(), nrOfCards.end(), 3) !=
                 nrOfCards.end()) {
            // full house
            if (find(nrOfCards.begin(), nrOfCards.end(), 2) !=
                nrOfCards.end()) {
                value = 35;
            } else {
                value = 30;
            }
        } else {
            // count 2s
            int countTwo = 0;
            for (int nr : nrOfCards) {
                if (nr == 2) {
                    countTwo++;
                }
            }

            // 2 pairds
            if (countTwo == 2) {
                value = 20;
            }
            // 1 pair
            else if (countTwo == 1) {
                value = 10;
            }
        }

        this->strenght = value;
    }

    void setHandStrenght() {
        map<char, int> countMap;
        vector<int> nrOfCards;
        // initi map
        for (char c : this->hand) {
            countMap[c] = 0;
        }
        // count cards
        for (char c : this->hand) {
            countMap[c]++;
        }
        // exctranct items for convenience
        for (auto item : countMap) {
            nrOfCards.push_back(item.second);
        }

        // assume it's high card from the start
        int value = 0;

        // 5 of a kind
        if (find(nrOfCards.begin(), nrOfCards.end(), 5) != nrOfCards.end()) {
            value = 50;
        }
        // 4 of a kind
        else if (find(nrOfCards.begin(), nrOfCards.end(), 4) !=
                 nrOfCards.end()) {
            value = 40;
        }
        // 3 of a kind
        else if (find(nrOfCards.begin(), nrOfCards.end(), 3) !=
                 nrOfCards.end()) {
            // full house
            if (find(nrOfCards.begin(), nrOfCards.end(), 2) !=
                nrOfCards.end()) {
                value = 35;
            } else {
                value = 30;
            }
        } else {
            // count 2s
            int countTwo = 0;
            for (int nr : nrOfCards) {
                if (nr == 2) {
                    countTwo++;
                }
            }

            // 2 pairds
            if (countTwo == 2) {
                value = 20;
            }
            // 1 pair
            else if (countTwo == 1) {
                value = 10;
            }
        }

        this->strenght = value;
    }

    void setCardValues(map<char, int> values) {
        for (char c : hand) {
            if (values.find(c) == values.end()) {
                int conv = c - '0';
                this->cardValues.push_back(conv);
            } else {
                this->cardValues.push_back(values[c]);
            }
        }
    }

    vector<int> getCardValues() { return cardValues; }

    int getBet() { return bet; }

    string getHand() { return hand; }

    int getStrenght() { return strenght; }

   private:
    vector<int> cardValues;
    string hand;
    int bet;
    int strenght;
};

ostream& operator<<(ostream& os, Game& g) {
    os << g.getHand() << '/' << g.getBet() << '/' << g.getStrenght();
    return os;
}

bool sortByHand(Game* game1, Game* game2) {
    return game1->getCardValues() < game2->getCardValues();
}

vector<Game*> mapValues(map<char, int> values) {
    ifstream file("../inputs/day7.txt");
    string text;
    vector<Game*> games;

    while (getline(file, text)) {
        istringstream iss(text);
        string hand;
        int bet;
        Game* g;

        // Extract key and value from each line
        if (iss >> hand >> bet) {
            g = new Game(hand, bet, values);
            games.push_back(g);
        } else {
            cerr << "Error parsing line: " << text << endl;
        }
    }

    file.close();
    return games;
}

int solve(vector<Game*> games) {
    // separate types by strenght
    vector<Game*> fiveOfAKind;
    vector<Game*> fourOfAKind;
    vector<Game*> fullHouse;
    vector<Game*> threeOfAKinds;
    vector<Game*> twoPairs;
    vector<Game*> onePair;
    vector<Game*> highCard;

    for (Game* g : games) {
        switch (g->getStrenght()) {
            case 50:
                fiveOfAKind.push_back(g);
                break;
            case 40:
                fourOfAKind.push_back(g);
                break;
            case 35:
                fullHouse.push_back(g);
                break;
            case 30:
                threeOfAKinds.push_back(g);
                break;
            case 20:
                twoPairs.push_back(g);
                break;
            case 10:
                onePair.push_back(g);
                break;
            case 0:
                highCard.push_back(g);
                break;
        }
    }

    // sort them all
    sort(begin(highCard), end(highCard),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });

    sort(begin(onePair), end(onePair),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });
    sort(begin(twoPairs), end(twoPairs),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });
    sort(begin(threeOfAKinds), end(threeOfAKinds),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });
    sort(begin(fullHouse), end(fullHouse),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });
    sort(begin(fourOfAKind), end(fourOfAKind),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });
    sort(begin(fiveOfAKind), end(fiveOfAKind),
         [](Game* game1, Game* game2) { return sortByHand(game1, game2); });

    // get results
    int solution = 0, currentRank = 1;

    for (auto g : highCard) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : onePair) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : twoPairs) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : threeOfAKinds) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : fullHouse) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : fourOfAKind) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }
    for (auto g : fiveOfAKind) {
        solution += g->getBet() * currentRank;
        currentRank++;
    }

    // printHighCards
    for (auto g : highCard) {
        cout << g->getHand() << endl;
    }

    return solution;
}

int main() {
    map<char, int> cardValues = {
        {'A', 14},
        {'K', 13},
        {'Q', 12},
        {'T', 10},
        // value set to 1 for part 2
        {'J', 1},
    };

    vector<Game*> games = mapValues(cardValues);
    int solution = solve(games);
    cout << solution << endl;

    // // print values for testing
    // for(auto g : games){
    //     cout << *g << endl;
    // }
    return 0;
}
