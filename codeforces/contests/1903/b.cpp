#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        int temp;
        cin >> n;
        if (n == 1) {
            cin >> temp;
            cout << 1 << endl;
            continue;
        }
        vector<int> res;
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            int num = -1;
            int z = 0;
            for (int j = 0; j < n; ++j) {
                // cout << i << " test " << j << endl;
                cin >> temp;
                if (i == j) {
                    continue;
                }
                z |= temp;
                if (temp == 0) {
                    flag = false;
                }
                if (num == -1) {
                    num = temp;
                }
                else {
                    num &= temp;
                }
            }
            if (z == 0) {
                flag = true;
            }
            res.push_back(num);
        }
        if (flag) {
            cout << "yes" << endl;
            for (int i = 0; i < n; ++i) {
                cout << res[i] << " ";
            }
        }
        else {
            cout << "no" << endl;
        }
    }
}
