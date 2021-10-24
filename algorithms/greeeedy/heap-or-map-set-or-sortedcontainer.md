# Heap | Map-Set | SortedContainer

## 1. Map-set Problems

* [x] LC [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) ✅🌇| uses \*\*SortedList \*\*
* [x] LC[ 146. LRU Cache](https://leetcode.com/problems/lru-cache/) ✅✅✅
* [x] [1700.Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
* [x] LC: [480 Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) ✅✅⭐️🚀 // `O(logK)` **NOTE: Dont skip w/o doing it!!!!!!!**
  * Video: [link](https://www.youtube.com/watch?v=UGs\_kQxJNPk\&ab\_channel=ARSLONGAVITABREVIS)
* [x] CSES: [Sliding Cost](https://cses.fi/problemset/task/1077/) | very similar to Sliding Medium; jst keep two sums: `upperSum` & `lowerSum`
* [x] CSES: [Maximum Subarray Sum II](https://cses.fi/problemset/task/1644/) | idea [here](https://discuss.codechef.com/t/help-with-maximum-subarray-sum-ii-from-cses/73404) 🐽
* [x] LC [315.Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) 🍪🍪🍪| \*\*SortedList | \*\*BST | MergeSort
* [x] LC [1347. Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) | **@google ✅💪**

{% tabs %}
{% tab title="218 🌇" %}
```python
from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        
        for l,r,h in buildings:
            events.append((l,h,-1)) #starting event
            events.append((r,h,1))  #ending event
            
        events.sort()   #sort by X cordinate
        n = len(events)
        
        res = []
        active_heights = SortedList([0]) #min heap of curr all hights in current window
        
        i = 0
        while i<n:
            curr_x = events[i][0]
            
            #process all events with same X together
            while i<n and events[i][0] == curr_x:
                x,h,t = events[i]
                
                if t == -1:                      #starting event
                    active_heights.add(h)
                else:
                    active_heights.remove(h)    #ending event
                i += 1
                
            #check if biggest height has changed in window due to this event
            if len(res) == 0 or (len(res) > 0 and res[-1][1] != active_heights[-1]):
                res.append((curr_x, active_heights[-1]))
        return res
```
{% endtab %}

{% tab title="146." %}
```python
#1. ================================= SLOWER :: using dict()
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.deque = deque()
    
    def _find(self, key: int) -> int:
		#Linearly scans the deque for a specified key. Returns -1 if it does not exist, returns the index of the deque if it exists
        for i in range(len(self.deque)):
            x = self.deque[i]
            if x[0] == key:
                return i 
        return -1
    
    def get(self, key: int) -> int:
        idx = self._find(key)
        if idx == -1:
            return -1
        else:
            k, v = self.deque[idx]
            del self.deque[idx] # We have to put this pair at the end of the queue so, we have to delete it first
            self.deque.append((k, v)) # And now, we put it at the end of the queue. So, the most viewed ones will be always at the end and be saved from popping when new capacity got hit.
            return v
                

    def put(self, key: int, value: int) -> None:
        idx = self._find(key)
        if idx == -1:
            if len(self.deque) >= self.size:
                self.deque.popleft()
            self.deque.append((key,value))
        else:
            del self.deque[idx]
            self.deque.append((key, value))
            
#2. ========================================= FASTER : using OrderedDict
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict
            
		    self.cache[key] = value
		
'''
The reason that using OrderedDict was faster than using deque is:
* the method move_to_end() in OrderedDict is in O(1) time complexity
     => (it uses a dictionary to record the location of each element) 
 * but the remove() method in deque is O(n) 
     => (have to iterate the double-linked list to find the element)
'''
```
{% endtab %}

{% tab title="480.✅" %}
```python
# 1. using SortedList ======================================== O(n log k)
from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums, k: int):
    	S = SortedList()
        # Initialize sorted list with first k - 1 elements of nums.
    	for i in range(k-1):
    		S.add(nums[i])  
            
    	i = k-1
    	res = []
    	while(i<len(nums)):
    		S.add(nums[i])
    		if k%2==0:
    			res.append((S[k//2 -1] + S[k//2])/2)
    		else:
    			res.append(S[k//2])
    		S.remove(nums[i-k+1])
    		i+=1
    	return res 
   

# 2. Using Two Heaps ============================================ O(NlogN) 
def medianSlidingWindow(self, nums, k):
        low = []  # lo is max-heap 
        high = [] # high is min-heap
        
        for i in range(k):
            heapq.heappush(high, (nums[i], i)) # high is a min-heap
            
        for _ in range(k>>1):
            self.convert(high, low)
            
        ans = [high[0][0]*1. if k&1 else (high[0][0]-low[0][0])/2]
        
        for i in range(len(nums[k:])):
            if nums[i+k] >= high[0][0]:
                heapq.heappush(high, (nums[i+k], i+k))
                if nums[i] <= high[0][0]: # keep the number of elements between two heap always in balance
                    self.convert(high, low)
            else:
                heapq.heappush(low, (-nums[i+k], i+k))
                if nums[i] >= high[0][0]:
                    self.convert(low, high)
            while low and low[0][1] <= i: heapq.heappop(low)
            while high and high[0][1] <= i: heapq.heappop(high)
            ans.append(high[0][0]*1. if k&1 else (high[0][0]-low[0][0])/2.)
        return ans
        
                    
    def convert(self, heap1, heap2): # convert min-heap1 to max-heap2
        element, index = heapq.heappop(heap1)
        heapq.heappush(heap2, (-element, index))
```
{% endtab %}

{% tab title="Sliding Sum" %}
```cpp
const ll mn = (ll) 2e5+5;

ll N, K;
ll arr[mn];
multiset<ll> up;
multiset<ll> low;
ll sLow, sUp;

void ins(ll val){
	ll a = *low.rbegin();
	if(a < val){
		up.insert(val); sUp += val;
		if(up.size() > K/2){
			ll moving = *up.begin();
			low.insert(moving); sLow += moving;
			up.erase(up.find(moving)); sUp -= moving;
		}
	}
	else{
		low.insert(val); sLow += val;
		if(low.size() > (K + 1)/2){
			ll moving = *low.rbegin();
			up.insert(*low.rbegin()); sUp += moving;
			low.erase(low.find(*low.rbegin())); sLow -= moving;
		}
	}
}

void er(ll val){
	if(up.find(val) != up.end()) up.erase(up.find(val)), sUp -= val;
	else low.erase(low.find(val)), sLow -= val;
	if(low.empty()){
		ll moving = *up.begin();
		low.insert(*up.begin()); sLow += moving;
		up.erase(up.find(*up.begin())); sUp -= moving;
	}
}

ll med(){ return (K%2 == 0) ? 0 : (*low.rbegin()); }

int main() {
	cin >> N >> K;
	for(ll i = 0; i < N; i++) cin >> arr[i];
	low.insert(arr[0]); sLow += arr[0];
	for(ll i = 1; i < K; i++) ins(arr[i]);
	cout << sUp - sLow + med(); if(N!=1) cout << " ";
	for(ll i = K; i < N; i++){
		if(K == 1){
			ins(arr[i]);
			er(arr[i - K]);
		}
		else{
			er(arr[i - K]);
			ins(arr[i]);
		}
		cout << sUp - sLow + med(); if(i != N -1) cout << " ";
	}
	cout << endl;
}
```
{% endtab %}

{% tab title="MaxSubarrSum II" %}
```cpp
int n,a,b;
cin>>n>>a>>b;
vector<ll> prefixsum(n+1);
prefixsum[0] = 0;
for(int i=1;i<=n;i++){
    int x;
    cin>>x;
    prefixsum[i] = prefixsum[i-1] + x;
}
multiset<ll> curr;
ll ans = -2e18;
for(int i=a;i<=n;i++){
    if(i>b){
        curr.erase(curr.find(prefixsum[i-b-1]));
    }
    curr.insert(prefixsum[i-a]);
    ans = max(ans, prefixsum[i] - *curr.begin());
}
cout<<ans<<"\n";
```
{% endtab %}

{% tab title="315" %}
```python
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedlist = SortedList([]) # To maintain the sorted list on go and also have O(logN) insert and bisect.
        result = []
        for num in nums[::-1]:
            idx = sortedlist.bisect_left(num) # bisect to find where the current number should insert
            result.append(idx) # this gives the lesser numbers on the left
            sortedlist.add(num) # then update the sorted list 
        return result[::-1]
'''
if not SortedList, there are other(& more tricky ways) too:
    1.Merge Sort
    2.BST
    3. Index/AVL Tree
'''
```
{% endtab %}

{% tab title="1347" %}
```python
from collections import Counter

def f(s,t):
    sc = Counter(list(s))
    
    for c in t:
        if c in sc.keys():
            sc[c] -= 1
        else:
            sc[c] = -1
    res = 0
    for _, v in sc.items():
        if v < 0:
            res += abs(v)
    return res
        
print(f("bab","aba"))           #``
print(f("leetcode","practice")) #5
```
{% endtab %}
{% endtabs %}

###

* [x] LC 388. [Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/) |\*\* @google\*\*
* [ ] ...

{% tabs %}
{% tab title="388" %}
The number of tabs is my depth and for each depth I store the current path length.

```python
def lengthLongestPath(input):
    pathlen = {0:0}
    maxlen = 0
    
    for line in input.split('\n'):
        name = line.lstrip('\t')
        depth = len(line)-len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth+1] = pathlen[depth] + len(name) + 1
    
    return maxlen

lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdirrr2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

"""
line :  dir
line :          subdir1
line :                  file1.ext
line :                  subsubdir1
line :          subdirrr2
line :                  subsubdir2
line :                          file2.ext
"""
```

#### #2: Stack Based

```python
class Solution(object):
    def TabNum(self, s):
        n = 0
        for char in s:
            if char == '\t':
                n += 1
            if char == '.':
                return n, True
        return n, False
    
    def lengthLongestPath(self, input):
        stack, longest = [], 0
        input = input.split("\n")
        accumulated = 0
        
        for char in input:
            tab, isFile = self.TabNum(char)
            while stack and len(stack) != tab:
                accumulated -= stack[-1]
                stack.pop()
            stack.append(len(char) - tab)
            accumulated += len(char) - tab
            if isFile:
                longest = max(longest, accumulated + len(stack) - 1)
        
        return longest
```
{% endtab %}
{% endtabs %}



## 2. Heap

### 2.0 Notes

* **Complexity** with Heap(of size K) :` O(nlogK)` // while with sort it'll be `O(nlogn)`
* \*\*NOTE: \*\*if sorting is the only better way & asked to **do better than `O(nlogn)`** , heap is the way!
* \*\*How to identify \*\*if its a heap question? look for this keyword: `smallest/largest K elements`
* Which heap to choose when:(hint: _opposite_, logic: we can pop the top element but not the bottom)
  * if **smallest K** elements => use **max heap**
  * if\*\* largest K **elements => use** min heap\*\*

### 2.1 Standard Problems

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

### 2.2 Rest of the Problems

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

faf
