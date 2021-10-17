# --->Greedy

## 5. List & String

* [x] [18. 4Sum](https://leetcode.com/problems/4sum/) - generalized for **Ksum**
* [x] [1021.Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
* [x] [443.String Compression](https://leetcode.com/problems/string-compression/)
* [x] [1520.Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) 🍪🍪🍪
* [x] LC: [8.String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
* [x] CSES: [Palindrome Reorder](https://cses.fi/problemset/task/1755)
* [x] \*\*TYPE: Count # Inversions \*\*✅
  * [x] CSES: [Collecting Numbers](https://cses.fi/problemset/task/2216) | [Approach](https://discuss.codechef.com/t/cses-collecting-numbers/83775)
  * [x] CSES: [Collecting Numbers II](https://cses.fi/problemset/task/2217) | [Video](https://www.youtube.com/watch?v=LEL3HW4dQew\&ab_channel=ARSLONGAVITABREVIS) 🐽
* [x] CSES: [Subarray Sum 1](https://cses.fi/problemset/task/1660/) | only "prefix sum"
* [x] CSES: [Subarray Sum 2](https://cses.fi/problemset/task/1661) | neg numbers | prefix sum **+** map
* [x] CSES: [Subarray Divisibility](https://cses.fi/problemset/result/2648945/) | ✅
* [x] LC 44: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
* [x] LC [163. Missing Ranges](https://leetfree.com/problems/missing-ranges)
* [x] LC [179.Largest Number](https://leetcode.com/problems/largest-number/) 🐽
* [x] LC [41.First Missing Positive](https://leetcode.com/problems/first-missing-positive/) ✅🍪🍪🍪
* [x] LC [14.Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) ✅| kaafi clever | longest common prefix
* [x] LC [334.Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | **O(N)**
* [x] LC [68. Text Justification](https://leetcode.com/problems/text-justification/) 💪🔴
  * Asked in Coinbase \*\*Karat Test \*\*| multiple times
  * so many corner cases; impossible to solve in interview
  * Built upon \[EASY] [1592.Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) ✅💪

{% tabs %}
{% tab title="18" %}
```python
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def dfs(l, r, k, target, path, out):  # [l, r] inclusive
        if k == 2:
            while l < r:
                if nums[l] + nums[r] == target:
                    out.append(path + [nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                    l, r = l + 1, r - 1
                elif nums[l] + nums[r] > target:
                    r -= 1  # Decrease sum
                else:
                    l += 1  # Increase sum
            return

        while l < r:
            dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
            while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
            l += 1

    def kSum(k):  # k >= 2
        ans = []
        nums.sort()
        dfs(0, len(nums)-1, k, target, [], ans)
        return ans

    return kSum(4)
```
{% endtab %}

{% tab title="Collecting Numbers✅" %}
```python
# 1. ==================== LIS doesnt work here: WA
tails = []
LIS = [1]*n

for i,x in enumerate(A):
    idx = bisect.bisect_left(tails,x)
    if idx == len(tails):
        tails.append(x)
        if len(tails) > 1:
            LIS[i] = LIS[idx-1]+1
    else:
        tails[idx] = x
        if idx > 0 and LIS[idx -1] == LIS[i]:
            LIS[i] = LIS[idx-1]+1
        else:
            LIS[i] = LIS[idx]
print(sum(x for x in LIS if x==1))

# 2. ============== Count inversions (as numbers are in 1...n)

s = set()
cnt = 0
for x in A:
    if x-1 not in s:
        cnt += 1
    s.add(x)

print(cnt)

'''
VIDEO: https://www.youtube.com/watch?v=lhhHCZYoJvs&ab_channel=ARSLONGAVITABREVIS
'''
```
{% endtab %}

{% tab title="Subarray Sum 2" %}
```python
I = lambda : map(int, input().split())
n,x = I()

A = list(I())

d = dict()
d[0] = 1
cnt = 0
curr = 0

for e in A:
    curr += e
    if curr - x in d:
        cnt += d[curr-x]

    if curr in d:
        d[curr] += 1
    else:
        d[curr] = 1
print(cnt)
```
{% endtab %}

{% tab title="Subarray Divisibility" %}
```python
d = dict()
d[0] = 1
cnt = 0
curr = 0

for e in A:
    curr = (curr+e+n)%n # '+n' because of negative numbers
    if curr in d:
        cnt += d[curr]

    if curr in d:
        d[curr] += 1
    else:
        d[curr] = 1
print(cnt)
```
{% endtab %}

{% tab title="atoi" %}
```python
ls = list(s.strip())
if len(ls) == 0 : return 0

sign = -1 if ls[0] == '-' else 1
if ls[0] in ['-','+'] : del ls[0]
ret, i = 0, 0
while i < len(ls) and ls[i].isdigit() :
    ret = ret*10 + ord(ls[i]) - ord('0')
    i += 1
return max(-2**31, min(sign * ret,2**31-1))
```
{% endtab %}

{% tab title="41.✅" %}
```python
# 1. O(NlogN) ===========================
        
nums.sort()
res = 1
for e in nums:
    if res == e:
        res += 1
return res

# 2. O(N) ===================================
# missing number will be in range [1,n]

n = len(nums)

# ignore all out of bound numbers
for i in range(n):
    if nums[i] <= 0 or nums[i] > n:
        nums[i] = n + 1
        
 # mark all the numbers                
for i in range(n):
    if abs(nums[i]) > n:
        continue
    nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

# return first unmarked number
for i in range(n):
    if nums[i] > 0:
        return i + 1
return n + 1
```
{% endtab %}

{% tab title="14." %}
```python
if not strs: return ''
        
m, M = min(strs), max(strs)

for i, c in enumerate(m):
    if c != M[i]:  
        return m[:i]
return m
```
{% endtab %}

{% tab title="334." %}
```python
def increasingTriplet(self, nums: List[int]) -> bool:
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
```
{% endtab %}

{% tab title="1592" %}
```python
def reorderSpaces(self, text: str) -> str:

    spaces = text.count(" ")
    words = text.split()
    if len(words) == 1:
        return words[0] + (" " * spaces)

    sep_count = len(words) - 1
    spaces_between_words = spaces // sep_count
    spaces_in_the_end = spaces % sep_count
    return (" " * spaces_between_words).join(words) + (" " * spaces_in_the_end)
```
{% endtab %}

{% tab title="68" %}
```python
def fullJustify(self, words: List[str], maxWidth: int):
    
    #--------------------------------------
    # Updated version of EASY: [1592. Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/)
    def reorderSpaces(text):
        spaces = text.count(" ")
        s = text.split(" ")

        while "" in s :
            s.remove("")

        if len(s) == 1:
            return s[0] + " "*spaces

        #min no of spaces between each word
        nsw = spaces//(len(s)-1)
        #no. of spaces left 
        nsl = spaces%(len(s)-1)
        result = ""
        for i in range(len(s)) :
            if i != len(s)-1 :
                result += s[i] + (" ")*nsw
                if nsl > 0:
                    result += " "
                    nsl -= 1
            else:
                result += s[i]  
        return result
    #--------------------------------------
    result = []
    last = words.pop(0)
    while words:
        if len(last) + len(words[0])  >= maxWidth :
            t = last + (" ")*(maxWidth-len(last))
            last = words.pop(0)
            result.append(t)
        elif len(last) + len(words[0]) < maxWidth :
            last = last + " " + words.pop(0)             
    result.append(last + (" ")*(maxWidth-len(last)))

    #reorder every row
    for i in range(len(result)-1):
        result[i] = reorderSpaces(result[i])
    return result 
        
```
{% endtab %}
{% endtabs %}

* [x] CF: [C.Unstable String](https://codeforces.com/problemset/problem/1535/C)

{% tabs %}
{% tab title="UnstableStr" %}
```python
def solve(s):
    res = 0
    pos0, pos1 = 0,0
    for c in s:
        if c == '0':
            pos0 += 1
            pos1 = 0
            res += pos0
        elif c == '1':
            pos1 += 1
            pos0 = 0
            res += pos1
        else:
            pos1 += 1
            pos0 += 1
            res += max(pos1,pos0)
        pos1, pos0 = pos0,pos1
    return res

t = int(input())
while t:
    t -= 1
    s = str(input())
    print(solve(s))
```
{% endtab %}
{% endtabs %}

### 1.2 String Matching Algo

* [x] [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/) 🐽

{% tabs %}
{% tab title="Naive Search" %}
```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1

# ============================ One Line code =============================
def strStr(self, haystack: str, needle: str) -> int:
         return haystack.find(needle)
```
{% endtab %}

{% tab title="KMP" %}
```python
# TC: O(N) =========================================================
def strStr(self, haystack: str, needle: str) -> int:
    lps = [0] * len(needle)
    i, j = 1, 0
    if not needle:
        return 0
    # preprocess needle
    while i < len(needle):
        if needle[i] == needle[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j - 1]
    i, j = 0, 0
    # find using lps
    while i < len(haystack) and j < len(needle):
        if needle[j] == haystack[i]:
            if j == len(needle) - 1:
                return i - j
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                continue
            j = lps[j - 1]
    return -1
```
{% endtab %}

{% tab title="Z Algorithm" %}
```python
# TC: O(N) =========================================================
def strStr(self, haystack: str, needle: str) -> int:
    s = needle + "$" + haystack
    left, right = 0, 0
    z = [0] * len(s)
    if not len(needle):
        return 0
    for k in range(1, len(s)):
        if k > right:
            right = left = k
            while right < len(s) and s[right] == s[right - left]:
                right += 1
            z[k] = right - left
            right -= 1
            if z[k] == len(needle):
                return k - 1 - len(needle)
        else:
            if z[k - left] < right - k + 1:
                z[k] = z[k - left]
            else:
                left = k
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                z[k] = right - left
                right -= 1
                if z[k] == len(needle):
                    return k - 1 - len(needle)
    return -1
```
{% endtab %}

{% tab title="Rabin Karp" %}
```python
def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        hck,nle=0,0
        if n<m: return -1
        for i in range(m):
                hck=10*hck+ord(haystack[i])
                nle=10*nle+ord(needle[i])
        for i in range(n-m+1):
                if hck==nle:
                        return i
                if i==n-m: break
                hck=10*(hck-ord(haystack[i])*10**(m-1))+(ord(haystack[i+m]))    
        return -1
```
{% endtab %}
{% endtabs %}

### ### --\[CP :: Array] --###############################\#

* [x] CF: [1367B. Even Array](https://codeforces.com/contest/1367/problem/B)
* [x] CF:[ 1353A. Most Unstable Array](https://codeforces.com/contest/1353/problem/A)
*

{% tabs %}
{% tab title="1367B" %}
```python
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(I())
    
    misp_o, misp_e = 0,0
    for i,x in enumerate(a):
        if (i%2 != 0) and (x%2 == 0):
            misp_o += 1
        if (i%2 == 0) and (x%2 != 0):
            misp_e += 1
    if misp_e != misp_o:
        print('-1')
    else:
        print(misp_o)
```
{% endtab %}

{% tab title="1353A" %}
```python
T = int(input())
for _ in range(T):
    n,m = I()
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2*m)
```
{% endtab %}
{% endtabs %}

### ### --\[CP :: String] --###############################\#

*

{% tabs %}
{% tab title="" %}
```python
```
{% endtab %}
{% endtabs %}

## 2. Hashing

### 2.1 Rolling Hash

* [x] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [**Rabin-Karp**](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o\(n-log-n\)-explained)\*\*\*\*
* [ ] [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath)

{% tabs %}
{% tab title="1044" %}
```python
def RabinKarp(self,text, M, q):
    if M == 0: return True
    h, t, d = (1<<(8*M-8))%q, 0, 256

    dic = defaultdict(list)

    for i in range(M): 
        t = (d * t + ord(text[i]))% q

    dic[t].append(i-M+1)

    for i in range(len(text) - M):
        t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
        for j in dic[t]:
            if text[i+1:i+M+1] == text[j:j+M]:
                return (True, text[j:j+M])
        dic[t].append(i+1)
    return (False, "")

def longestDupSubstring(self, S):
    beg, end = 0, len(S)
    q = (1<<31) - 1 
    Found = ""
    while beg + 1 < end:
        mid = (beg + end)//2
        isFound, candidate = self.RabinKarp(S, mid, q)
        if isFound:
            beg, Found = mid, candidate
        else:
            end = mid

    return Found
```
{% endtab %}
{% endtabs %}

## 5. Heap

### 5.0 Notes

* **Complexity** with Heap(of size K) :` O(nlogK)` // while with sort it'll be `O(nlogn)`
* \*\*NOTE: \*\*if sorting is the only better way & asked to **do better than `O(nlogn)`** , heap is the way!
* \*\*How to identify \*\*if its a heap question? look for this keyword: `smallest/largest K elements`
* Which heap to choose when:(hint: _opposite_, logic: we can pop the top element but not the bottom)
  * if **smallest K** elements => use **max heap**
  * if\*\* largest K **elements => use** min heap\*\*

### 5.1 Standard Problems

**Top K Pattern**

* [x] [215.Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
* [x] GfG: [Sort a nearly sorted (or K sorted) array](https://www.geeksforgeeks.org/nearly-sorted-algorithm/)
* [x] [658.Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
* [x] [347.Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
* [x] [1636.Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) | using 2 keys in heappush(if 1st key same, sort by 2nd)🚀
* [x] [973.K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

{% tabs %}
{% tab title="658" %}
```python
from heapq import heapify, heappush, heappop

def findClosestElements(arr, k, x) -> List[int]:
    # 1. subtract x from all arr ele
    # 2. return K smallest ele - the usual maxHeap way
    h = []      # contains tuple (dist,idx)
    res = []
    for i in range(len(arr)):
        heappush(h,(abs(x-arr[i]),i)) 
        if len(h) > k:
            heappop(h)
            
    while h:
        res.append(arr[heappop(h)[1]])
    res.reverse()
    return res
```
{% endtab %}

{% tab title="347" %}
```python
from heapq import heappush, heappop
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    h = []
    for x in count:
        heappush(h,(count[x],x))
        if len(h) > k:
            heappop(h)
    res = []
    while h:
        res.append(heappop(h)[1])
    return res
```
{% endtab %}

{% tab title="1636" %}
```python
from heapq import heappop, heappush, heapify

def frequencySort(self, A):
    count = collections.Counter(A)
    # =================== 1. sorting : O(NlogN) ==============================
    return sorted(A, key=lambda x: (count[x], -x))
    #2. ================ 2. min_heap: O(NlogK) , K = #unique elements =========
    h, res = [], []
    C = collections.Counter(A)
    for k, c in C.items():
        for _ in range(c):
            # "If multiple values have the same frequency, sort them in decreasing order"
            heappush(h, (c, -k)) 
    while h:
        res.append(-heappop(h)[1])
    return res
        
```
{% endtab %}

{% tab title="973" %}
```python
from heapq import heappop, heappush

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def dist(point):
        return math.sqrt(point[0]**2 + point[1]**2)
    
    #1. === Sort : O(NlogN) ==============================================
    points.sort(key = lambda x: dist(x))
    return points[:k]
    
    #2. === MaxHeap: O(NlogK) ===========================================
    heap = []
    for point in points:
        heappush(heap, (-dist(point),point))
        if len(heap) > k:
            heappop(heap)
    res = []
    while heap:
        res.append(heappop(heap)[1])
    return res
    #3. ============ QuickSort : avg case: O(N), worst: O(N^2) ===========
    dist = lambda x: A[x][0]**2 + A[x][1]**2
    
    def partition(l,r, pvt):
        # 1. move pivot to end
        A[pvt],A[r] = A[r],A[pvt]
        
        # 2. move all smaller elements in start
        start = l
        for i in range(l,r):
            if dist(i) < dist(pvt):
                A[start], A[i] = A[i],A[start]
                start += 1
        
        # 3. move pivot(now @r) ele to its correct position
        A[start],A[r] = A[r],A[start]
        return start

    n = len(A)
    lo, hi = 0, n-1
    while lo<hi:
        #step 1 in quick sort : pick a pivot
        pvt = hi        
        # pvt = random.randint(lo,hi) # to avoid the worst case of O(N^2)
        #step 2 in quick sort: partition
        pvt = partition(lo,hi,pvt)  # now; after partition pvt element is ats correct position
        if pvt < k:
            lo = pvt+1
        elif pvt > k:
            hi = pvt - 1
        else:
            break
    return A[:k]
```
{% endtab %}
{% endtabs %}

* [x] GfG: [Sum of all elements between k1’th and k2’th smallest elements](https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/)
* [x] [1337.The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)
* [ ] [LC #692](https://leetcode.com/problems/top-k-frequent-words) - Top k frequent words
* [ ] [LC #264](https://leetcode.com/problems/ugly-number-ii/) - Ugly Number II
* [ ] [LC #451](https://leetcode.com/problems/sort-characters-by-frequency/) - Frequency Sort
* [ ] [LC #703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) - Kth largest number in a stream
* [ ] [LC #719](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) - Kth smallest distance among all pairs
* [ ] [LC #767](https://leetcode.com/problems/reorganize-string/) - Reorganize String
* [ ] [LC #358](https://leetcode.com/problems/rearrange-string-k-distance-apart) - Rearrange string K distance apart
* [ ] [LC #1439](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) - Kth smallest sum of a matrix with sorted rows

**Merge K sorted pattern**

* [ ] [LC #23](https://leetcode.com/problems/merge-k-sorted-lists) - Merge K sorted
* [ ] [LC #373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) - K pairs with the smallest sum
* [ ] [LC #378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - K smallest numbers in M-sorted lists

**Two Heaps Pattern**

* [x] [LC #295](https://leetcode.com/problems/find-median-from-data-stream) - Find median from a data stream 🌟
* [x] [LC #480](https://leetcode.com/problems/sliding-window-median/) - Sliding window Median
* [ ] [LC #502](https://leetcode.com/problems/ipo/) - Maximize Capital/IPO

**Minimum number Pattern**

* [ ] [LC #1167](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) - Minimum Cost to connect sticks/ropes
* [ ] [LC #253](https://leetcode.com/problems/meeting-rooms-ii) - Meeting Rooms II
* [ ] [LC #759](https://leetcode.com/problems/employee-free-time) - Employee free time
* [ ] [LC #857](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) - Minimumcost to hire K workers
* [ ] [LC #621](https://leetcode.com/problems/task-scheduler/) - Minimum number of CPU (Task scheduler)
* [ ] [LC #871](https://leetcode.com/problems/minimum-number-of-refueling-stops/) - Minimum number of Refueling stops

### 5.2 Rest of the Problems

* [x] [1046.Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
* [x] CSES: [Josephus Problem I](https://cses.fi/problemset/task/2162)

{% tabs %}
{% tab title="Josephus I" %}
```python
n = int(input())
d = deque([i for i in range(1,n+1)])

while d:
    bach_gya = d.popleft()
    d.append(bach_gya) # bachao
    gya = d.popleft()
    print(gya)
```
{% endtab %}

{% tab title="295" %}
```python
from heapq import *

'''
O(log n) : add, O(1) : find

When we have new element num, we always put it to small heap, 
and then normalize our heaps:
     remove biggest element from the small heap 
     and put it to the large heap. 
 After this operation we can be sure that 
 we have the property that 
 the largest element in small heap is smaller than smaller elements in large heap.
'''
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            # push to small
            heappush(self.small, -num)
            # rebalance
            heappush(self.large, -heappop(self.small))
        else:
            # push to large
            heappush(self.large, num)
            # rebalance
            heappush(self.small, -heappop(self.large))

    def findMedian(self):
        
        if len(self.small) == len(self.large):
            return float(self.large[0] + (-self.small[0])) / 2.0
        else:
            return float(self.large[0])
        
```
{% endtab %}
{% endtabs %}

##

##
