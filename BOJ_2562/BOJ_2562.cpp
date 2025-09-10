#include <iostream>
using namespace std;

int x, y;
int arr[100];

int main(){
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		}
	y = arr[0];
	for (int i = 1; i < 9; i++){
		if (y < arr[i]){
			x = i;
			y = arr[i];
		}	
	}
	cout << y << endl;
	cout << x+1;
	return 0;
}