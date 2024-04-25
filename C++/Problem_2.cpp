#include <iostream>
using namespace std;


int Problem_2() {
	int a = 1, b = 2,c,sum = 0;
	while (b < 4000000) {
		if (b % 2 == 0) {
			sum += b;
		}
		c = a;
		a = b;
		b += c;
	}
	return sum;
}

int main() {
	
	cout << Problem_2() << endl;

	return 0;
}
//ANSWER: 4613732
