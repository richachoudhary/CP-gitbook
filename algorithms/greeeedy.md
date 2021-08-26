# Greeeedy

## 1. List & String

* [x] [1021.Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
* [x] [443.String Compression](https://leetcode.com/problems/string-compression/)
* [x] [1520.Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) 🍪🍪🍪
* [x] LC: [8.String to Integer \(atoi\)](https://leetcode.com/problems/string-to-integer-atoi/)
* [x] CSES: [Palindrome Reorder](https://cses.fi/problemset/task/1755)
* [x] **TYPE: Count \# Inversions** ✅
  * [x] CSES: [Collecting Numbers](https://cses.fi/problemset/task/2216)  \| [Approach](https://discuss.codechef.com/t/cses-collecting-numbers/83775)
  * [x] CSES: [Collecting Numbers II](https://cses.fi/problemset/task/2217) \|  [Video](https://www.youtube.com/watch?v=LEL3HW4dQew&ab_channel=ARSLONGAVITABREVIS) 🐽
* [x] CSES: [Subarray Sum 1](https://cses.fi/problemset/task/1660/) \| only "prefix sum"
* [x] CSES: [Subarray Sum 2](https://cses.fi/problemset/task/1661) \| neg numbers \| prefix sum + map
* [x] CSES: [Subarray Divisibility](https://cses.fi/problemset/result/2648945/) \| ✅ 
* [x] LC 44: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
* [x] LC [163. Missing Ranges](https://leetfree.com/problems/missing-ranges)
* [x] LC [179.Largest Number](https://leetcode.com/problems/largest-number/) 🐽
* [x] LC [41.First Missing Positive](https://leetcode.com/problems/first-missing-positive/) ✅🍪🍪🍪
* [x] LC [14.Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) ✅\| kaafi clever
* [x] LC [334.Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) \| **O\(N\)**
* [x] LC [68. Text Justification](https://leetcode.com/problems/text-justification/) 💪🔴
  * Asked in Coinbase **Karat Test** \| multiple times
  * so many corner cases; impossible to solve in interview
  * Built upon \[EASY\] [1592.Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) ✅💪

{% tabs %}
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

## 2. Hashing

### 2.1 Rolling Hash

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained)
* [ ] [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath) 



## 3. Map \| Set \| SortedList

### 3.1 Problems

* [x] LC [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) ✅🌇\| uses **SortedList** 
* [x] LC[ 146. LRU Cache](https://leetcode.com/problems/lru-cache/) ✅✅✅
* [x] [1700.Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
* [x] CSES: [Sliding Medium](https://cses.fi/problemset/task/1076) \| LC: [480 Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)  ✅✅⭐️🚀 // `O(logK)` **NOTE: Dont skip w/o doing it!!!!!!!**
  * Video: [link](https://www.youtube.com/watch?v=UGs_kQxJNPk&ab_channel=ARSLONGAVITABREVIS)
* [x] CSES: [Sliding Cost](https://cses.fi/problemset/task/1077/) \| very similar to Sliding Medium; jst keep two sums: `upperSum` & `lowerSum`
* [x] CSES: [Maximum Subarray Sum II](https://cses.fi/problemset/task/1644/) \| idea [here](https://discuss.codechef.com/t/help-with-maximum-subarray-sum-ii-from-cses/73404) 🐽
* [x] LC [315.Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) 🍪🍪🍪\| **SortedList \|** BST \| MergeSort

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

{% tab title="SlidingMedium" %}
```cpp
multiset<int> lo,hi;
int k;
void rebalance(){
    if(k&1){
        while(lo.size() < k/2 + 1){
            int t = *(hi.begin());
            hi.erase(hi.begin());
            lo.insert(t);
        }
        while(lo.size()> k/2 + 1){
            int t = *(lo.rbegin());
            lo.erase(lo.find(t));
            hi.insert(t);
        }
    }else{
        while(lo.size() < k/2){
            int t = *(hi.begin());
            hi.erase(hi.begin());
            lo.insert(t);
        }
        while(lo.size()> k/2){
            int t = *(lo.rbegin());
            lo.erase(lo.find(t));
            hi.insert(t);
        }
    }
}

void ins(int x){
    if(x < *(lo.rbegin())){
        lo.insert(x);
    }else{
        hi.insert(x);
    }
    rebalance();
}

void rem(int x){
    if(lo.find(x) != lo.end()){
        lo.erase(lo.find(x));
    }else{
        hi.erase(hi.find(x));
    }
    rebalance();
}

vector<double> medianSlidingWindow(vector<int>& a, int K) {
    vector<double>res;
    k = K;
    int n = a.size();
    //special case
    if(k==1){
        return a;
    }
    
    //first window
    lo.insert(a[0]);
    for(int i=1;i<k;i++){
        ins(a[i]);
    }
    if(k&1){
        res.push_back(double(*lo.rbegin()));
    }else{
        double x = (double(*lo.rbegin()) + double(*hi.begin()))/2;
        res.push_back(x);
    }
    
    //next windows after first
    for(int i=k;i<n;i++){
        if(k==1){           //special case(not reqd now, already handled @line51)
            ins(a[i]);
            rem(a[i-k]);
        }else{
            rem(a[i-k]);
            ins(a[i]);
        }
        if(k&1){
            res.push_back(double(*lo.rbegin()));
        }else{
            double x = (double(*lo.rbegin()) + double(*hi.begin()))/2;
            res.push_back(x);
        }
    }
    return res;
}
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
{% endtabs %}





## 4. Queue/Stack/Monotonic

### 4.0 Notes:

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

### 4.1 Standard Questions

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
* [ ] LC239. Sliding Window Maximum
* [ ] LC739. Daily Temperatures
* [ ] LC862. Shortest Subarray with Sum at Least K
* [ ] LC907. Sum of Subarray Minimums
* [x] [1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

### 4.2 Rest of the problems

* [x] [391. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
* [x] [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) \|  for circular array 🚀
* [ ] [556.Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) 🍪🍪🍪
* [x] [155. Min Stack](https://leetcode.com/problems/min-stack/) : instead of 2 stacks, use single stack & insert pairs in it: `ele,min_ele`
  * Regular approach of `O(1)` =&gt; [Aditya Verma](https://www.youtube.com/watch?v=ZvaRHYYI0-4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=11&ab_channel=AdityaVerma)
* [x] [1441.Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/)

### 4.3 Resources

* [Aditya Verma's Playlist](https://www.youtube.com/watch?v=P1bAPZg5uaE&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&ab_channel=AdityaVerma)

## 5. Heap

### 5.0 Notes

* **Complexity** with Heap\(of size K\) : `O(nlogK)` // while with sort it'll be `O(nlogn)`
* **NOTE:** if sorting is the only better way & asked to **do better than `O(nlogn)`** , heap is the way!
* **How to identify** if its a heap question? look for this keyword: `smallest/largest K elements`
* Which heap to choose when:\(hint: _opposite_, logic: we can pop the top element but not the bottom\) 
  * if **smallest K** elements   =&gt; use **max heap**
  * if **largest K**  elements     =&gt; use **min heap**

### 5.1 Standard Problems

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
* [x] [1337.The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)
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
* [x] [LC \#480](https://leetcode.com/problems/sliding-window-median/) - Sliding window Median
* [ ] [LC \#502](https://leetcode.com/problems/ipo/) - Maximize Capital/IPO

**Minimum number Pattern**

* [ ] [LC \#1167](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) - Minimum Cost to connect sticks/ropes
* [ ] [LC \#253](https://leetcode.com/problems/meeting-rooms-ii) - Meeting Rooms II
* [ ] [LC \#759](https://leetcode.com/problems/employee-free-time) - Employee free time
* [ ] [LC \#857](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) - Minimumcost to hire K workers
* [ ] [LC \#621](https://leetcode.com/problems/task-scheduler/) - Minimum number of CPU \(Task scheduler\)
* [ ] [LC \#871](https://leetcode.com/problems/minimum-number-of-refueling-stops/) - Minimum number of Refueling stops

### 5.2 Rest of the Problems

* [x] [1046.Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
* [x] CSES: [Josephus Problem I](https://cses.fi/problemset/task/2162)

{% tabs %}
{% tab title="Josephus I" %}
```python
n = int(input())
d = deque([i for i in range(1,n+1)])

while d:
    x = d.popleft()
    d.append(x)
    print(d.popleft())
```
{% endtab %}
{% endtabs %}

## 6.Sort

* [x] CSES: [Stick Lengths](https://cses.fi/problemset/result/2583535/)✅ \| standard problem \|use **MEDIAN** not **MEAN**
* [x] CSES: [Traffic Lights](https://cses.fi/problemset/task/1163) : 🐽🐽✅✅ \| [Youtube](ttps://www.youtube.com/watch?v=4HKXdh_LHps&ab_channel=ARSLONGAVITABREVIS) \| [Stackoverflow](https://stackoverflow.com/questions/63329220/i-tried-solving-traffic-lights-problem-in-the-cses-problem-set-my-approach-seem)
* [x] CSES: [Room Allocation](https://cses.fi/problemset/task/1164) ✅ \| LC: [1942.The Number of the Smallest Unoccupied Chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/discuss/1360146/python-heap-easy-implementation-faster-than-100) -&gt; my first editorial!!
* [x] CSES: [Reading Books](https://cses.fi/problemset/task/1631) \| [why max\(sum,2\*last\_ele\) works](https://codeforces.com/blog/entry/79238)

{% tabs %}
{% tab title="Traffic Lights" %}
```python
# ======================== NOOB: O(N*N(logN))
segments = [0,x]
for t in trafficLights:
    segments.append(t)
    segments.sort()
    res =0
    for i in range(len(segments)-1):
        res = max(res,segments[i+1]-segments[i])
    print(res)

# 2. ====================== Using multiset+bin_serach: O(NlogN)

street = [0,x]
lights = Counter()    # MULTISET as deletion in lists take O(N) & for dict its O(1)
lights[x] = 1

for t in trafficLights:
    r = bisect.bisect_right(street,t)
    l = r-1
    lights[(street[r]-street[l])] -= 1   # O(1)
    if lights[(street[r]-street[l])] == 0:
        lights.pop((street[r]-street[l]))
    # add new lights
    lights[(street[r]-t)] += 1
    lights[(t-street[l])] += 1

    street.insert(r,t) #insert new light
    print('\t\t ', street)
# YOUTUBE: https://www.youtube.com/watch?v=4HKXdh_LHps&ab_channel=ARSLONGAVITABREVIS
# CODE: https://stackoverflow.com/questions/63329220/i-tried-solving-traffic-lights-problem-in-the-cses-problem-set-my-approach-seem

```
{% endtab %}

{% tab title="Room Allocation" %}
```cpp
/*
CANT DO WITH PYTHON: AS #NOTE.
#NOTE: free rooms: ordered container with O(logN) addition/removal => set
if checkin:
    if no room free : assign new
    if any room/s free: assing lowest free & mark that room as not-free
if checkout:
    mark his room as free
*/
int n;cin>>n;
vector<pair<int,pair<int,int> > > guests;
for(int i=0;i<n;i++){
    int x,y;
    cin >> x >> y;
    guests.push_back(make_pair(x,make_pair(-1,i)));
    guests.push_back(make_pair(y,make_pair(1,i)));
}
vector<int>res(n,0);
sort(guests.begin(),guests.end());
set<int>frees;

int max_room = 1;
for(int i=0;i<2*n;i++){
    int t = guests[i].first, op = guests[i].second.first, idx = guests[i].second.second;
    if(op == -1){    //check-in
        if(frees.size() == 0){
            res[idx] = max_room;
            max_room++;
        }else{
            res[idx] = *frees.begin();
            frees.erase(frees.begin());
        }
    }else{          //check-out
        frees.insert(res[idx]);
    }
}

cout<<max_room-1<<endl;
for(int i=0;i<n;i++){
    cout<<res[i]<<" ";
}
```
{% endtab %}
{% endtabs %}

## 7.Binary Search

### 7.0 Notes

### 7.1 Problems

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained) =&gt; **Rolling Hash/Rabin Karp**
* [ ] [658.Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) \| [Soln](https://leetcode.com/problems/find-k-closest-elements/discuss/915047/Finally-I-understand-it-and-so-can-you.)
* [x] CSES:[ Digit Queries](https://cses.fi/problemset/result/2573072/) \| s[oln video](https://www.youtube.com/watch?v=QAcH8qD9Pe0&ab_channel=ARSLONGAVITABREVIS) ✅✅🐽
* [x] CSES: [Concert Tickets](https://cses.fi/problemset/task/1091) \| [WilliamLin](https://www.youtube.com/watch?v=dZ_6MS14Mg4&t=3436s&ab_channel=WilliamLin)✅⭐️⭐️✅ \| **Kuch naya sikha ke gya ye Q**
* [x] LC: **4.** [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) 🐽🐽✅
* [x] LC 33: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) ☑️
* [x] LC [34.Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ✅
* [x] LC [162.Find Peak Element](https://leetcode.com/problems/find-peak-element/) \| ⭐️🤯✅

{% tabs %}
{% tab title="Concert Tickets:: CPP" %}
```cpp
multiset<int> tickets;
cin >> n >> m;
for (int i=0;i<n;++i){
	cin >> h; tickets.insert(h);
}
for (int i=0;i<m;++i){
	cin >> t;
	auto it = tickets.upper_bound(t);
	if (it==tickets.begin()){
		cout << -1 << "\n";
	}
	else{
		cout << *(--it) << "\n";
		tickets.erase(it);
	}
}
```
{% endtab %}

{% tab title="CounterTickets:: py TLE" %}
```python
# 1. ================ TLE: O(NlogN)
A = list(I())  
A.sort()

for e in I():  
    i = bisect.bisect_right(A,e)
    if i == 0:
        print('-1')
    else:
        print(A[i-1])
        A.pop(i-1)  # COSTLY Operation: Adds extra O(N)

# 2. ================== O(logN) :: use multiset (not 'set' because of duplication)
'''
    NOTE: there is no O(logN) seach based multiset data structure in python : https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint
    i.e. with python you cant implement m.lower_bound() for a multimap 'm'
'''
A = list(I())  
A.sort()
print('\n',A)
freq = Counter(A)

for e in I():  
    i = bisect.bisect_right(A,e)
    if i > 0 and freq[A[i-1]] > 0:
        print(A[i-1])
        freq[A[i-1]] -= 1
    else:
        print('-1')
```
{% endtab %}

{% tab title="4." %}
```python
def findMedianSortedArrays(self, nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2:  # the length is odd
        return self.findKthSmallest(nums1, nums2, l//2+1)
    else:
        return (self.findKthSmallest(nums1, nums2, l//2) +
        self.findKthSmallest(nums1, nums2, l//2+1))*0.5

def findKthSmallest(self, nums1, nums2, k):
    # force nums1 is not longer than nums2
    if len(nums1) > len(nums2):
        return self.findKthSmallest(nums2, nums1, k)
    if not nums1:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    pa = min(int(k/2), len(nums1)); pb = k-pa  # take care here
    if nums1[pa-1] <= nums2[pb-1]:
        return self.findKthSmallest(nums1[pa:], nums2, k-pa)
    else:
        return self.findKthSmallest(nums1, nums2[pb:], k-pb)
```
{% endtab %}

{% tab title="33✅" %}
```python
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
```
{% endtab %}

{% tab title="34." %}
```python
def searchRange(self, nums: List[int], target: int) -> List[int]:
    start = 0; end = len(nums)-1
    while start <= end:
        mid = (start+end) // 2
        if nums[start] == nums[end] == target:
            return [start, end]
        if nums[mid] < target:
            start = mid+1
        elif nums[mid] > target:
            end = mid-1
        else:
            if nums[start] != target: start += 1
            if nums[end] != target: end -= 1
    return [-1,-1]
```
{% endtab %}

{% tab title="162.🤯" %}
```python
def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right

'''
    Basic Idea: Binary search

Elaboration: 
 if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either 
   1. always increasing  -> the right-most element is the peak
   2. always decreasing  -> the left-most element is the peak
   3. first increasing then decreasing -> the pivot point is the peak
   4. first decreasing then increasing -> the left-most element is the peak  

   Therefore, we can find the peak only on its right elements( cut the array to half)

   The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.

'''
```
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
**NOTE**: there is no O\(logN\) search based multiset data structure in python : [https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint](https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint) 

i.e. with python you cant implement m.lower\_bound\(\) for a multimap 'm'. \(closest D.S. to multiset is **collections.Counter\)**  
So for this question, you **HAVE TO GO WITH C++** 

**\(**cant use Counters either, because of case: when just prev elemnent has freq = 0 & you've to keep searching back for prev lowest ele\)
{% endhint %}

### 7.2 Linear Function based problems \(find min x for f\(x\)\)

* [x] CSES: [Factory Machines ](https://cses.fi/problemset/task/1620)✅
* [x] CSES: [Array Division](https://cses.fi/problemset/task/1085/) ✅✅

{% tabs %}
{% tab title="FactoryMachines" %}
```python
lb, ub = 0,10**18
ans = 0
while lb<=ub:
    mid = (lb+ub)//2
    summ = 0
    print(f'lb = {lb} , mid = {mid} , ub = {ub}')
    for e in A:
        summ += mid//e
        if summ >= t:
            break
    print(f'\t summ = {summ}')
    if summ >= t:
        ans = mid
        ub = mid-1
    else:
        lb = mid+1
print(ans)
```
{% endtab %}

{% tab title="Array Division" %}
```python
n,k = I()
A = list(I())

lo,hi = max(A), sum(A)
while lo<hi:
    mid = (lo+hi)//2
    cnt = 0
    curr = 0
    for e in A:
        if curr+e > mid:
            cnt += 1
            curr = 0
        curr += e
        
    cnt += 1    # count the last segment
    if cnt > k:
        lo = mid+1
    else:
        hi = mid
print(lo)
```
{% endtab %}
{% endtabs %}

[Aditya Verma playlist](https://www.youtube.com/watch?v=j7NodO9HIbk&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&ab_channel=AdityaVerma)

## 8.Two Pointers

* [x] **CSES:** [Apartments](https://cses.fi/problemset/task/1084) ⭐️💪
* [x] CSES: [Ferris Wheel](https://cses.fi/problemset/task/1090) 
* [x] CSES: [Subarray Distinct Values](https://cses.fi/problemset/result/2649112/)

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

{% tab title="239." %}
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

* [x] CSES: [Playlist](https://cses.fi/problemset/task/1141)
* [x] [560.Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)✅
  * **NOTE:** Sliding window technique works only for all positive/all negative \(i.e. not for arr with both pos & neg numbers\).So soln\#1 below gets WA
* [x] GfG\#1: [Longest substring with k unique characters](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/) ❤️
  * [x] SIMILAR: [904.Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/submissions/)
* [x] [424.Longest Repeating Character Replacement ](https://leetcode.com/problems/longest-repeating-character-replacement/)\(similar to \#1\) 🚀🚀

{% tabs %}
{% tab title="Playlist" %}
```python
n= int(input())
A = list(map(int,input().split()))

res = 0
l = 0
s = set()
s.add(A[0])
for r in range(1,n):
    while l<r and A[r] in s:
        s.remove(A[l])
        l += 1
    s.add(A[r])
    res = max(res, r-l+1)
print(res)
```
{% endtab %}

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

* [x] CSES: [Movie Festival](https://cses.fi/problemset/task/1629)
* [x] CSES: [Movei Festival II](https://cses.fi/problemset/task/1632) ✅
* [x] CSES: [Restaurant Customers](https://cses.fi/problemset/task/1619)

{% tabs %}
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

