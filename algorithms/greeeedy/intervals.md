# Intervals

* [x] LC [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
* [x] LC [57. Insert Interval](https://leetcode.com/problems/insert-interval/) 🌟| **must\_do**
* [x] LC [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/)
* [x] CSES: [Movie Festival](https://cses.fi/problemset/task/1629)
* [x] CSES: [Movei Festival II](https://cses.fi/problemset/task/1632) ✅
* [x] CSES: [Restaurant Customers](https://cses.fi/problemset/task/1619)
* [x] LC [715. Range Module](https://leetcode.com/problems/range-module/) | \<hard>
* [x] LC [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | **@Microsoft**

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

{% tab title="57" %}
```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # 1. Extension of "Merge Intervals" ========================== TC: O(NlogN)

    intervals.append(newInterval)
    intervals.sort()

    res = []
    start,end = intervals[0][0],intervals[0][1]

    for interval in intervals[1:]:
        if start<= interval[0] <= end:
            end = max(end,interval[1])
        else:
            res.append([start,end])
            start,end = interval
    # for the last one
    res.append([start,end])
    return res

    # 2. In-Place : using already-sorted property================== TC: O(N)
    res = []

    for i, interval in enumerate(intervals):
         # non-overlapping - caseI
        if interval[1] < newInterval[0]:   
            res.append(interval)
        # non-overlapping - caseII
        elif interval[0] > newInterval[1]:  
            res.append(newInterval) 
            # early return
            return res + intervals[i:]
        # overlapping case
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
    # if we couldn't accomodate newInterval till the end
    res.append(newInterval)
    return res
```
{% endtab %}

{% tab title="228" %}
```python
def summaryRanges(self, A: List[int]) -> List[str]:
    ans = []
    if len(A) == 0:
        return ans
    start,end = A[0],A[0]

    for a in A[1:]:
        #continue prev range
        if a == end+1:
            end = a
        # start new range
        else:
            if start != end:
                ans.append(str(start)+'->'+str(end))
            else:
                ans.append(str(start))
            start, end = a,a

    # for the last
    if start != end:
        ans.append(str(start)+'->'+str(end))
    else:
        ans.append(str(start))
        return ans
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

{% tab title="715" %}
```python
class RangeModule:

    def __init__(self):
        self.X = [0, 10**9]
        self.track = [False] * 2

    def addRange(self, left, right, track=True):
        def index(x):
            i = bisect.bisect_left(self.X, x)
            if self.X[i] != x:
                self.X.insert(i, x)
                self.track.insert(i, self.track[i-1])
            return i
        i = index(left)
        j = index(right)
        self.X[i:j] = [left]
        self.track[i:j] = [track]

    def queryRange(self, left, right):
        i = bisect.bisect(self.X, left) - 1
        j = bisect.bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left, right):
        self.addRange(left, right, False)
```
{% endtab %}

{% tab title="Untitled" %}


Intuition:

1. similar to the closing openning backet problems, where there's nesting, stack is required
2. nested function time need to be deducted from the parent time, therefore update the parent function with negative children's time
3. Each time a function finishes, the time span needs to be added to the function slot in the outputs array

```python
def exclusiveTime(self, n, logs):
    
    outputs = [0]*n
    stack = [] # holds f_id, time stamp
    
    for s in logs:
        tokens = s.split(":")
        f_id, state, time = int(tokens[0]), tokens[1], int(tokens[2])
        if state == "start":
            stack.append((f_id, time))
        else:
            f_id_end, time_start = stack.pop()
            time_diff = time - time_start + 1
            outputs[f_id_end] += time_diff
            if len(stack) > 0:
                # deduct from previous fn time 
                outputs[stack[-1][0]] += -time_diff
    return outputs 
```
{% endtab %}
{% endtabs %}
