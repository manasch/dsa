#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(2 * n);
    for (int i = 0; i < (2 * n); ++i) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    int mid1 = arr[n - 1];
    int mid2 = arr[n];
    /* cout << mid1 << " " << mid2 << endl; */
    /* for (int i: arr) { */
    /*   cout << i << " "; */
    /* } */
    cout << (mid2 - mid1) << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}

