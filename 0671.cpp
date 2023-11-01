#include <iostream>
#include <vector>
#include <cmath>

int z;					// длина строки/числа
std::string str;		// входящая строка числа
long long int s = 0;	// сумма чисел из 4 и 7
std::vector<int> arr;	// цифры числа

// рекурсия
long long int rec(int pos, bool same) {
	if (!same)
		return (pow(2, (z - pos)));
	if (z == pos)
		return 1;
	long long int t = 0;
	if (4 < arr[pos])
		t += rec(pos + 1, 0);
	if (7 < arr[pos])
		t += rec(pos + 1, 0);
	if (4 == arr[pos] || 7 == arr[pos])
		t += rec(pos + 1, 1);
	return t;
}

int main() {
	std::cin >> str;
	z = size(str);

	for (char const& c : str)
		arr.push_back(c-'0');

	for (int i = 1; i < z; i++)
		s += pow(2, i);

	s += rec(0, 1);

	std::cout << s;
}