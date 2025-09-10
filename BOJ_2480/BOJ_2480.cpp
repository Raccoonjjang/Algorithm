#include <iostream>

using namespace std;

int main() {
	int A, B, C;
	int D;
	cin >> A >> B >> C;
	if (A == B && B == C) {
		D = 10000 + A * 1000;
	}
	else if (A == B || A == C) {
		D = 1000 + A * 100;
	}
	else if (B == C) {
		D = 1000 + B * 100;
	}
	else {
		if (A > B && A > C) {
			D = A * 100;
		}
		else if (B > A && B > C) {
			D = B * 100;
		}
		else {
			D = C * 100;
		}
	}
	cout << D << endl;
}