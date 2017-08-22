#include <cstdio>
#include <algorithm>
#include <cstring>
#define MAX_N 130000
using namespace std;
char str[MAX_N];
int t, n, g[MAX_N], tg[MAX_N], SA[MAX_N], r[MAX_N], LCP[MAX_N], idx, AAAA[MAX_N];
bool cmp(int x, int y) {
    if (g[x] == g[y]) {
        return g[x + t] < g[y + t];
    }
    return g[x] < g[y];
}
int main() {
    gets(str);
    n = strlen(str) - 4;
    str[n - 1] = 0;
    t = 1;
    for (int i = 0; i < n; i++) {
        SA[i] = i;
        g[i] = str[i];
    }
    while (t <= n) {
        g[n] = -1;
        sort(SA, SA + n, cmp);
        tg[SA[0]] = 0;
        for (int i = 1; i < n; i++) {
            if (cmp(SA[i - 1], SA[i]))
                tg[SA[i]] = tg[SA[i - 1]] + 1;
            else
                tg[SA[i]] = tg[SA[i - 1]];
        }
        for (int i = 0; i < n; i++)
            g[i] = tg[i];
        t <<= 1;
    }
    for (int i = 0; i < n; i++)
        r[SA[i]] = i;
    int len = 0;
    for (int i = 0; i < n; i++) {
        int k = r[i];
        if (k) {
            int j = SA[k - 1];
            while (str[j + len] == str[i + len])
                len++;
            LCP[k] = len;
            AAAA[k] = j;
            if (len)
                len--;
        }
    }
    int ans = 0;

    for (int i = 0; i < n; i++) {
        if (LCP[i] > ans)  {
            ans = LCP[i];
            idx = i;
        }
    }
    for (int i = 0; i < ans; i++)
        printf("%c", str[AAAA[idx] + i]);

    return 0;
}
