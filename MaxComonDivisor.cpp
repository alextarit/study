#include <iostream>

using namespace std;

template <class Int>
Int gcd(Int a, Int b) {
  while (a != b){
      if (a > b){
          a -= b;
      }else {
          b -= a;
      }
  }
  return a;
}

int main(void) {
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;
    return 0;
}