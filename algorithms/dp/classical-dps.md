# Classical DPs



## 1. Kadane's Algorithm

* [x] CSES: [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | LC [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 
* [x] 152.[ Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) ✅| remember the swap
* [x] 873\. [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) 🍪🍪✅💪
* [x] 1186.[Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | so similar to Kaden's; yet the so simple approach is unthinkable | [approach_with_diag](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377522/C%2B%2B-forward-and-backward-solution-with-explanation-and-picture) | must do baby ✅💪
* [x] 368\. [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/submissions/) 🐽
* [x] 1191\. [K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)
* [x] 1014.[ Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/) 
  * It's similar to [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), but instead of min price, we track max value, and our max value decays every step due to the distance penalty
* [ ] [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] [https://leetcode.com/problems/longest-turbulent-subarray/](https://leetcode.com/problems/longest-turbulent-subarray/)
* [ ] [https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)
* [ ] [https://leetcode.com/problems/k-concatenation-maximum-sum/](https://leetcode.com/problems/k-concatenation-maximum-sum/)

{% tabs %}
{% tab title="53.(Kaden's Algo)" %}
```python
if n == 0:
    return 0

res = curr = a[0]
for x in a[1:]:
    curr = max(x,curr+x)
    res = max(res,curr)
return res
```
{% endtab %}

{% tab title="152" %}
```python
n = len(a)
if n == 0:
    return 0
curr = a[0]
maxp, minp,res = curr, curr,curr

for i in range(1,n):
    if a[i]< 0:
        maxp,minp = minp,maxp
    maxp = max(maxp*a[i], a[i])
    minp = min(minp*a[i],a[i])
    
    res = max(res,maxp)
return res
```
{% endtab %}

{% tab title="873" %}
```python
'''
dp[a, b] represents the length of fibo sequence ends up with (a, b)
Then we have dp[a, b] = (dp[b - a, a] + 1 ) or 2
'''
dp = collections.defaultdict(int)
s = set(A)
for i in range(len(A)):
    for j in range(i):
        if A[i] -A[j]< A[j] and A[i] - A[j] in s:
            dp[A[j], A[i]] = dp.get((A[i] - A[j], A[j]), 2) + 1
return max(dp.values() or [0])
```
{% endtab %}

{% tab title="1186.✅" %}
```python
n = len(a)  
max_forward,max_backward,excluding_me = [a[0]]*n, [a[0]]*n, [a[0]]*n

# calculate max_forward:
curr = a[0]
max_forward[0] = curr
for i in range(1,n):
    curr = max(curr+a[i],a[i])
    max_forward[i] = curr

# calculate max_backward
curr = a[-1]
max_backward[-1] = curr
for i in range(n-2,-1,-1):
    curr = max(curr+a[i],a[i])
    max_backward[i] = curr

# calculate excluding_me
for i in range(1,n-1):
    excluding_me[i] = max_forward[i-1]+max_backward[i+1]
    
# print(max_forward)
# print(max_backward)
# print(excluding_me)

return max(max(max_forward),max(max_backward),max(excluding_me))
```
{% endtab %}

{% tab title="368" %}
```python
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    if len(nums) == 0: return []
    nums.sort()
    sol = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                sol[i] = sol[j] + [nums[i]]
    return max(sol, key=len)
```
{% endtab %}

{% tab title="1191" %}
```python
MOD = (10**9)+7

def kaden(A):
    curr, ans = A[0],A[0]
    for i in range(1,len(A)):
        curr = max(curr+A[i], A[i])
✅        ans = max(ans,curr)
    return max(ans,0)


def solve(A,k):
    if k <= 1:
        return kaden(A)
    return (max(sum(A)*(k-2),0) + kaden(A*2))%MOD

return solve(A,k)

```
{% endtab %}

{% tab title="1014" %}
```python
def maxScoreSightseeingPair(self, A: List[int]) -> int:
    max_yet, ans = 0,0
    for a in A:
        ans = max(ans,max_yet+a)
        max_yet = max(a,max_yet) -1
        
    return ans
```
{% endtab %}
{% endtabs %}

## 2. LCS

* [x] 72\. Edit Distance | ✅✅| aata hai; par fir bhi dekh lo ek baar | _**the R-C initialization**_
* [x] ****[**1143. LCS **](https://leetcode.com/problems/longest-common-subsequence/)| standard
* [x] 718\. [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Now find this LCS 😎🤯😎
* [x] 5.[ Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | **`LPS`** | not a DP question
* [x] 516.[ Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | **`LPS`** | this is a DP question | **`LCS`**`on reversed self` ✅
* [x] 10\. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Regex Match 🐽✅✅
* [x] 44\. [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Wildcard Match 🐽✅✅
* [x] 97.[Interleaving String](https://leetcode.com/problems/interleaving-string/) | standarddddddddddddddddddd | Do it nowwwwwwwwwww ✅✅✅💪💪
* [ ] 1092\. [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/) | shortest-CS 🐽
* [x] 1312.[Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) 😎
  * just return **`len(s) - LPS`** (see #[516.LPS](https://leetcode.com/problems/longest-palindromic-subsequence/))
* [ ] [https://leetcode.com/problems/max-dot-product-of-two-subsequences/](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

{% tabs %}
{% tab title="72.EditDist" %}
```python
def minDistance(self, s: str, t: str) -> int:
    n,m = len(s), len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i
    
    for j in range(m+1):
        dp[0][j] = j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[-1][-1]
```
{% endtab %}

{% tab title="1143.LCS" %}
```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]
```
{% endtab %}

{% tab title="718.| print the LCS🤯😎" %}
```python
def lcs(h1,h2) -> int:
    n,m = len(h1), len(h2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    max_cnt = 0
    res = []

    for i in range(1,n+1):
        for j in range(1,m+1):
            if h1[i-1] == h2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if max_cnt < dp[i][j]:
                max_cnt = dp[i][j]
                res = h1[i-max_cnt:i]   #WOAHHHHHH 😎😎😎😎😎😎😎😎😎😎😎😎
    print(res)        #------------------------------> print the actual LCS 
    return max_cnt
```
{% endtab %}

{% tab title="516. LPS" %}
```python
t = s[::-1]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
max_cnt = 0
res = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        if max_cnt < dp[i][j]:
            max_cnt = dp[i][j]
return max_cnt
```
{% endtab %}

{% tab title="10🐽✅" %}
```python
s, p = ' '+ s, ' '+ p
lenS, lenP = len(s), len(p)
dp = [[0]*(lenP) for i in range(lenS)]
dp[0][0] = 1

for j in range(1, lenP):
    if p[j] == '*':
        dp[0][j] = dp[0][j-2]

for i in range(1, lenS):
    for j in range(1, lenP):
        if p[j] in {s[i], '.'}:
            dp[i][j] = dp[i-1][j-1]
        elif p[j] == "*":
            dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

return bool(dp[-1][-1])
```
{% endtab %}

{% tab title="44.🐽✅" %}
```python
n,m = len(s), len(p)
        
dp = [[False for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = True

# we set values to true until a non "*" character is found : for s = "adceb", p = "*a*b"
for j in range(1, len(p)+1):
    if p[j-1] != '*':
        break
    dp[0][j] = True

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == p[j-1] or p[j-1]=='?':
            dp[i][j] = dp[i-1][j-1]
        elif p[j-1] == '*':
            dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]

return dp[n][m]
```
{% endtab %}

{% tab title="97" %}
```python
def dp(a,b,c): # not O(N^3) but O(N^2) since 'c' is dependent -> 'a'+'b'         
    # base cases
    if c == len(s3) and b == len(s2) and a==len(s1): return True
    elif c==len(s3): return False
    
    # took from `A`; move the head pointers 
    if a<len(s1) and s1[a] == s3[c] and dp(a+1,b,c+1): 
        return True
    
    # took from `B`; move the head pointers 
    if b< len(s2) and s2[b] == s3[c] and dp(a,b+1,c+1): 
        return True
    
    return False

return dp(0,0,0)
```
{% endtab %}

{% tab title="1092" %}
```python
def lcs(A, B):
    n, m = len(A), len(B)
    dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + A[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    return dp[-1][-1]

res, i, j = "", 0, 0
for c in lcs(A, B):
    while A[i] != c:
        res += A[i]
        i += 1
    while B[j] != c:
        res += B[j]
        j += 1
    res += c
    i, j = i + 1, j + 1
return res + A[i:] + B[j:]
```
{% endtab %}
{% endtabs %}

## 3. LIS

*  [ ] **LIS in O(NlogN)** : [KartikArora](https://www.youtube.com/watch?v=66w10xKzbRM\&ab_channel=KartikArora) | [Leetcode Post](https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O\(nlogn\)-time-with-explanation) => Maintain Tails arr
  * `Tails` arr contains all the **starting** points of all **LISs**(aptly named)=> use `bisect_left` for LIS
  * `Tails` arr contains all the **ending** points of all **LIDs**(aptly named) => use `bisect_right` for LDS
* [x] CSES: [Towers](https://cses.fi/problemset/task/1073) ✅=> Longest Decreasing Sequence: (exactly same as LIS) | **just use** `bisect_right`
* [x] [300.Longest Increasing Subsequence ](https://leetcode.com/problems/longest-increasing-subsequence/)
* [x] 673\. [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) ✅💪| ye na kar paoge khud se implement|**`must_do`**
* [x] 354\. [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | must do!! 🪆🪆❤️ | **@Observer.AI | fuck_yaaar!**
* [ ] [https://leetcode.com/problems/delete-columns-to-make-sorted-iii/](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)
* [ ] [https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/)
* [ ] [https://leetcode.com/problems/maximum-height-by-stacking-cuboids/](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/)
* [ ] [https://leetcode.com/problems/make-array-strictly-increasing/](https://leetcode.com/problems/make-array-strictly-increasing/)

{% tabs %}
{% tab title="LIS in O(NlogN)⭐️" %}
```python
# dp keeps some of the visited element in a sorted list, and its size is lengthOfLIS sofar.
# It always keeps the our best chance to build a LIS in the future.
tails = []
for num in nums:
    i = bisect.bisect_left(tails, num)
    if i == len(tails):
        tails.append(num)    ## we can have a new, longer increasing subsequence!
    else: 
        tails[i] = num   # oh ok, at least we can make the ending element smaller
return len(tails)  

```
{% endtab %}

{% tab title="Towers✅" %}
```python
tails = []
for i in range(n):
    idx = bisect.bisect_right(tails,A[i]) # not bisect_left | to take only >= values
    if idx == len(tails):
        tails.append(A[i])
    else:
        tails[idx] = A[i]
print(len(tails))
```
{% endtab %}

{% tab title="673.✅" %}
```python
import bisect
def findNumberOfLIS(self, A: List[int]) -> int:
    tails = []
    n = len(A)
    counter = defaultdict(list)
    for i in range(n):
        idx = bisect.bisect_left(tails,A[i])
        if idx == len(tails):
            tails.append(A[i])
        else:
            tails[idx] = A[i]
        
        total = 0
        for count, last in counter[idx]:
            if last < A[i]:
                total += count
        counter[idx+1].append((max(1, total), A[i]))
        
    # print(counter)
    res = 0
    for cnt,_ in counter[len(tails)]:
        res += cnt
    return res
    
'''
For example for [1,3,5,4,7]; counter =
len : [(count, last_biggest)]
{
   1: [(1, 1)],
   2: [(1, 3)],
   3: [(1, 5), (1, 4)],
   4: [(2, 7)]
}
& for nums = [2,2,2,2,2]
counter = 
{
    0: [], 
    1: [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
}
'''
```
{% endtab %}

{% tab title="354.🪆❤️" %}
```python
def maxEnvelopes(self, A: List[List[int]]) -> int:
    A.sort()
    n = len(A)
    
# 1. O(N^2) : TLE ===============================================
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[i][0] > A[j][0] and A[i][1] > A[j][1] :
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)
# 2. O(NlogN) ===================================================
    
    # just sorting by asc. order of width will do
    # the only edge case: for consecutive envelopes with the same sorted width
    # to avoid this: sort by dec order of heights
    # s.t. the first envelope encountered for any given width would be 
    # the largest one.
    
    A.sort(key=lambda x: (x[0], -x[1]))
    tails = []
    for _,height in A:
        left = bisect_left(tails, height)
        if left == len(tails): 
            tails.append(height)
        else: 
            tails[left] = height
    return len(tails)
```
{% endtab %}
{% endtabs %}



## 4.  2D Grid Traversal

* [ ] [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)
* [ ] [https://leetcode.com/problems/unique-paths-ii/](https://leetcode.com/problems/unique-paths-ii/)
* [ ] [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)
* [ ] [https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/)
* [ ] [https://leetcode.com/problems/where-will-the-ball-fall/](https://leetcode.com/problems/where-will-the-ball-fall/)
* [ ] [https://leetcode.com/problems/dungeon-game/](https://leetcode.com/problems/dungeon-game/)
* [ ] [https://leetcode.com/problems/cherry-pickup/](https://leetcode.com/problems/cherry-pickup/)
* [ ] [https://leetcode.com/problems/number-of-paths-with-max-score/](https://leetcode.com/problems/number-of-paths-with-max-score/)
* [ ] [https://leetcode.com/problems/cherry-pickup-ii/](https://leetcode.com/problems/cherry-pickup-ii/)
* [ ] [https://leetcode.com/problems/kth-smallest-instructions/](https://leetcode.com/problems/kth-smallest-instructions/)

## 5. Cumulative Sum

* [ ] [https://leetcode.com/problems/range-sum-query-immutable/](https://leetcode.com/problems/range-sum-query-immutable/)
* [ ] [https://leetcode.com/problems/maximal-square/](https://leetcode.com/problems/maximal-square/)
* [ ] [https://leetcode.com/problems/range-sum-query-2d-immutable/](https://leetcode.com/problems/range-sum-query-2d-immutable/)
* [ ] [https://leetcode.com/problems/largest-plus-sign/](https://leetcode.com/problems/largest-plus-sign/)
* [ ] [https://leetcode.com/problems/push-dominoes/](https://leetcode.com/problems/push-dominoes/)
* [ ] [https://leetcode.com/problems/largest-1-bordered-square/](https://leetcode.com/problems/largest-1-bordered-square/)
* [ ] [https://leetcode.com/problems/count-square-submatrices-with-all-ones/](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
* [ ] [https://leetcode.com/problems/matrix-block-sum/](https://leetcode.com/problems/matrix-block-sum/)
* [ ] [https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
* [ ] [https://leetcode.com/problems/count-submatrices-with-all-ones/](https://leetcode.com/problems/count-submatrices-with-all-ones/)
* [ ] [https://leetcode.com/problems/ways-to-make-a-fair-array/](https://leetcode.com/problems/ways-to-make-a-fair-array/)[=](https://leetcode.com/problems/maximal-rectangle/)
* [ ] [https://leetcode.com/problems/maximal-rectangle/](https://leetcode.com/problems/maximal-rectangle/)
* [ ] [https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)
* [ ] [https://leetcode.com/problems/super-washing-machines/](https://leetcode.com/problems/super-washing-machines/)
* [ ] [https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
* [ ] [https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
* [ ] [https://leetcode.com/problems/get-the-maximum-score/](https://leetcode.com/problems/get-the-maximum-score/)

###
