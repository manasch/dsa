#include <bits/stdc++.h>
using namespace std;

// 1 -3 7 -6 2 5

int solve(vector<int>& arr) {
    int cypriot = INT_MIN;
    auto dfs = [&] (auto self, int idx, int sum, int i) {
        if (i >= arr.size()) {
            return 0;
        }
        // extend the subarray
        int extend = self(self, idx, sum + arr[i], i + 1);

        // start new subarray
        int newSub = self(self, idx + 1, 0, i + 1);

        int current = idx * sum;
    };

    dfs(dfs, 1, 0, 0);
}

int main() {
    int t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        cout << solve(arr) << endl;
    }
}
