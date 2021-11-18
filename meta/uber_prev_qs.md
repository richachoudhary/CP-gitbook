# Uber\_prev\_Qs

## 1. DSA

* [x] [332.Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
* [x] [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
* [x] [2054. Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events/)
  * [x] [2008. Maximum Earnings From Taxi](https://leetcode.com/problems/maximum-earnings-from-taxi/)
* [x] SSLP Problem: (NP Hard though, but doable as: (1) multiply edges with -1 , (2) use topo to give ans in `O(E+V)`
* [x] [79. Word Search](https://leetcode.com/problems/word-search/) & [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
* [x] [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
* [x] [1928. Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)
* [x] [581. Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
* [x] [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)
* [x] **LC **[**986. **Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)&#x20;
* [x] LC [750. Number Of Corner Rectangles](https://sugarac.gitbooks.io/facebook-interview-handbook/content/number-of-corner-rectangles.html)
* [x] [979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

{% tabs %}
{% tab title="1235" %}
```python
# 1.Brute Force DP --------------------------- TC: O(N^2), SC: O(N) 
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))

    @lru_cache(None)
    def dp(i):
        if i == n: return 0
        ans = dp(i + 1)  # Choice 1: Don't pick

        for j in range(i + 1, n + 1):
            if j == n or jobs[j][0] >= jobs[i][1]:
                ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
                break

        return ans

    return dp(0)

    # 2. DP + Binary serach ---------------------------- TC: O(NlogN), SC: O(N)
    '''
    Since our jobs is already sorted in increasing order by startTime.
    So we can binary search to find the job next j, so that job[j].startTime >= job[i].endTime.

    '''
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))

    @lru_cache(None)
    def dp(i):
        if i == n: return 0
        ans = dp(i + 1)  # Choice 1: Don't pick

        j = bisect_left(startTime, jobs[i][1])
        ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
        return ans

    return dp(0)
```
{% endtab %}

{% tab title="2054" %}
```python
def maxTwoEvents(self, events: List[List[int]]) -> int:
    # 1. DP ================================================= [TLE]
    DP = {}
    def solve(events,k,i, last_end):
        if k <= 0 or i > len(events)-1:
            return 0

        if (k,i,last_end) in DP:
            return DP[(k,i,last_end)]

        #op1: pick if you can
        #op2: dont pick
        op1, op2 = 0,0

        if events[i][0] >= last_end:
            op1 = events[i][2] + solve(events, k-1,i+1,events[i][1])
        op2 = solve(events,k,i+1,last_end)
        DP[(k,i,last_end)] = max(op1,op2)
        return DP[(k,i,last_end)]   

    new_events = []

    for event in events:
        new_events.append((event[0]-1, event[1], event[2]))

    new_events.sort(key= lambda x: (x[0], -x[2]))   #sorted by start_time->val
    return solve(new_events, 2,0,0)

    # 2. ========================================== Binary Search
    time = []
    vals = []
    ans = prefix = 0
    for st, et, val in sorted(events, key=lambda x: x[1]): 
        prefix = max(prefix, val)
        k = bisect_left(time, st)-1
        if k >= 0: val += vals[k]
        ans = max(ans, val)
        time.append(et)
        vals.append(prefix)
    return ans 
```
{% endtab %}

{% tab title="2008" %}
```python
def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
    #1. DP ====================================================== [TLE]
    DP = {}
    def solve(rides, i, last_drop):
        if i >= len(rides):
            return 0

        if (i,last_drop) in DP:
            return DP[(i,last_drop)]
        op1, op2 = 0,0
        # if can pick up; then pick up
        if rides[i][0] >= last_drop:
            profit = rides[i][1] - rides[i][0] + rides[i][2]
            op1 = profit + solve(rides,i+1,rides[i][1])
        op2 = solve(rides, i+1, last_drop)
        DP[(i,last_drop)] = max(op1, op2)
        return DP[(i,last_drop)]

    rides.sort(key = lambda x: (x[0],-x[2]))
    return solve(rides,0,last_drop=0)
```
{% endtab %}

{% tab title="787" %}
```python
from collections import defaultdict
from heapq import heappush, heappop
'''
Simple Dijkstras
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1
```
{% endtab %}

{% tab title="581" %}
```python
if len(nums) <2:
    return 0

start = len(nums) - 1
prev = nums[start]
# find the smallest index not in place
for i in range(len(nums)-1, -1, -1):
    if prev < nums[i]:
        start = i
    else:
        prev = nums[i]

prev = nums[0]
end = 0
# find the largest index not in place
for i in range(0, len(nums)):
    if nums[i] < prev:
        end = i
    else:
        prev = nums[i]


if end != 0:
    return end - start + 1
else: 
    return 0
```
{% endtab %}

{% tab title="986" %}


![](<../.gitbook/assets/Screenshot 2021-11-08 at 2.25.37 AM.png>)



```python
def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0

    result = []
    while i < len(A) and j < len(B):
        a_start, a_end = A[i]
        b_start, b_end = B[j]
        if a_start <= b_end and b_start <= a_end:                       # Criss-cross lock
            result.append([max(a_start, b_start), min(a_end, b_end)])   # Squeezing

        if a_end <= b_end:         # Exhausted this range in A
            i += 1               # Point to next range in A
        else:                      # Exhausted this range in B
            j += 1               # Point to next range in B
    return result
```
{% endtab %}

{% tab title="750" %}
**Solution 1:**\
One straight-forward solution is: we can iterate any two rows, say r1 and r2, and for every column, we check if grid\[r1]\[c] == grid\[r2]\[c]. IF yes, we increate the count by 1. Then the number of rentangles formed by these two rows are count \* (count - 1) / 2.\
\
The time complexity of the solution is O(m^2 \* n). \
\
If the number of rows is significantly greater than number of columns, we can iterate the columns and check the rows for each of the two columns. Then the time complexity is&#x20;

O(n^2 \* m).

```java
public int countCornerRectangles(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length - 1; i++) {
            for (int j = i + 1; j < grid.length; j++) {
                int counter = 0;
                for (int k = 0; k < grid[0].length; k++) {
                    if (grid[i][k] == 1 && grid[j][k] == 1) counter++;
                }
                if (counter > 0) ans += counter * (counter - 1) / 2;
            }
        }
        return ans;
    }
```

\
**Solution 2:**\
Solution 2 is similar to solution 1. The main difference is we use a hash map to save the positions of the two rows.

_**Time Complexity:** O(N\*(M^2))_\
_**Auxiliary Space:** O(M^2)_\


```java
public int countCornerRectangles(int[][] grid) {
        if (grid == null || grid.length < 2 || grid[0] == null || grid[0].length < 2) {
            return 0;
        }
         
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
         
        int m = grid.length;
        int n = grid[0].length;
         
        for (int r1 = 0; r1 < m; r1++) {
            for (int r2 = r1 + 1; r2 < m; r2++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r1][c] == 1 && grid[r2][c] == 1) {
                        int pos = r1* n + r2;
                        if (map.containsKey(pos)) {
                            int val = map.get(pos);
                            ans += val;
                            map.put(pos, val + 1);
                        } else {
                            map.put(pos, 1);
                        }
                    }
                }
            }
        }
         
        return ans;
    }
```
{% endtab %}
{% endtabs %}

* [x] [55. Jump Game](https://leetcode.com/problems/jump-game/)
* [x] LC [939. Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)&#x20;
* [x] [1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
* [x] LC [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)
* [x] [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
* [x] [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
* [x] LC [973.K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | [O(N) quicksort approach](https://leetcode.com/problems/k-closest-points-to-origin/discuss/219442/Python-with-quicksort-algorithm) | #**quick\_sort**
* [x] **LC **[**855. Exam Room**](https://leetcode.com/problems/exam-room/)****
* [ ] LC [836. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) 🐽
* [ ] LC [465. Optimal Account Balancing](https://leetfree.com/problems/optimal-account-balancing) 🐽
* [ ] LC [68. Text Justification](https://leetcode.com/problems/text-justification/)
* [ ] LC [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
* [ ] [Battery Swap in Uber Cars](https://leetcode.com/discuss/interview-question/1095987/UBER-oror-CodeSignal) | binary search
* [ ] LC [128.Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
* [x] [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) 🐽🔴

{% tabs %}
{% tab title="55" %}
```python
def canJump(self, a: List[int]) -> bool:
    n = len(a)
    maxpos = 0

    for i in range(n):
        if i > maxpos:
            return False
        maxpos = max(maxpos, i+a[i])
    return True
```
{% endtab %}

{% tab title="939" %}
```python
def minAreaRect(self, points: List[List[int]]) -> int:

    seen = set()
    res = float('inf')
    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                area = abs(x1 - x2) * abs(y1 - y2)
                if area and area < res:
                    res = area
        seen.add((x1, y1))
    return res if res < float('inf') else 0

'''
TC: O(N^2)
'''
```
{% endtab %}

{% tab title="1074" %}


def numSubmatrixSumTarget(self, matrix: List\[List\[int]], target: int) -> int:

```
# PREFIX SUM
'''
For each row, calculate the prefix sum. 
For each pair of columns, calculate the sum of rows.

Time O(mnn)
Space O(m)
'''
m, n = len(matrix), len(matrix[0])
for x in range(m):
    for y in range(n - 1):
        matrix[x][y+1] += matrix[x][y]

res = 0
for y1 in range(n):
    for y2 in range(y1, n):
        preSums = {0: 1}
        s = 0
        for x in range(m):
            s += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
            res += preSums.get(s - target, 0)
            preSums[s] = preSums.get(s, 0) + 1
return res
```
{% endtab %}

{% tab title="363" %}
```python
def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    '''
    For each row, calculate the prefix sum. 
    For each pair of columns, calculate the sum of rows.

    Now this problem is changed to a 1D problem: max subarray sum no more than k.
    '''
    def maxSumSubarray(arr):
        sub_s_max = float('-inf')
        s_curr = 0
        prefix_sums = [float('inf')]
        for x in arr:
            bisect.insort(prefix_sums, s_curr)
            s_curr += x
            i = bisect.bisect_left(prefix_sums, s_curr - k)
            sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
        return sub_s_max

    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(n - 1):
            matrix[x][y+1] += matrix[x][y]
    res = float('-inf')
    for y1 in range(n):
        for y2 in range(y1, n):
            arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
            res = max(res, maxSumSubarray(arr))
    return res
```
{% endtab %}

{% tab title="542" %}
```python
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    DIR = [0, 1, 0, -1, 0]

    q = deque([])
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i + 1]
            if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
            mat[nr][nc] = mat[r][c] + 1
            q.append((nr, nc))
    return mat
'''
BFS from 0-cells
Complexity

Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
Space: O(M * N), space for the queue.
'''    
      
```
{% endtab %}

{% tab title="1579" %}


![](<../.gitbook/assets/Screenshot 2021-11-18 at 9.38.56 AM.png>)

```python
def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

    # Union find
    def find(i):
        if i != root[i]:
            root[i] = find(root[i])
        return root[i]

    def uni(x, y):
        x, y = find(x), find(y)
        if x == y: return 0
        root[x] = y
        return 1

    res = e1 = e2 = 0

    # Alice and Bob
    root = range(n + 1)
    for t, i, j in edges:
        if t == 3:
            if uni(i, j):
                e1 += 1
                e2 += 1
            else:
                res += 1
    root0 = root[:]

    # only Alice
    for t, i, j in edges:
        if t == 1:
            if uni(i, j):
                e1 += 1
            else:
                res += 1

    # only Bob
    root = root0
    for t, i, j in edges:
        if t == 2:
            if uni(i, j):
                e2 += 1
            else:
                res += 1

    return res if e1 == e2 == n - 1 else -1


'''
Union find:
Add Type3 first, then check Type 1 and Type 2.

Time O(E), if union find with compression and rank
Space O(E)

''' 
```
{% endtab %}
{% endtabs %}

* [x] LC 588. [Design In-Memory File System](https://leetfree.com/problems/design-in-memory-file-system)
* [x] [339. Evaluate Division](https://leetcode.com/problems/evaluate-division/)
* [x] **Textbook Buy Sell**
* [x] [**CurrencyConversion**](https://leetcode.com/discuss/interview-question/483660/google-phone-currency-conversion)
* [x] **Currency Arbitrage**: Now given any two currencies x and y. Find the best conversion rate. Basically a graph problem you will have to traverse all paths from x to y because you want the best conversion rate.
  * **follow up** - Rather than hardcoding the data use two apis - 1.) [https://api.pro.coinbase.com/products](https://api.pro.coinbase.com/products) to get the id like USD-EUR aka currency pair and 2.) [https://api.pro.coinbase.com/products/](https://api.pro.coinbase.com/products/)" + id + "/book to fetch the ask and bid price for each one of them. response = request.get(url) is enough to handle the GET calls + response.json() is enough to parse the response.

{% tabs %}
{% tab title="588" %}
```python
# l is the path length, 
# k is the number of entries in the last level directory(max_possible_path_len)
# =====================================
# Time:  ls: O(l + klogk), 
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.


class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""


class FileSystem:
    def __init__(self):
        self.__root = TrieNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.__root
        subdirs = path.split("/")[1:]
        if path == '/':
            subdirs = []
        for s in subdirs:
            curr = curr.children[s]

        #if its a file_path; return a list which only has this file's name
        # => lexicographical order
        if curr.is_file:
             return [subdirs[-1]]

        #if its a directory path: return lsit of file+directory names
        # in this directory 
        # => lexicographical order
        return sorted(curr.children.keys())

    # mkdir: O(l) ; l = path length
    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.__root
        subdirs = path.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_file = False
        return curr

    def readContentFromFile(self, filePath):
        """ 
        :type filePath: str
        :rtype: str
        """
        curr = self.__root
        subdirs = filePath.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr.content
    
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.__root
        subdirs = filePath.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_file = True
        curr.content += content

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir('/a/b/c')
    fs.addContentToFile('/a/b/c/d', 'hello')
    print(fs.ls("/"))
    print(fs.readContentFromFile('/a/b/c/d'))
    print(fs.ls("/a/b/c/d"))
```
{% endtab %}

{% tab title="(posh)588" %}
```python
# l is the path length, 
# k is the number of entries in the last level directory
# =====================================
# Time:  ls: O(l + klogk), 
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.


class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""


class FileSystem:
    def __init__(self):
        self.__root = TrieNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.__getNode(path)

        if curr.is_file:
            return [self.__split(path, "/")[-1]]

        return sorted(curr.children.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.__putNode(path)
        curr.is_file = False

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.__putNode(filePath)
        curr.is_file = True
        curr.content += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.__getNode(filePath).content

    def __getNode(self, path):
        curr = self.__root
        for s in self.__split(path, "/"):
            curr = curr.children[s]
        return curr

    def __putNode(self, path):
        curr = self.__root
        for s in self.__split(path, "/"):
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr

    def __split(self, path, delim):
        if path == "/":
            return []
        return path.split("/")[1:]


if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir('/a/b/c')
    fs.addContentToFile('/a/b/c/d', 'hello')
    print(fs.ls("/"))
    print(fs.readContentFromFile('/a/b/c/d'))
    print(fs.ls("/a/b/c/d"))
```
{% endtab %}

{% tab title="Txtbook" %}
```python
"""
You operate a market place for buying & selling used textbooks For a giventext book eg“TheoryofCryptography”
there are people who want to buy this textbook and people who want to sell

Offers to BUY: $100 $100 $99 $99 $97 $90
Offers to SELL: $109 $110 $110 $114 $115 $119

A match occurs when two people agree on a price 
Some new offers do not  match. These offers should be added to the active set of offers.

For example : Tim offers to SELL at $150 This will not match No one is willing to buy at that price so we save the offer

Offers to SELL::$109 $110 $110 $114 $115 $119 $150

When matching we want to give the customer the “best price”

Example matches : If Jane offers to BUY at $120

she will match and buy a book for $109 (the lowest offer)



====================== [APPROACH] ==================
Use two heaps. 
1. Max Heap : buy orders
2. Min Heap : sell orders

>>> Processing:
1. Buy Order Req comes(p):
    * we want to lowest sell price in list i.e. top of sell minH
    Case#1: (p > max_sell) there's a match => process order
    Case#2: (p <= max_sell)  not a match => add this in buy's heap for future

2. Sell Order req comes(p):
    * get top_val_from_buy_max_heap
    Case#1: (p < max_buy) match => process
    Case#2: (p >= max_buy): store in sell order's list

TC: O(n logn) --> because we put everything in the heaps which are O(log n) per offer/poll operations.
SC: O(n) --> we're putting the entire input lists in the heaps

"""
from heapq import heappush, heappop


class TextBookMarket():
    def __init__(self,buy_requests, sell_requests):
        self.__buy_requests = buy_requests
        self.__sell_requests = sell_requests
        self.__sell_min_heap = []
        self.__buy_max_heap = []
        self.__initialize_marketplace()
    
    def __initialize_marketplace(self):
        for sell in self.__sell_requests:
            heappush(self.__sell_min_heap, sell)
            
        # implement max heap
        for buy in self.__buy_requests:
            heappush(self.__buy_max_heap, -buy)

        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
    
    def process_buy(self, buy):
        max_sell = heappop(self.__sell_min_heap)
        if buy > max_sell:
            profit =  buy - max_sell
            print(f'\tPROFIT = {profit}')
            return profit
        print('your order has been stored.Please wait for better opportunity')
        heappush(self.__buy_max_heap,-buy)
        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
        return None
    
    def process_sell(self,sell):
        max_buy = (-1)*heappop(self.__buy_max_heap)
        
        if sell > max_buy:
            profit = sell - max_buy
            print(f'\tPROFIT = {profit}')
            return profit
        print('your order has been stored.Please wait for better opportunity')
        heappush(self.__sell_min_heap,sell)
        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
        return None

buys = [100, 100, 99, 99, 97, 90]
sells = [109, 110, 110, 114, 115, 119]

market = TextBookMarket(buys,sells)
market.process_buy(120)
market.process_buy(113)
market.process_buy(90)
```
{% endtab %}

{% tab title="339" %}
```python
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    G = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v
        
    def bfs(src, dst):
        if not (src in G and dst in G): return -1.0
        q, seen = [(src, 1.0)], set()
        for x, v in q:
            if x == dst: 
                return v
            seen.add(x)
            for y in G[x]:
                if y not in seen: 
                    q.append((y, v*G[x][y]))
        return -1.0
    return [bfs(s, d) for s, d in queries]
```
{% endtab %}

{% tab title="CurrConver" %}
```python
from collections import defaultdict
from collections import deque

def getRatio(start, end, data):
    adj = defaultdict(list)
    vis = dict()
    for node in data:
        adj[node[0]].append([node[1], node[2]])
        adj[node[1]].append([node[0], 1.0 / node[2]])
        vis[node[0]] = False
        vis[node[1]] = False
    
    # start BFS
    queue = deque()
    queue.append((start, 1.0))
    
    while queue:
        curr, num = queue.popleft()
        if vis[curr]:
            continue
        vis[curr] = True
         
        if curr in adj:
            values = adj[curr]
            neighbors = {}
            for val in values:
                neighbors[val[0]] = val[1]
            for key in neighbors:
                if not vis[key]:
                    if key == end:
                        res = num * neighbors[key]
                        return round(res,2)
                    queue.append((key, num * neighbors[key]))
    return -1


data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("GBP", "AUD", data))

''' ================= APIs =================='''
import requests, json
resp =  requests.get('http://api.pro.coinbase.com/products').json()
print(resp[0]['id'])
```
{% endtab %}

{% tab title="CurrArbi" %}
```python
from math import log

def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float("inf")] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    print(min_dist)
    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]
print(arbitrage(rates))

'''

TC: O(N^3)
SC: O(N^2)

For example, say we have a weighted edge path a -> b -> c -> d. 
Since we want to see if a * b * c * d > 1, we’ll take the negative log of each edge:

-log(a) -> -log(b) -> -log(c) -> -log(d).

The total cost of this path will then be

-(log(a) + log(b) + log(c) + log(d)) = -log(a * b * c * d).

-log(x) < 0 if x is greater than 1, so that’s why if we have a negative cost cycle, if means that the product of the weighted edges is bigger than 1.

The Bellman-Ford algorithm can detect negative cycles. So if we run Bellman-Ford on our graph and discover one, then that means its corresponding edge weights multiply out to more than 1, and thus we can perform an arbitrage.

'''
```
{% endtab %}
{% endtabs %}

## 2. Machine Coding

* [x] fare generation for a cab service | [Question Here](https://leetcode.com/discuss/interview-experience/682096/Uber-or-SE-2-or-Hyderabad) | @LLD:Question>1.FareGenerator
* [x] Design Map Reduce
* [x] pub-sub with concurrency | [Interview\_exp](https://leetcode.com/discuss/interview-experience/1453593/Uber-or-L4-or-SDE-II-or-Bangalore)
* [ ] Job Schedular | [exp](https://leetcode.com/discuss/interview-experience/951674/Uber-or-L4-or-Banglore-or-Oct-Nov-2020-Reject)
* [x] Design data structure to get/insert/delete an element. It should also support DeleteRandom method. All the methods should be O(1) | concurrency | [exp\_here](https://leetcode.com/discuss/interview-experience/469588/Uber-Onsite-or-L5-or-Dec-2019-or-SF-or-Reject)
* [ ] Minesweeper [here](https://leetcode.com/discuss/interview-question/770225/Uber-or-SDE2)

## 3. SysDesign

* [x] Spacial Problems/Quad Trees
* [x] uber system design | [here](https://leetcode.com/discuss/interview-question/1490926/Uber-System-Design)
* [ ] a service for Uber which would show a heatmap of active drivers around the world | [exp](https://leetcode.com/discuss/interview-experience/951674/Uber-or-L4-or-Banglore-or-Oct-Nov-2020-Reject)
* [ ] Parking Lot
* [x] Google Doc Commenting
* [x] Facebook Messenger
* [ ] multiplayer online chess game
* [ ] uber eats
* [x] Design distributed notification service
* [ ] Design a proximity service like Yelp.
* [x] Design a meeting scheduler.
* [x] Design a photo sharing application like instagram
* [x] chat system like whatsapp | with ticks
* [x] Design Amazon Wishlist
* [x] Google doc | [What’s different about the new Google Docs: Making collaboration fast](https://drive.googleblog.com/2010/09/whats-different-about-new-google-docs.html)

## =============================

## 4. HM
