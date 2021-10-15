# Intervals



* [x] LC [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
* [x] CSES: [Movie Festival](https://cses.fi/problemset/task/1629)
* [x] CSES: [Movei Festival II](https://cses.fi/problemset/task/1632) ✅
* [x] CSES: [Restaurant Customers](https://cses.fi/problemset/task/1619)

{% tabs %}
{% tab title="56" %}
```python
 def merge(self, A: List[List[int]]) -> List[List[int]]:
    A.sort()

    res = []
    start, end = A[0]
    for a in A[1:]:
        # 1. if intersection
        if start<=a[0]<=end:
            end = max(end,a[1])
        # 2. if disjointed
        else:
            res.append((start,end))
            start,end = a
    # for the last one
    res.append((start,end))
    return res
```
{% endtab %}

{% tab title="MovieFestival -II" %}
```cpp
int n, k; cin >> n >> k;
vector<pair<int, int>> v(n);
for (int i = 0; i < n; i++) // read start time, end time
	cin >> v[i].second >> v[i].first;
sort(begin(v), end(v)); // sort by end time

int ans = 0;
multiset<int> end_times; // times when members will finish watching movies
for (int i = 0; i < k; ++i)
	end_times.insert(0);

for (int i = 0; i < n; i++) {
	auto it = end_times.upper_bound(v[i].second);
	if (it == begin(end_times)) continue;
	// assign movie to be watched by member in multiset who finishes at time *prev(it)
	end_times.erase(--it);
	// member now finishes watching at time v[i].first
	end_times.insert(v[i].first);
	++ ans;
}
```
{% endtab %}
{% endtabs %}

