#include <iostream>
using namespace std;


int Task_3() {
	const long long NUMBER = 600851475143;
	int m = 1;
	for (int i = 3; i <= int(sqrt(NUMBER)) + 1;i+=2) {
		if (NUMBER % i == 0) {
			
			for (int j = 3; j <= int(sqrt(i)) + 1; j++) {
				if (i % j == 0) {
					break;
				}
				else if (j == int(sqrt(i)) + 1) {
					m = i;
					
				}
			}
		}
		
	}
	return m;
}

int main() {
	
	cout << Task_3() << endl;
	return 0;
}
//ANSWER: 6857
