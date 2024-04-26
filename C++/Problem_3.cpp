#include <iostream>
using namespace std;


int Task_6() {
	int sumSqu = 0,sum = 0;
	for (int i = 1; i <= 100; i++) {
		sumSqu += i * i;
		sum += i;
	}
	return sum * sum - sumSqu;
}

int main() {
	
	cout << Task_6() << endl;

	return 0;
}
//25164150
//25502500-338350=25164150
