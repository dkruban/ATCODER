#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isValidDigits(const string& str) {
    for (char const &c : str) {
        if (isdigit(c) == 0) return false;
    }
    return true;
}

int main() {
    string car_no;
    cout << "Enter the car no:";
    cin >> car_no;
    
    if (car_no.length() != 4 || !isValidDigits(car_no)) {
        cout << car_no << " is not a valid car number" << endl;
        return 0;
    }
    if (stoi(car_no) <= 0) {
        cout << car_no << " is not a valid car number" << endl;
        return 0;
    }
    int digit_sum = 0;
    for (char c : car_no) {
        digit_sum += (c - '0');
    }
    
    if (digit_sum % 3 == 0 || digit_sum % 5 == 0 || digit_sum % 7 == 0) {
        cout << "Lucky Number" << endl;
    } else {
        cout << "Sorry its not my lucky number" << endl;
    }
    
    return 0;
}
