#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


void check(int currentCycle, int currentPosition, int X) {
    if (X == currentPosition || X - 1 == currentPosition || X + 1 == currentPosition) {
        cout << "#";
      }
    else {
        cout << ".";
      }
}

int main() {
  char delim = '\n';

  string line;
  fstream fin;
  int X = 1;
  int currentCycle = 0;
  int currentPosition = 0;
  fin.open("./data.txt");

  while (getline(fin, line, delim)) {
    if (line[0] == 'n') {
      currentCycle++;
      check(currentCycle, currentPosition, X);
      currentPosition++;
      if ((currentCycle) % 40 == 0) {
        cout << endl;
        currentPosition = 0;
      }
    }
    else {
      currentCycle ++;
      check(currentCycle, currentPosition, X);
      currentPosition++;
      if ((currentCycle) % 40 == 0) {
        cout << endl;
        currentPosition = 0;
      }
        currentCycle++;
        check(currentCycle, currentPosition, X);
        currentPosition++;
        if ((currentCycle) % 40 == 0) {
          cout << endl;
        currentPosition = 0;
        }
          X += stoi(line.substr(5));
    }
  }
}

