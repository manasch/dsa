#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
            if (i > 0) {
                if (arr[i] < arr[i - 1]) {
                    flag = false;
                }
            }
        }
        if (flag || k > 1) {
            cout << "yes" << endl;
        }
        else {
            cout << "no" << endl;
        }
    }
}
