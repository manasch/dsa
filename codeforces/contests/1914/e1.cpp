#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* void solve() { */
/*   ll n; */
/*   cin >> n; */
/*   vector<ll> a(n), b(n); */
/**/
/*   for (ll i = 0; i < n; ++i) { */
/*     cin >> a[i]; */
/*   } */
/*   for (ll i = 0; i < n; ++i) { */
/*     cin >> b[i]; */
/*   } */
/**/
/*   for (ll i = 0; i < n; ++i) { */
/*     ll idx = -1; */
/*     ll maxVal = INT_MIN; */
/*     for (ll j = 0; j < n; ++j) { */
/*       if ((i & 1) == 1) { */
/*         if (b[j] > 0 && a[j] > maxVal) { */
/*           maxVal = a[j]; */
/*           idx = j; */
/*         } */
/*         else if (a[j] == maxVal) { */
/*           if (idx != -1) { */
/*             if (b[j] > b[idx]) { */
/*               idx = j; */
/*             } */
/*           } */
/*           else { */
/*             idx = j; */
/*           } */
/*         } */
/*       } */
/*       else { */
/*         if (a[j] > 0 && b[j] > maxVal) { */
/*           maxVal = b[j]; */
/*           idx = j; */
/*         } */
/*         else if (b[j] == maxVal) { */
/*           if (idx != -1) { */
/*             if (a[j] > a[idx]) { */
/*               idx = j; */
/*             } */
/*           } */
/*           else { */
/*             idx = j; */
/*           } */
/*         } */
/*       } */
/*     } */
/*     if ((i & 1) == 1) { */
/*       --b[idx]; */
/*       a[idx] = 0; */
/*     } */
/*     else { */
/*       --a[idx]; */
/*       b[idx] = 0; */
/*     } */
/*     cout << idx << endl; */
/*     for (ll i = 0; i < n; ++i) { */
/*       cout << a[i] << " "; */
/*     } */
/*     cout << endl; */
/*     for (ll i = 0; i < n; ++i) { */
/*       cout << b[i] << " "; */
/*     } */
/*     cout << endl; */
/*   } */
  /* for (ll i = 0; i < n; ++i) { */
  /*   cout << a[i] << " "; */
  /* } */
  /* cout << endl; */
  /* for (ll i = 0; i < n; ++i) { */
  /*   cout << b[i] << " "; */
  /* } */
  /* cout << endl; */
  /**/
/*   ll aSum = accumulate(a.begin(), a.end(), 0); */
/*   ll bSum = accumulate(b.begin(), b.end(), 0); */
/*   cout << aSum << " " << bSum << endl; */
/*   cout << aSum - bSum << endl; */
/* } */

void solve() {
  ll n;
  cin >> n;
  vector<ll> a(n), b(n);
  vector<pair<ll, ll>> idxPair;

  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> b[i];
  }
  for (int i = 0; i < n; ++i) {
    idxPair.push_back({a[i] + b[i], i});
  }

  sort(idxPair.begin(), idxPair.end(), greater<>());

  int j;
  for (int i = 0; i < n; ++i) {
    j = idxPair[i].second;
    if ((i & 1) == 0) {
      a[j] -= 1;
      b[j] = 0;
    }
    else {
      b[j] -= 1;
      a[j] = 0;
    }
  }

  ll aSum = 0, bSum = 0;
  for (int i = 0; i < n; ++i) {
    aSum += a[i];
    bSum += b[i];
  }

  cout << aSum - bSum << endl;
}

int main() {
  ll t;
  cin >> t;
  while (t--) {
    solve();
  }
}

