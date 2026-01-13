#include <bits/stdc++.h>

using namespace std;

const int N = 200010;
long long cost[N];
vector<int> adj[N];
int n, q;
long long ans[N][2];




void dfs1(int u, int p, int depth) {
    
    if (depth >= 1) {
        ans[u][0] = cost[u];
    } else {
        ans[u][0] = LLONG_MIN; 
    }

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs1(v, u, depth + 1);

        if (depth >= 1 && ans[v][0] > 0) {
            ans[u][1] = max(ans[u][1], ans[v][0] + cost[u]);
        }
    }
}

void solve_query(int v, int x) {
    if (x == 1) {
        cout << cost[v] << '\n';
        return;
    }

    long long best = cost[v];

    
    
    function<void(int,int,int,long long)> dfs_path = [&](int u, int p, int steps, long long sum) {
        if (steps > x) return;
        best = max(best, sum);
        if (steps == x) return;
        for (int nei : adj[u]) {
            if (nei == p) continue;
            dfs_path(nei, u, steps + 1, sum + cost[nei]);
        }
    };

    dfs_path(v, -1, 1, cost[v]);
    cout << best << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; i++) {
        cin >> cost[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cin >> q;
    for (int i = 0; i < q; i++) {
        int v, x;
        cin >> v >> x;
        solve_query(v, x);
    }

    return 0;
}
