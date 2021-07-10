# Greeeedy

## 1. Map



## 2. Hashing

### 2.1 Rolling Hash

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained)
* [ ] [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath) 



## 3. Queue/Stack/Monotonic

### 3.0 Notes:

* How to identify **stack** problem: there'll be an dependent second nested loop. EG:

```python
for i in range(0,N):
    # case1:
    for j in range(0,i): ...
    # case2:
    for j in range(i,0,-1): ...
    # case3:
    for j in range(i+1,N)): ..
    # etc etc
```

### 3.1 Standard Questions

#### NGL variants:

* [x] GfG: [Next Greatest Element](https://www.geeksforgeeks.org/next-greater-element/) \| **NGL**
* [x] [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O%281%29) \| similar to NGL \|  \| system design heavy🔒
* [x] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) \| simple implementation of `NSL+NSR` ❤️
  * **NOTE**: dont cram that single stack traversal method. This one is easy to derive on your own
* [x] [85.Maximal Rectangle Area In Binary Matrix](https://leetcode.com/problems/maximal-rectangle/) **`NSL+NSR`** add heights for every row&apply \#84's code😎

{% tabs %}
{% tab title="NGL" %}
```python
def ngl(arr):
    stk = []
    n = len(arr)
    res = []*n
    for i in range(n-1,-1,-1):
        while len(stk) and stk[-1] < arr[i]:
            stk.pop()
        if len(stk) == 0:
            res[i] = -1
        else:
            res[i] = stk[-1]
        stk.append(arr[i])
    return res
```
{% endtab %}

{% tab title="901" %}
```python
def lel(self, arr: int) -> int:
    arr = self.price
    n = len(arr)
    res = [1]*n
    stk = []    # stores indices
    
    for i in range(n):
        while len(stk) and arr[i] > arr[stk[-1]]:
            stk.pop()
        if len(stk) == 0:
            res[i] = 1
        else:
            res [i] = i-stk[-1]
        stk.append(i)
    return res 
```
{% endtab %}

{% tab title="84❤️" %}
```python
def largestRectangleArea(self, h: List[int]) -> int:
    n = len(h)
    # 1. get nsl - indices
    '''
  i:[0,1,2,3,4,5]
  h:[2,1,5,6,2,3]
nsl:[-1,-1,1,2,1,4]
    '''
    nsl = [0]*n
    stk = []
    
    for i in range(n):
        while stk and h[stk[-1]] >= h[i]:
            stk.pop()
        if len(stk) == 0:
            nsl[i] = -1
        else:
            nsl[i] = stk[-1]
        stk.append(i)
    print(nsl)
    
    # 2. get nsr - indices
    '''
  i:[0,1,2,3,4,5]
  h:[2,1,5,6,2,3]
nsr:[1,6,4,4,6,6]
    '''
    
    nsr = [0]*n
    stk = []
    for i in range(n-1,-1,-1):
        while stk and h[stk[-1]] >= h[i]:
            stk.pop()
        if len(stk) == 0:
            nsr[i] = n
        else:
            nsr[i] = stk[-1]
        stk.append(i)
    print(nsr)
    
    # 3. compute areas
    # (nsr[i] - nsl[i] - 1)*h[i]
    res = 0
    for i in range(n):
        area = abs(nsr[i] - nsl[i] - 1)*h[i]
        res = max(res,area)
    return res
```
{% endtab %}

{% tab title="85" %}
```python
def maximalRectangle(self, matrix: List[List[str]]):
    n= len(matrix)
    if n == 0:return 0
    m = len(matrix[0])
    
    grid = [[0 for i in range(m)]for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                grid[i][j] = int(matrix[i][j])
            elif i>0 and matrix[i][j]=="1":
                grid[i][j] = grid[i-1][j] + 1
    
    res = 0
    for row in grid:
         res = max(res,largestRectangleArea(row))      
    return res
```
{% endtab %}
{% endtabs %}

* [x] [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

```python
def trap(h: List[int]) -> int:
    n = len(h)
    if n == 0: return 0
    mxl = [h[0]]*n
    mxr = [h[-1]]*n
    
    max_yet = mxl[0]
    for i in range(1,n):
        max_yet = max(h[i],max_yet)
        mxl[i] = max_yet
    
    max_yet = mxr[-1]
    for i in range(n-1,-1,-1):
        max_yet = max(h[i],max_yet)
        mxr[i] = max_yet

    res = 0
    for i in range(n):
        res += min(mxl[i],mxr[i]) - h[i]
    return res
```



* [ ] [1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O%28N%29-Time-and-Space)
* [ ] [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution)
* [ ] [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-O%281%29-Space)
* [ ] **LC239. Sliding Window Maximum**
* [ ] **LC739. Daily Temperatures**
* [ ] **LC862. Shortest Subarray with Sum at Least K**
* [ ] **LC907. Sum of Subarray Minimums**

### 3.2 Rest of the problems

* [x] [391. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
* [x] [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) \|  for circular array 🚀
* [ ] [556.Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) 🍪🍪🍪
* [x] [155. Min Stack](https://leetcode.com/problems/min-stack/) : instead of 2 stacks, use single stack & insert pairs in it: `ele,min_ele`
  * Regular approach of `O(1)` =&gt; [Aditya Verma](https://www.youtube.com/watch?v=ZvaRHYYI0-4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=11&ab_channel=AdityaVerma)

### 3.3 Resources

* [Aditya Verma's Playlist](https://www.youtube.com/watch?v=P1bAPZg5uaE&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&ab_channel=AdityaVerma)

## 4. Heap

### 4.0 Notes

* **Complexity** with Heap\(of size K\) : `O(nlogK)` // while with sort it'll be `O(nlogn)`
* **NOTE:** if sorting is the only better way & asked to **do better than `O(nlogn)`** , heap is the way!
* **How to identify** if its a heap question? look for this keyword: `smallest/largest K elements`
* Which heap to choose when:\(hint: _opposite_, logic: we can pop the top element but not the bottom\) 
  * if **smallest K** elements   =&gt; use **max heap**
  * if **largest K**  elements     =&gt; use **min heap**

### 4.1 Standard Problems

**Top K Pattern**

* [x] [215.Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
* [x] GfG: [Sort a nearly sorted \(or K sorted\) array](https://www.geeksforgeeks.org/nearly-sorted-algorithm/)
* [x] [658.Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
* [x] [347.Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
* [x] [1636.Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) \| using 2 keys in heappush\(if 1st key same, sort by 2nd\)🚀
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
```
{% endtab %}
{% endtabs %}

* [x] GfG: [Sum of all elements between k1’th and k2’th smallest elements](https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/)
* [ ] [LC \#692](https://leetcode.com/problems/top-k-frequent-words) - Top k frequent words
* [ ] [LC \#264](https://leetcode.com/problems/ugly-number-ii/) - Ugly Number II
* [ ] [LC \#451](https://leetcode.com/problems/sort-characters-by-frequency/) - Frequency Sort
* [ ] [LC \#703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) - Kth largest number in a stream
* [ ] [LC \#719](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) - Kth smallest distance among all pairs
* [ ] [LC \#767](https://leetcode.com/problems/reorganize-string/) - Reorganize String
* [ ] [LC \#358](https://leetcode.com/problems/rearrange-string-k-distance-apart) - Rearrange string K distance apart
* [ ] [LC \#1439](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) - Kth smallest sum of a matrix with sorted rows

**Merge K sorted pattern**

* [ ] [LC \#23](https://leetcode.com/problems/merge-k-sorted-lists) - Merge K sorted
* [ ] [LC \#373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) - K pairs with the smallest sum
* [ ] [LC \#378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - K smallest numbers in M-sorted lists

**Two Heaps Pattern**

* [ ] [LC \#295](https://leetcode.com/problems/find-median-from-data-stream) - Find median from a data stream
* [ ] [LC \#480](https://leetcode.com/problems/sliding-window-median/) - Sliding window Median
* [ ] [LC \#502](https://leetcode.com/problems/ipo/) - Maximize Capital/IPO

**Minimum number Pattern**

* [ ] [LC \#1167](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) - Minimum Cost to connect sticks/ropes
* [ ] [LC \#253](https://leetcode.com/problems/meeting-rooms-ii) - Meeting Rooms II
* [ ] [LC \#759](https://leetcode.com/problems/employee-free-time) - Employee free time
* [ ] [LC \#857](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) - Minimumcost to hire K workers
* [ ] [LC \#621](https://leetcode.com/problems/task-scheduler/) - Minimum number of CPU \(Task scheduler\)
* [ ] [LC \#871](https://leetcode.com/problems/minimum-number-of-refueling-stops/) - Minimum number of Refueling stops

### 4.2 Rest of the Problems

\*\*\*\*

## 5.Sort



## 6.Binary Search

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained) =&gt; **Rolling Hash/Rabin Karp**
* [ ] [658.Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) \| [Soln](https://leetcode.com/problems/find-k-closest-elements/discuss/915047/Finally-I-understand-it-and-so-can-you.)



[Aditya Verma playlist](https://www.youtube.com/watch?v=j7NodO9HIbk&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&ab_channel=AdityaVerma)

## 7.Two Pointers



## 9.Sliding Window

* **Fixed Size: How I do it?**
* 1. Create first window 
  2. iterate in array for next window onwards

{% hint style="info" %}
**Dynamic Size:** WHEN DOES SLIDING WINDOW WORK?

ONLY when you're working with all negative or positives or if your input is sorted
{% endhint %}

### 9.1 Standard Problems

#### Fixed Size Window

* [x] GfG\#1: [Maximum sum of subarray of size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)
* [x] GfG\#2 [First negative integer in every window of size k](https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/#:~:text=Recommended%3A%20Please%20solve%20it%20on,the%20current%20subarray%28window%29.)
* [x] [438.Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) 🚀
* [x] [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) 🍪🍪🍪

{% tabs %}
{% tab title="\#1" %}
```python
def maximumSumSubarray (k,arr,n):
    if n == 0: return 0
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    res = curr_sum
    for r in range(k,n):
        l = k-j
        curr_sum += -arr[l] + arr[r]
        res = max(res, curr_sum)
    return res
```
{% endtab %}

{% tab title="\#2" %}
```python
def printFirstNegativeInteger( a,n,k):
    negs,res = [],[]
    for i in range(k):
        if a[i]<0:
            negs.append(a[i])
    res.append(negs[0])
    
    for r in range(k,n):
        l = r-k         # l is "just outside the window on left"
        if a[r]<0:
            negs.append(a[r])
        if negs and a[l] == negs[0]:
                negs.pop(0)
        
        if len(negs):
            res.append(negs[0])
        else:
            res.append(0)
    return res
```
{% endtab %}

{% tab title="438" %}
```python
from collections import Counter

def findAnagrams(self, s: str, p: str) -> List[int]:
    pdic = Counter(p)
    k = len(p)
    
    res = []
    sdic = Counter(s[:k])
    if pdic == sdic:
        res.append(0)
    
    for r in range(k,len(s)):
        l = r - k       # just left outside
        # remove left
        sdic[s[l]] -= 1
        if sdic[s[l]] == 0:
            sdic.pop(s[l])
        
        #add right  
        # plain 'sdic[s[r]] += 1' is also supported in python ;in place of this if-else 
        if s[r] in sdic.keys():
            sdic[s[r]] += 1
        else:
           sdic[s[r]] = 1
           
        if pdic == sdic:
            res.append(l+1)
    return res
```
{% endtab %}

{% tab title="" %}
```python
from heapq import heappush, heappop
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # sliding window + max_heap
    # TRICK: keep discarding the non-important numbers
    heap = []   
    for i in range(k):
        while len(heap) > 0 and nums[heap[0][1]]< nums[i]:
            heappop(heap)
        heappush(heap,(-nums[i],i))    # '-' as maxheap
        
    res = []
    res.append(nums[heap[0][1]])
    
    for r in range(k,len(nums)):
        l = r-k # just outer left
        
        # delete left
        if len(heap) and nums[heap[0][1]] == nums[l]:
            heappop(heap)
        
        # add right
        while len(heap) > 0 and nums[heap[0][1]] < nums[r]:
            heappop(heap)
        heappush(heap,(-nums[r],r))    # '-' as maxheap
        res.append(nums[heap[0][1]])
    return res
```
{% endtab %}
{% endtabs %}

#### Dynamic Size Window

* [x] [560.Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)✅
  * **NOTE:** Sliding window technique works only for all positive/all negative \(i.e. not for arr with both pos & neg numbers\).So soln\#1 below gets WA
* [x] GfG\#1: [Longest substring with k unique characters](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/) ❤️
  * [x] SIMILAR: [904.Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/submissions/)
* [x] [424.Longest Repeating Character Replacement ](https://leetcode.com/problems/longest-repeating-character-replacement/)\(similar to \#1\) 🚀🚀

{% tabs %}
{% tab title="560✅" %}
```python
def subarraySum(self, nums: List[int], k: int) -> int:
    # =================[DOESNT work for neg+pos arr]==========
    cnt = 0
    l,r=0,0
    n = len(nums)
    curr = 0
    for r in range(0,n):
        curr += nums[r]
        while l<r and curr > k:
            curr -= nums[l]
            l += 1
        if curr == k:
            cnt += 1        
    return cnt

    # =================[works for neg+pos+unsorted numbers arr]=======
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums-k,0)
        d[sums] = d.get(sums,0) + 1
    
    return(count)
```
{% endtab %}

{% tab title="GfG\#1" %}
```python
def longestKSubstr(s, k)
    res = 0
    l = 0
    count = Counter()
    for r in range(0,len(s)):            
        count[s[r]] += 1        
        while l<r and len(count) > k:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                count.pop(s[l])
            l += 1
        if len(count) == k:
            res = max(res,r-l+1)
    return res
```
{% endtab %}

{% tab title="424" %}
```python
def characterReplacement(self, s: str, k: int) -> int:
    # NOTE: exactly same as 'Longest K unique characters substring' 
    # .... BUT....
    # How to find no. of non-unique chars in substrings??
    
    res,max_freq = 0,0
    l = 0
    count = Counter()
    for r in range(0,len(s)):            
        count[s[r]] += 1
        foo = r-l+1 - max(count.values()) # 'foo' -> no. of MINORITY characters to be replaced
       
        while l<r and (r-l+1 - max(count.values())) > k:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                count.pop(s[l])
            l += 1
            
        foo = r-l+1 - (max(count.values()) if count else 0)
        if foo <= k:    # as 'ATMOST'
            res = max(res,r-l+1)
    return res
```
{% endtab %}
{% endtabs %}

* [ ] [76.Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)🔒🔒

### 9.2 Other Problems

* [ ]  * [https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
  * [https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)
  * [https://leetcode.com/problems/replace-the-substring-for-balanced-string/](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)
  * [https://leetcode.com/problems/max-consecutive-ones-iii/](https://leetcode.com/problems/max-consecutive-ones-iii/)
  * [https://leetcode.com/problems/subarrays-with-k-different-integers/](https://leetcode.com/problems/subarrays-with-k-different-integers/)
  * [https://leetcode.com/problems/fruit-into-baskets/](https://leetcode.com/problems/fruit-into-baskets/)
  * [https://leetcode.com/problems/get-equal-substrings-within-budget/](https://leetcode.com/problems/get-equal-substrings-within-budget/)
  * [https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)
  * [https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
  * [https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)
  * [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

 



## 10.Intervals Question

