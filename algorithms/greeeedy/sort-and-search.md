# Sort & Search



## 1.Sort

* [x] Learn Quicksort for LC [973.K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | [O(N) quicksort approach](https://leetcode.com/problems/k-closest-points-to-origin/discuss/219442/Python-with-quicksort-algorithm) | **@uber**
  * Sort OR Heap se koi bhi kar lega, koi na poorch rha interview mei ye approach!!!
* [x] CSES: [Stick Lengths](https://cses.fi/problemset/result/2583535/)✅ | standard problem |use **MEDIAN** not **MEAN**
* [x] CSES: [Traffic Lights](https://cses.fi/problemset/task/1163) : 🐽🐽✅✅ | [Youtube](ttps://www.youtube.com/watch?v=4HKXdh_LHps\&ab_channel=ARSLONGAVITABREVIS) | [Stackoverflow](https://stackoverflow.com/questions/63329220/i-tried-solving-traffic-lights-problem-in-the-cses-problem-set-my-approach-seem)
* [x] CSES: [Room Allocation](https://cses.fi/problemset/task/1164) ✅ | LC: [1942.The Number of the Smallest Unoccupied Chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/discuss/1360146/python-heap-easy-implementation-faster-than-100) -> my first editorial!!
* [x] CSES: [Reading Books](https://cses.fi/problemset/task/1631) | [why max(sum,2\*last_ele) works](https://codeforces.com/blog/entry/79238)
* [x] [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | Bucket sort strategy
* [x] LC 406. [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

{% tabs %}
{% tab title="973.QuickSortBased" %}
```python
'''
Time complexity is O(N^2) worst case. (come up with Quick sort)

But In average, we can reach in logN times and don't need to sort all elements at every step.

It looks like N + N/2 + N/4 + N/8 + .... OK?
Because of N + N/2 + N/4 + N/8 + .... < 2N 
        so average time complexity would O(2N) => O(N)

'''

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

{% tab title="220." %}
```python
def solve(A, k, t):
    d = dict()
    
    for i in range(len(A)):
        bucket = A[i]//(t+1)
        # check in bucekt, bucekt-1, bucekt+1
        # 1. check in same bucket
        if bucket in d and abs(d[bucket] - A[i])<= t:
            return True
        # 2. check in JUST prev bucket
        if bucket-1 in d and abs(d[bucket-1] - A[i])<= t:
            return True
        # 2. check in JUST next bucket
        if bucket+1 in d and abs(d[bucket+1] - A[i])<= t:
            return True
        
        d[bucket] = A[i]    # put A[i] into its bucket
        if i>=k:
            del d[A[i-k]//(t+1)]
    return False
```
{% endtab %}

{% tab title="406" %}


1. **Pick out tallest group of people and sort them** in a subarray (S). Since there's no other groups of people taller than them, therefore **each guy's index will be just as same as his k value**.
2. For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.

E.g.\
input: \[\[7,0], \[4,4], \[7,1], \[5,0], \[6,1], \[5,2]]\
subarray after step 1: \[**\[7,0], \[7,1]**]\
subarray after step 2: \[\[7,0], **\[6,1]**, \[7,1]]\
...



```python
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x: (-x[0],x[1]))

    res = []
    for p in people:
        res.insert(p[1],p)
    return res
```
{% endtab %}
{% endtabs %}

## 2.Binary Search 🌟

### 1.0 Notes

* [**\*\* greatest template\*\***](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)** ever!!!!**
* Generalized template ( **works all the time**) :: fucking moonshot!!!
  * Remember this: **after exiting the while loop, `left` is the minimal k​ satisfying the `condition` function**;

{% tabs %}
{% tab title="Binary Search Template" %}
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
{% endtab %}
{% endtabs %}

### 2.1 Problems based on Template

* [x] [**278. First Bad Version \[Easy\]**](https://leetcode.com/problems/first-bad-version/)
* [x] [**69. Sqrt(x) \[Easy\]**](https://leetcode.com/problems/sqrtx/)
* [x] [**35. Search Insert Position \[Easy\]**](https://leetcode.com/problems/search-insert-position/)

{% tabs %}
{% tab title="278" %}
```python
def firstBadVersion(self, n):
    l,r = 1, n
    while l<r:
        mid = (l+r)//2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}

{% tab title="69" %}
```python
def mySqrt(self, n: int) -> int:
    if n == 0 or n == 1:
        return n
    l,r = 0, n+1
    while l<r:
        mid = (l+r)//2
        if mid*mid > n:
            r = mid
        else:
            l = mid+1
    return l-1
    
    '''
    set right = n + 1 instead of right = n to deal with 
    special input cases like n = 0 and n = 1
    '''
```
{% endtab %}

{% tab title="35" %}
```python
def searchInsert(self, nums: List[int], target: int) -> int:
        
    return bisect.bisect_left(nums,target)
    
    # =====================================
    n = len(nums)
    l,r = 0, n
    while l<r:
        mid = (l+r)//2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}
{% endtabs %}

* [x] [**1011. Capacity To Ship Packages Within D Days \[Medium\]**](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)** ✅**
* [x] \*\*[**410. Split Array Largest Sum \[Hard\]**](https://leetcode.com/problems/split-array-largest-sum/) \*\*// ditto same as `1011`
* [x] [**875. Koko Eating Bananas \[Medium\]**](https://leetcode.com/problems/koko-eating-bananas/)
* [x] [**1482. Minimum Number of Days to Make m Bouquets \[Medium\]**](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
* [x] [**475. Heaters \[Medium\]**](https://leetcode.com/problems/heaters/)** ✅💪**
* [x] **Spoj**: [Aggressive Cows](https://www.spoj.com/problems/AGGRCOW/) | @curefit 💪| khud se kiya poora😎!

{% tabs %}
{% tab title="1011" %}
```python
def shipWithinDays(self, W: List[int], k: int) -> int:
    def is_feasible(x):
        days = 1
        total = 0
        for w in W:
            total += w
            if total > x:   # too heavy, wait for next day
                total = w
                days += 1
        return days <= k
    
    l, r = max(W), sum(W)        # initialization pe GAUR farmayein
    
    while l<r:
        mid = (l+r)//2
        if is_feasible(mid):
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}

{% tab title="410" %}
```python
def splitArray(self, nums: List[int], m: int) -> int:
    def feasible(threshold) -> bool:
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                total = num
                count += 1
                if count > m:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid     
        else:
            left = mid + 1
    return left
```
{% endtab %}

{% tab title="875" %}
```python
def minEatingSpeed(self, A: List[int], H: int) -> int:
        
    def is_feasible(k):
        hrs = 0
        for x in A:
            hrs += math.ceil(x/k)
        return hrs <= H
        # return sum((a-1)//k + 1 for a in A)   # raster!!
    
    l,r = 1, max(A)
    while l<r:
        mid = (l+r)//2
        if is_feasible(mid):
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}

{% tab title="1482" %}
```python
def minDays(self, A: List[int], m: int, k: int) -> int:
        
    def is_feasible(x):
        cnt = 0
        curr_flowers = 0
        for i in range(len(A)):
            if A[i] <= x:
                cnt += (curr_flowers + 1)//k
                curr_flowers = (curr_flowers + 1)%k
            else: 
                curr_flowers = 0
            '''
            # Below fails for case: [x, x, x, x, _, x, x] , m = 2, k = 3. ==> we can form 2 bouquets(not 1) from first 3 flowers
            if A[i] <= x:    # has bloomed
                curr_flowers += 1
                if curr_flowers >= k:
                    cnt += 1
            else:
                curr_flowers = 0
            '''
        return cnt >= m
    
    # BC:
    if len(A) < m*k:
        return -1
    
    l,r = 1, max(A)
    while l<r:
        mid = (l+r)//2
        if is_feasible(mid):
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}

{% tab title="475" %}
```python
def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
    def is_feasible(r):
        j = 0
        for h in houses:
            if heaters[j] - r <= h <= heaters[j] + r:
                continue
            else:
                while j < m and h > heaters[j] + r:
                    j += 1
                if j == m or h < heaters[j] - r:
                    return False
        return True
    
    heaters.sort()
    houses.sort()
    n, m = len(houses), len(heaters)
    
    l,r = 0,(10**9)+1
    while l<r:
        mid = (l+r)//2
        if is_feasible(mid):
            r = mid
        else:
            l = mid+1
    return l
```
{% endtab %}

{% tab title="AggressiveCows" %}
```python
def is_possible(a,gap,c):
    prev = 0
    c -= 1  # place cow#1 @idx = 0
    for curr in range(1,len(a)):
        if a[curr]-a[prev] >= gap:
            c -= 1
            prev = curr
    return c == 0

T = int(input())

for _ in range(T):
    n,c = I()
    stalls = []
    for _ in range(n):
        x = int(input())
        stalls.append(x)
    
    stalls.sort()
    l,r = 0,stalls[-1]-stalls[0]
    ans = 0
    while l <r:
        mid = (l+r)//2
        if is_possible(stalls,mid,c):
            l = mid+1   # swapped because we've to find 'largest possible value' here
            ans = mid
        else:
            r = mid
    print(ans)


"""

1 2     4       8  9
x       x          x
"""
```
{% endtab %}
{% endtabs %}

* [x] \*\*\*\*[**287: Find the Duplicate Number**](https://leetcode.com/problems/find-the-duplicate-number/) | **@ShareChat** | also see in `LinkedLIst` 💪
* [x] [**1201. Ugly Number III \[Medium\]**](https://leetcode.com/problems/ugly-number-iii/)\*\* ✅✅ | \*\*weird GCD formula
* [ ] [**668. Kth Smallest Number in Multiplication Table \[Hard\]**](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/)
* [ ] [**719. Find K-th Smallest Pair Distance \[Hard\]**](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)
* [ ] [**1283. Find the Smallest Divisor Given a Threshold \[Medium\]**](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)
* [x] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)\*\* | `RabinKarp`\*\*

{% tabs %}
{% tab title="287.💪" %}
```python
'''
array size is n + 1while the value in array is from 1 to n
Apply binary search to pick a number m within 1 to n,
count how many numbers in the array is less or equal to m
If the count > m , then m is too large or m is the answer, so right = m
If count <= m, then m is too small, so left = m + 1
Time: O(nlogn)
Space: O(1)
'''

n = len(nums)
l,r = 1,n-1
while l<r:
    mid = (l+r)//2
    cnt = sum(x<=mid for x in nums)
    
    if cnt > mid:
        r = mid
    else:
        l = mid+1
return l
```
{% endtab %}

{% tab title="1201" %}
```python
def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
    # Since a might be a multiple of b or c, 
    # OR the other way round, we need the help of greatest common divisor
    # to avoid counting duplicate numbers.
    def enough(num) -> bool:
        total = num//a + num//b + num//c - num//ab - num//ac - num//bc + num//abc
        return total >= n

    ab = a * b // math.gcd(a, b)
    ac = a * c // math.gcd(a, c)
    bc = b * c // math.gcd(b, c)
    abc = a * bc // math.gcd(a, bc)
    left, right = 1, 10 ** 10
    while left < right:
        mid = left + (right - left) // 2
        if enough(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
{% endtab %}

{% tab title="1044." %}
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

***

### 2.2 Modified  Binary Search Problems

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o\(n-log-n\)-explained) => **Rolling Hash/Rabin Karp**
* [ ] [658.Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | [Soln](https://leetcode.com/problems/find-k-closest-elements/discuss/915047/Finally-I-understand-it-and-so-can-you.)
* [x] CSES:[ Digit Queries](https://cses.fi/problemset/result/2573072/) | s[oln video](https://www.youtube.com/watch?v=QAcH8qD9Pe0\&ab_channel=ARSLONGAVITABREVIS) ✅✅🐽
* [x] CSES: [Concert Tickets](https://cses.fi/problemset/task/1091) | [WilliamLin](https://www.youtube.com/watch?v=dZ\_6MS14Mg4\&t=3436s\&ab_channel=WilliamLin)✅⭐️⭐️✅ | **Kuch naya sikha ke gya ye Q**
* [x] LC: \*\*4. \*\*[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) 🐽🐽✅
* [x] LC 33: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) ☑️
* [x] LC [34.Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ✅

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
{% endtabs %}



* [x] LC [162.Find Peak Element](https://leetcode.com/problems/find-peak-element/) | ⭐️🤯✅| **@google**
* [x] ..

{% tabs %}
{% tab title="162🤯" %}
![the three cases](<../../.gitbook/assets/Screenshot 2021-10-18 at 1.50.38 AM.png>)

above solution [link](https://leetcode.com/problems/find-peak-element/discuss/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search)

```python
def findPeakElement(self, nums):
    n = len(nums)
    if n == 1: return 0 # single element

    # check if 0th/n-1th index is the peak element
    if nums[0] > nums[1]: return 0
    if nums[n-1] > nums[n-2] : return n-1

    # search in the remaining array
    left = 1
    right = n-2

    while left <= right:
        mid = (left+right)//2

        # if mid == peak ( case 2 )
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid

        # downward slope and search space left side ( case 1)
        elif nums[mid] < nums[mid-1]: right = mid - 1

        #  upward slope and search space right side ( case 3 )
        elif nums[mid] < nums[mid+1]: left = mid + 1

    return -1   # dummy return statement
```
{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}







{% hint style="danger" %}
**NOTE**: there is no O(logN) search based multiset data structure in python : [https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint](https://stackoverflow.com/questions/17346905/is-there-a-python-equivalent-for-c-multisetint)

i.e. with python you cant implement m.lower_bound() for a multimap 'm'. (closest D.S. to multiset is **collections.Counter)**\
\*\*\*\*So for this question, you \*\*HAVE TO GO WITH C++ \*\*

\*\*(\*\*cant use Counters either, because of case: when just prev elemnent has freq = 0 & you've to keep searching back for prev lowest ele)
{% endhint %}
