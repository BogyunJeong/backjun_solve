// 택배상자.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, int w, int num) {
	vector < vector<int>> box;
	
	int cnt = 1;
	int row = 0;

	while (cnt <= n) {
		vector<int> row_box; // 한 줄의 박스
		for (int i = 0; i < w && cnt <= n; i++) {
			row_box.push_back(cnt);
			cnt++;
		}

		while (row_box.size() < w) { // 만약 박스가 다 안채워졌으면 0으로 채우기
			row_box.push_back(0);
		}

		if (row % 2 == 1) { 
			reverse(row_box.begin(), row_box.end());
		}
		box.push_back(row_box);
		row++;
	}
	int answer = 0;
	int r = 0;
	int c = 0;
	bool found = false;

	for (int i = 0; i < box.size(); i++) {
		for (int j = 0; j < box[i].size(); j++) {
			if (box[i][j] == num) {
				r = i;
				c = j;
				found = true;
				break;
			}
		}
			if (found == true) break;
	}

	for (int i = r; i < box.size(); i++) {
		if (box[i][c] != 0) {
			answer++;
		}
	}

	cout << answer;
	return 0;
}

int main() {
	solution(22, 6, 8);
	return 0;
}

