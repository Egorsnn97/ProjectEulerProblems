#include <iostream>
using namespace std;


int Problem_7() {
	int i = 2;
	int num = 3;
	while (i != 10001) {
		num+=2;
		for (int j = 2; j <= int(sqrt(num)) + 1; j++) {
			if (num % j == 0) {
				break;
			}
			else if (j == int(sqrt(num)) + 1) {
				i++;
			}
		}
	}
	return num;
}

int main() {
	
	cout << Problem_7() << endl;
	return 0;
}
//ANSWER: 104743
