#include <iostream>
using namespace std;

int main() {
	int N;
	int c=0;
	cin >> N;
	for (int i=0; i < N; i++) {
		while (c < i+1) {
			cout << "*";
			c++;
		}
		c = 0;
		cout << "\n";
	}
}