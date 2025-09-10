#include <iostream>
using namespace std;

int main() {
	int A, B, C;
	cin >> A >> B;
	cin >> C;
	if (A >= 0 && A <= 23) {
		if (B >= 0 && B <= 59) {
			if (C >= 0 && C <= 1000) {
				B = B + C;
				for (B; B > 59;){
					A = A + 1;
					B = B - 60;
				}
				if (A >= 24) {
					A = A - 24;
				}
				cout << A << " " << B << endl;
			}
			else {
				cout << "정수값 벗어남" << endl;
			}
		}
		else{
			cout << "정수값 벗어남" << endl;
		}
	}
	else {
		cout << "정수값 벗어남" << endl;
	}
}