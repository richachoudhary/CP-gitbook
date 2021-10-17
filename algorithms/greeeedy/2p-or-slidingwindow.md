# 2P | SlidingWindow

## 1.Two Pointers

* [x] \*\*CSES: \*\*[Subarray Sums I](https://cses.fi/problemset/task/1660) 🌟✅ | count the number of subarrays having sum x
* [x] \*\*CSES: \*\*[Apartments](https://cses.fi/problemset/task/1084) ⭐️💪
* [x] CSES: [Ferris Wheel](https://cses.fi/problemset/task/1090)
* [x] CSES: [Subarray Distinct Values](https://cses.fi/problemset/result/2649112/)
* [ ] CF [814 C. An impassioned circulation of affection](https://codeforces.com/problemset/problem/814/C) 🐽🐽
* [ ] LC 345.[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

{% tabs %}
{% tab title="Subarray Sums I🌟" %}
```python
# =================================== 1: Hashmap
n,x = I()
A = list(I())

s = set()
s.add(0)
cnt = 0
curr = 0

for e in A:
    curr += e
    if curr - x in s:
        cnt += 1
    s.add(curr)
print(cnt)
# =================================== 2: Two Pointer
n,x = I()
A = list(I())

ans = 0
l = 0
curr = 0
for i in range(n):
    curr += A[i]
    while curr > x:
        curr -= A[l]
        l += 1
    if curr == x:
        ans += 1
print(ans)
```
{% endtab %}

{% tab title="Apartments" %}
```python
import bisect
 
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
a.sort()
b.sort()
i,j, = 0,0
 
cnt = 0
 
for i in range(n):
    while j<m and b[j]<a[i]-k:
        j += 1
    if j<m and b[j]<=a[i]+k:
        cnt += 1
        j += 1
print(cnt)
 
'''
2Pointer:similar to Policemen Catches Theives
 
b: 30 60 75
a: 45 60 60 80
 
'''
```
{% endtab %}

{% tab title="Ferris Wheel" %}
```python
import bisect
 
def run():
    I = lambda : map(int, input().split())
    n,x = I()
    A = list(I())
    A.sort()
 
    cnt = 0
    l,r = 0, len(A)-1
 
    while l<=r:
        if A[l]+A[r] <= x:
            l += 1
            r -= 1
            cnt += 1
        else:
            cnt += 1
            r -= 1
 
    # if l==r:
    #     cnt += 1
 
    print(cnt)
    
 
if __name__ == "__main__":
    run()
```
{% endtab %}

{% tab title="Subarray Distinct Values" %}
```python
I = lambda : map(int, input().split())
n,k = I()

A = list(I())
d = dict()
res = 0

l = 0
for r in range(n):
    if A[r] in d:
        d[A[r]] += 1
    else:
        d[A[r]] = 1

    while l<r and len(d) > k:
        if d[A[l]] == 1:
            d.pop(A[l])
        else:
            d[A[l]] -= 1
        l += 1
    res += (r-l+1)

print(res) 
```
{% endtab %}

{% tab title="345" %}
```python
def reverseVowels(self, s: str) -> str:
    vow = set(list('aeiouAEIOU'))
    
    l,r = 0, len(s)-1
    s = list(s)        # as strings are immutable
    while l<r:      
        while l<r and s[l] not in vow:
            l += 1
        while l<r and s[r] not in vow:
            r -= 1
        s[l],s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)
```
{% endtab %}
{% endtabs %}

## 2.Sliding Window

* **Fixed Size: How I do it?**
*
  1. Create first window
  2. iterate in array for next window onwards

{% hint style="info" %}
\*\*Dynamic Size: \*\*WHEN DOES SLIDING WINDOW WORK?

ONLY when you're working with all negative or positives or if your input is sorted
{% endhint %}

### 2.1 Fixed Size Window

* [x] GfG#1: [Maximum sum of subarray of size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)
* [x] GfG#2 [First negative integer in every window of size k](https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/#:\~:text=Recommended%3A%20Please%20solve%20it%20on,the%20current%20subarray\(window\).)
* [x] [438.Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) 🚀
* [x] [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) 🍪🍪🍪
* [x] 849\. [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) 🤯🐽| \~\~unable to get the 2P method!!!! \~\~not needed
  * [x] 855.[Exam Room](https://leetcode.com/problems/exam-room/) | design problem based on this | **@Google!!!!!🐽**

{% tabs %}
{% tab title="#1" %}
```python
def maximumSumSubarray (k,arr,n):
    if n == 0: return 0
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    res = curr_sum
    for r in range(k,n):
        l = r-k     # l is "just outside the window on left"
        curr_sum += -arr[l] + arr[r]
        res = max(res, curr_sum)
    return res
```
{% endtab %}

{% tab title="#2" %}
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
    
    #1. sliding_window + deque ===================================
    #IDEA: keep the deque sorted in decreasing order
    n = len(a)
    Q = deque()
    res = []
    for i in range(k):
        while Q and Q[-1]<a[i]:
            Q.pop()
        Q.append(a[i])
    res.append(Q[0])
    
    for i in range(k,n):
        if Q and Q[0] == a[i-k]:
            Q.popleft()
        while Q and Q[-1]<a[i]:
            Q.pop()
        Q.append(a[i])
        res.append(Q[0])
    return res
    
    #2. sliding window + max_heap==================================
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

{% tab title="849." %}
```python
def maxDistToClosest(self, A: List[int]) -> int:
      
    # 1. ========================= My Approach, 2 pass :: : O(N)          
    n = len(A)
    left, right = [1]*n,[1]*n

    for i in range(n):
        if i== 0 or A[i] == 1:
            left[i] = float('inf')
        else:   # i>1
            if A[i-1]==0:
                left[i] = 1+left[i-1]
            else:
                left[i] = 1

    for i in range(n-1,-1,-1):
        if i== n-1 or A[i] == 1:
            right[i] = float('inf')
        else:   # i>1
            if A[i+1]==0:
                right[i] = 1+right[i+1]
            else:
                right[i] = 1

    dists = [0]*n

    for i in range(n):
        dists[i] = min(left[i],right[i])
        if dists[i] == float('inf'):
            dists[i] = 0
    return max(dists)

    # 2. ======================== 2Pointer Approach, single pass :: O(N)
    prev, max_len = 0, 0
    for cur, seat in enumerate(A):
        if seat:
            if A[prev]:
                max_len = max(max_len, (cur - prev) // 2)       # [...10001....]
            else:
                max_len = max(max_len, (cur - prev))            # [1000...
            prev = cur
    if A[prev]: 
        max_len = max(max_len, len(A) - 1 - prev)                # ...10000]
    return max_len
```
{% endtab %}
{% endtabs %}

### 2.2 Dynamic Size Window

* [x] [**3. Longest Substring Without Repeating Characters**](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** | @rubrik | doob maro sharam se behanchodd**
  * [x] CSES: [Playlist](https://cses.fi/problemset/task/1141) similar
* [x] [560.Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)✅
  * \*\*NOTE: \*\*Sliding window technique works only for all positive/all negative (i.e. not for arr with both pos & neg numbers).So soln#1 below gets WA
* [x] GfG#1: [Longest substring with k unique characters](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/) ❤️
  * [x] SIMILAR: [904.Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/submissions/)
* [x] [424.Longest Repeating Character Replacement ](https://leetcode.com/problems/longest-repeating-character-replacement/)(similar to #1) 🚀🚀
* [x] CSES: [Shortest Subsequence](https://cses.fi/problemset/task/1087/) | DNA | eee naa hora bina [theory](https://codeforces.com/blog/entry/82174) padhe.Karlo betta💪
* [x] [1658.Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | the trick is to identify that its a Sliding Window Q

{% tabs %}
{% tab title="3" %}
```python
# 1. ================================================ O(N^2) | @rubrik!!!
def lengthOfLongestSubstring(self, s: str) -> int:
    l,r = 0,0
    d = dict()
    ans = ''

    while r<len(s):
        if s[r] in d:
            l = max(d[s[r]]+1,l)

        d[s[r]] = r
        if r-l+1 >= len(ans):
            ans = s[l:r+1]
        r += 1

    return len(ans)

# 2. ============================================== O(N)

n = int(input())
a = list(I())

l = 0
ans = 0
D = dict()

for r in range(n):
    if a[r] in D:
        l = max(l,D[a[r]]+1)
    D[a[r]] = r
    ans = max(ans, r-l+1)
print(ans)
```
{% endtab %}

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

{% tab title="GfG#1" %}
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

{% tab title="ShortestSubsequence" %}
```python
'''
Taken from CF: https://codeforces.com/blog/entry/82174
Suppose we partition the string into 𝑘 contiguous subsegments such that the letters GCAT all appear at least once each in each partition. Then, it is clear that all 𝑘-character strings appear as subsequences.

We can construct such a partition greedily. Find the shortest prefix of the string that contains all characters GCAT, make that one subsegment, then recurse on the remaining string. Note that this might actually partition it into 𝑘+1 subsegments, where the last subsegment is ``incomplete''. The last character in each subsegment (besides the incomplete subsegment) also appears exactly once in that subsegment; greedily, if it appeared earlier in the subsegment, then we could have ended this partition earlier.

If 𝑘 is maximal, then we can show that there exists a 𝑘+1 length string that is not a subsequence. How? We can explicitly construct it as the last character in each of the partitions, plus some character not in the incomplete subsegment (or any character, if there is no incomplete subsegment).
'''
import collections
from typing import Counter


def solve():
    dna_chars = ['A','C','G','T']
    
    dna = str(input())
    start = 0
    partitions = []
    
    counter = dict()
    for i in range(len(dna)):
        if dna[i] in counter:
            counter[dna[i]] += 1
        else:
            counter[dna[i]] = 1
        if len(counter) == len(dna_chars):
            partitions.append(dna[start:i+1])
            start = i+1
            counter = dict()
    extra = ''
    if start != len(dna):
        extra = dna[start:]
        
    # print(partitions)
    res = ''
    for part in partitions:
        res += part[-1]
        
    if len(extra) == 0:
        res += 'A'
    else:
        diffs = list(set(dna_chars) - set([c for c in extra]))
        # print('diffs = ',diffs)
        res += str(diffs[0])
    print(res)
    


if __name__ == "__main__":
    solve()
```
{% endtab %}

{% tab title="" %}
```python
l = 0
curr = 0
d = -1
need = sum(A) - x
if need == 0:
    return len(A)

for r in range(0,len(A)):
    curr += A[r]
    while curr > need and l<r:
        curr -= A[l]
        l += 1
    if curr == need:
        print('\t ===============')
        d = max(d,r-l+1)
    print(f'>>> {curr} l = {l} , r ={r}')
if d==-1:
    return -1
return len(A)-d
```
{% endtab %}
{% endtabs %}

* [ ] [76.Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)🔒🔒
