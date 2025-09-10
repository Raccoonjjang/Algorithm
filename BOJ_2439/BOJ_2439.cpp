#include <iostream>
using namespace std;

int main()
{
    int N;
    int a = 0;
    cin >> N;
    for(int i=1; i<N+1; i++){
        for(int b=i; b<N; b++){
            cout << " ";
        }
        while(a<i){
            cout << "*";
            a++;
        }
        a = 0;
        cout << "\n";
    }
    return 0;
}
