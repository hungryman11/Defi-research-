#include <iostream>
using namespace std;

int main() {
    double price = 2000.0;  // example ETH price
    double threshold = 2100.0;

    if (price < threshold) {
        cout << "Buying ETH at $" << price << endl;
    } else {
        cout << "Holding position." << endl;
    }
    return 0;
}
