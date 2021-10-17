# Heap | Map-Set | SortedContainer

## 1. Map-set Problems

* [x] LC [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) ✅🌇| uses \*\*SortedList \*\*
* [x] LC[ 146. LRU Cache](https://leetcode.com/problems/lru-cache/) ✅✅✅
* [x] [1700.Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
* [x] LC: [480 Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) ✅✅⭐️🚀 // `O(logK)` **NOTE: Dont skip w/o doing it!!!!!!!**
  * Video: [link](https://www.youtube.com/watch?v=UGs_kQxJNPk\&ab_channel=ARSLONGAVITABREVIS)
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
