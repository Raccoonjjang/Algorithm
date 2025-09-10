#include <iostream>

using namespace std;

int main() {
	int a, b, c;
	cin >> a;
	b = 1;
	c = 0;
	while (b < 10) {
		c = a * b;
		cout << a << " * " << b << " = " << c << endl;
		++b;
	}
}