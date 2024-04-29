#include <iostream>
using namespace std;

int Problem_5() {
	int min = NULL;
	int i = 20;
	while (min == NULL) {
		for (int j = 3; j < 20; j++) {
			if (i % j != 0) {
				break;
			}
			else if (j == 19) {
				return i;
			}
		}
		i += 20;
	}
}

int main() {
	
	cout << Problem_5() << endl;
	return 0;
}
//ANSWER: 232792560
