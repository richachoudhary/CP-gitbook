# DP on Graph



* [x] CSES: [Forest Queries](https://cses.fi/problemset/result/2670872/) | **`classic`**
* [ ] [https://leetcode.com/problems/cheapest-flights-within-k-stops/](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
* [ ] [https://leetcode.com/problems/find-the-shortest-superstring/](https://leetcode.com/problems/find-the-shortest-superstring/)
* [x] [1340. Jump Game V](https://leetcode.com/problems/jump-game-v/) ✅
*   [x] [1533.Minimum Number of Days to Eat N Oranges](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/) ✅💪| DP or BFS



{% tabs %}
{% tab title="ForestQueries" %}
```python
I = lambda : map(int, input().split())
n,q = I()
graph = [[0]*(n+1)]

for _ in range(n):
    s = str(input())
    graph.append([0] + [c for c in s])

DP = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        DP[i][j] = 1 if graph[i][j] == '*' else 0
        DP[i][j] = DP[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

for _ in range(q):
    x1,y1,x2,y2 = I()
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])

```
{% endtab %}

{% tab title="1340" %}
```python
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def jumps(start: int) -> int:
            height = arr[start]
            max_jumps = 0
            
            for index in range(start - 1, max(0, start - d) - 1, -1):
                if arr[index] >= height:
                    break
                
                max_jumps = max(max_jumps, jumps(index))
            
            for index in range(start + 1, min(n, start + d + 1)):
                if arr[index] >= height:
                    break
                
                max_jumps = max(max_jumps, jumps(index))
            
            return max_jumps + 1
        
        return max(jumps(start) for start in range(n))
```
{% endtab %}

{% tab title="1533" %}
```python
from collections import deque
def minDays(self, n: int) -> int:
    #1. DP ===================================================
    MEMO = {}
    def dp(n):
        if n <= 1:
            return n
        
        if n in MEMO: return MEMO[n]
        
        op1 = n%2 + dp(n//2)
        op2 = n%3 + dp(n//3)
        
        MEMO[n] = 1 + min(op1,op2)
        return MEMO[n]

    return dp(n)
    
    #So, the choice we have is to 
    #      1. eat n % 2 oranges one-by-one and then swallow n / 2, 
    #      2. or eat n % 3 oranges so that we can gobble 2 * n / 3

    # BFS ========================================================
    
    def bfs(n):
        Q = deque()
        vis = set()
        Q.append((n,0))
        
        while Q:
            # implement for this level
            for _ in range(len(Q)):
                x,move = Q.popleft()
                if x == 0:
                    return move
                if (x-1) not in vis:
                    Q.append((x-1,move+1))
                    vis.add(x-1)
                if x%2 == 0 and x//2 not in vis:
                    Q.append((x//2,move+1))
                    vis.add(x//2)
                if x%3 == 0 and x//3 not in vis:
                    Q.append((x//3,move+1))
                    vis.add(x//3)

    return bfs(n)
```
{% endtab %}
{% endtabs %}

