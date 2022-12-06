#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main() {
  string line;
  ifstream data ("data.txt");
  int sum = 0;

  if (data.is_open())
  {
    while (getline(data,line)) 
    {
      set<char> s;
      cout << line << "\n";
      string one = line.substr(0, line.length()/2);
      string two = line.substr(line.length()/2);
      for (int i = 0; i < one.length(); i++) {
        for (int j = 0; j < two.length(); j++) {
          if (one[i] == two[j]) {
            cout << one[i] << "\n";
            s.insert(one[i]);
            
          }
        }
      }
      for (auto& str: s)
      {
        cout << str << "\n";
      }

    }

    data.close();
  }
  else cout << "Unable to open file";
  cout << "Sum: " << sum;


  return 0;
}

