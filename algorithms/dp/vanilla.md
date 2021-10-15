# Vanilla

## Solved

* [x] 70\. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | easy | `standard`
  * [x] Similar: LC [1269.Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) 🍪🍪
* [x] 198.[ House Robber](https://leetcode.com/problems/house-robber/) 
* [x] 213.[ House Robber II](https://leetcode.com/problems/house-robber-ii/) | circular 💪
* [x] 337\. [House Robber III](https://leetcode.com/problems/house-robber-iii/) | Tree
* [x] CSES: [Projects](https://cses.fi/problemset/task/1140) | [Kartik Arora](https://www.youtube.com/watch?v=MJn3ogwsUbo\&ab_channel=KartikArora) ✅🐽🚀
  * Binary Search!!!! Dont skip!
  * Dekhke lagta nhi ki DP lagegi!!!
* [x] LC: [1340.Jump Game V](https://leetcode.com/problems/jump-game-v/)
* [x] CF: [Potions](https://codeforces.com/problemset/problem/1526/C1)

{% tabs %}
{% tab title="70" %}
```python
MEMO = {}
def dp(x):
    if x == n:
        return 1
    if x > n:
        return 0
    if x in MEMO: return MEMO[x]
    op1 = dp(x+1)
    op2 = dp(x+2)
    MEMO[x] = op1+op2
    return MEMO[x]

return dp(0)
```
{% endtab %}

{% tab title="1269" %}
```python
MEMO = {}
def dp(x,k):
    if x < 0 or x >= arrLen:
        return 0
    if k == 0:
        if x == 0:
            return 1
        else:
            return 0
    if (x,k) in MEMO: return MEMO[(x,k)]
    op1 = dp(x-1,k-1)%MOD   #move from left
    op2 = dp(x+1,k-1)%MOD   #move from right
    op3 = dp(x,k-1)%MOD     #stay there         

    MEMO[(x,k)] = ((op1+op2)%MOD+op3)%MOD
    return MEMO[(x,k)]


return dp(0,steps)
```
{% endtab %}

{% tab title="198" %}
```python
MEMO = {}
        
def dp(i,nums):
    if i>len(nums)-1:
        return 0
    if i == len(nums)-1:
        return nums[i]
    
    if i in MEMO:
        return MEMO[i]
    opt1 = nums[i] + dp(i+2,nums)
    opt2 = dp(i+1,nums)
    MEMO[i] = max(opt1, opt2)
    return MEMO[i]
return dp(0,nums)
```
{% endtab %}

{% tab title="213" %}
```python
MEMO = {}
def dp(l,r):
    if l >= r:
        return 0
    if (l,r) in MEMO:
        return MEMO[(l,r)]
    opt1 = nums[l]+dp(l+2,r)
    opt2 = dp(l+1,r)
    MEMO[(l,r)] = max(opt1, opt2)
    return MEMO[(l,r)]
    
n = len(nums)
if n == 0:
    return 0
if n == 1:
    return nums[0]
if n == 2:
    return max(nums[0], nums[1])
return max(dp(0,n-1), dp(1,n))
```
{% endtab %}

{% tab title="337" %}
```python
MEMO = {}
def dp(x):
    if not x:
        return 0
    if not x.left and not x.right:
        return x.val
    if x in MEMO:
        return MEMO[x]
    opt1 = dp(x.left) + dp(x.right) # do not rob this node
    
    #rob this node
    opt2 = x.val 
    if x.left:
        opt2 += dp(x.left.left) + dp(x.left.right)
    if x.right:
        opt2 += dp(x.right.left) + dp(x.right.right) 
    MEMO[x] = max(opt1, opt2)
    return MEMO[x]
    
return dp(root)
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

{% tab title="Potions" %}
```python
# 1. DP ================================= timed out
@lru_cache(None)
def dp(x, curr, cnt):
    if x == n:
        return cnt
    ans = 0
    for i in range(x, n):
        op1, op2 = 0, 0
        if A[i] + curr >= 0:
            op1 = dp(i + 1, curr + A[i], cnt + 1)   # drink it
        op2 = dp(i + 1, curr, cnt)
        ans = max(ans, op1, op2)
    return ans
# 2. Greedy ============================ got AC
def solve(A):
    res = 0
    H = []  # min_heap
    curr_sum, curr_len = 0,0
    for a in A:
        curr_sum += a
        curr_len += 1
        heappush(H,a)
        
        while H and curr_sum < 0:
            x = heappop(H)
            curr_sum -= x
            curr_len -= 1
        res = max(res, curr_len)
    return res
```
{% endtab %}
{% endtabs %}



* [x] CSES: [Grid Paths](https://cses.fi/problemset/task/1638/)
* [ ] CSES: [Array Description](https://cses.fi/problemset/task/1746) | [KartikArora](https://www.youtube.com/watch?v=d1H5JylYG4I\&ab_channel=KartikArora) .🐽✅🐽 
* [x] Egg Dropping puzzle: [gfg](https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/) 🥚🏣✅

{% tabs %}
{% tab title="GridPaths" %}
```cpp
int dp[n][n];
dp[0][0] = 1;
for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
		if(a[i][j] == '.'){
			if(i==0 && j==0){
				dp[i][j] = 1;
			}else{
				int down = 0, right = 0;
				if(i>0){
					down = dp[i-1][j]%MOD;
				}
				if(j>0){
					right= dp[i][j-1]%MOD;
				}
				dp[i][j] = (right+down)%MOD;
			}
		}else{
			dp[i][j] = 0;
		}
	}
}
```
{% endtab %}

{% tab title="EggDropping" %}
```python
def dp(e,f): # f-> #floors, e-> #eggs
    if f == 1 or f == 0: # no floor/1 floor means 0/1 trials respectively
        return f
    if e == 1:  # we need f trials for 1 egg
        return f
    
    res = float('inf')
    for i in range(1,f+1):
        res = min(res, max(dp(e-1,i-1), dp(e,f-i)))
    return 1 + res
    
# TC: O(ef^2) -------> very bad ======================================


# 2. @lee215's ====================================[Turn the problem around ]

'''
He has turned the problem around from
"How many moves do you need to check N floors if you have K eggs"
to:
"How many floors can you check given M moves available and K eggs".

If you can solve this second problem than you can just increase the moves M one by one until you are able to check a number of floors larger or equal to the number N which the problem requires.
He then defined
dp[M][K] as the maximum number of floors that you can check within M moves given K eggs

A move essentially is dropping an egg and it either breaks or doesn't break.
Case A: The egg breaks and now you have spent 1 move (M=M-1) and also lost 1 egg (K=K-1). You can still check dp[M-1][K-1] floors, with your remaining eggs and moves.
Case B: The egg remains and you only loose one move (M=M-1). You can still check dp[M-1][K] floors.
Additionally you just checked a floor by dropping the egg from it.
Therefore dp[M][K] = dp[M - 1][k - 1] + dp[M - 1][K] + 1

The dp equation is:
dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
which means we take 1 move to a floor,
if egg breaks, then we can check dp[m - 1][k - 1] floors.
if egg doesn't breaks, then we can check dp[m - 1][k] floors.

dp[m][k] is the number of combinations and it increase exponentially to N


Complexity
For time, O(NK) decalre the space, O(KlogN) running,
For space, O(NK).
'''

def superEggDrop(self, K, N):
    dp = [[0] * (K + 1) for i in range(N + 1)]
    for m in range(1, N + 1):
        for k in range(1, K + 1):
            dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
        if dp[m][K] >= N: return m
```
{% endtab %}
{% endtabs %}



* [x] CSES: [Removal Game](https://cses.fi/problemset/task/1097/)

{% tabs %}
{% tab title="RemovalGame" %}
```python
def dp(l,r,a):
    if l == r: 
        return a[l]
    if l>r:
        return 0
    if (l,r) in MEMO:
        return MEMO[(l,r)]
    op1 = a[l] + min(dp(l+1,r-1,a), dp(l+2,r,a))
    op2 = a[r] + min(dp(l+1,r-1,a), dp(l,r-2,a))
    MEMO[(l,r)] = max(op1, op2)
    return MEMO[(l,r)]

def f():
    I = lambda : map(int, input().split())
    n = int(input())
    a = list(I())

    print(dp(0,n-1,a))
```
{% endtab %}
{% endtabs %}

## 2. String DP

* [x] LC 5. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Video](https://www.youtube.com/watch?v=0CKUjDcUYYA) | **NOT A DP Problem!!! **| expand from all mid pts✅🚀✅
* [x] LC 44: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) ✅ | very similar to **Edit Distance!!**
* [x] LC 10: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) ✅✅| **diff from #44**. Freq asked in FAANG!! | [**TusharRoy**](https://www.youtube.com/watch?v=l3hda49XcDE)****
* [x] LC 90: [Decode Ways](https://leetcode.com/problems/decode-ways/)
* [x] LC [140. Word Break II](https://leetcode.com/problems/word-break-ii/) 🚀 | **`startswith`**
  * [x] LC: [139.Word Break](https://leetcode.com/problems/word-break/)
* [x] LC [87. Scramble String](https://leetcode.com/problems/scramble-string/) 🤯💪😎✅| must_do

{% tabs %}
{% tab title="5.✅" %}
```python
n = len(s)
if n == 0:
    return ""

resl,ress = 1, s[0]
#1.expand all odd lengh palindromes
for i in range(n):
    l,r = i-1, i+1
    while l>= 0 and r <=n-1:
        if s[l] != s[r]:
            break
        else:
            if r-l+1 > resl:
                resl = r-l+1
                ress = s[l:r+1]
        l -= 1
        r += 1

#2. Expand all even-length palindromes
for i in range(n-1):
    l,r = i,i+1   # l,i,i+1,r
    while l>= 0 and r <=n-1:
        if s[l] != s[r]:
            break
        else:
            if r-l+2 > resl:
                resl = r-l+2
                ress = s[l:r+1]
        l -= 1
        r += 1
    
return ress
```
{% endtab %}

{% tab title="44" %}
```python
def isMatch(self, s: str, p: str) -> bool:
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

{% tab title="10.✅" %}
```python
def isMatch(self, s: str, p: str) -> bool:
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

{% tab title="90" %}
```python
def recur(s,i):
    # BC
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0
    if i in MEMO:
        return MEMO[i]
    # recursion
    opt1 = recur(s,i+1)
    opt2 = 0
    if i<= len(s)-2 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
        opt2 = recur(s,i+2) 
    MEMO[i] = opt1 + opt2
    return MEMO[i]
```
{% endtab %}

{% tab title="140.✅" %}
```python

# 139. Word Break I ======================================
 def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        MEMO = {}
        def recur(s):
            if s in MEMO:
                return MEMO[s]
            if s in wordDict:
                return True
            
            for word in wordDict:
                if not s.startswith(word):
                    continue
                elif len(word) == len(s):
                    MEMO[s] = True
                    return True
                else:
                    if recur(s[len(word):]):
                        MEMO[s] = True
                        return True
            MEMO[s] = False
            return False
            
        return recur(s)

# 140. Word Break II ======================================

def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
    def recur(s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = recur(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
    
    return recur(s, wordDict, {})

```
{% endtab %}

{% tab title="87." %}
```python
MEMO = {}
def recur(s,t):
    if s == t:
        return True
    if len(s) <= 1:
        return False
    if (s,t) in MEMO: return MEMO[(s,t)]
    res = False
    for i in range(1,len(s)):
        op1 = recur(s[:i],t[:i]) and recur(s[i:],t[i:]) #straight match
        op2 = recur(s[:i],t[len(s)-i:]) and recur(s[i:],t[:len(s)-i]) #swapped matches
        
        res = op1 or op2
        if res:
            break
        
    MEMO[(s,t)]= res
    return MEMO[(s,t)]

# base checks
if len(s1)!=len(s2): return False
if s1==s2: return True
return recur(s1,s2)
    
```
{% endtab %}
{% endtabs %}



* [x] 97.[Interleaving String](https://leetcode.com/problems/interleaving-string/) | standarddddddddddddddddddd | Do it nowwwwwwwwwww ✅✅✅💪💪
* [x] 1977\. [Number of Ways to Separate Numbers](https://leetcode.com/problems/number-of-ways-to-separate-numbers/) | contest | 🍪🍪🍪✅
* [x] **@shrechat:** Find all the possible combination of making a sentence from it in the same order.
* [x] LC 22. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)



{% tabs %}
{% tab title="97.✅💪Interleaved string" %}
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

{% tab title="1977." %}
```python
def numberOfCombinations(self, s: str) -> int:
    MOD = (10**9) +7
    
    MEMO = {}
    def dp(x,prev):
        if x == n:
            return 1
        if s[x] == '0':
            return 0
        if (x,prev) in MEMO:
            return MEMO[(x,prev)]
        res = 0
        for i in range(x,n):
            curr = int(s[x:i+1])
            if curr >= prev:
                res = (res + dp(i+1,curr))%MOD
        MEMO[(x,prev)] = res
        return MEMO[(x,prev)]%MOD
    
    n = len(s)
    return dp(0,0)
        
```
{% endtab %}

{% tab title="@sharechat" %}
```python
'''
Question

Given a string with n characters. Find all the possible combination of making a sentence from it in the same order. A sentence is a statement generated by using 1 or more words.
Example: uvqx
possible strings:
u v q x
uv qx
uv q x
uvqx
u vq x
u vqx
u v qx
uvq x
'''
def f(s,idx,last_space,op):
    if idx == len(s):
        print(op)
        return
    # to put a space
    if not last_space:
        op += ' '
        f(s,idx,True,op)
        op = op[0:len(op)-1]    # undo this space's addition
    
    # dont put a space
    op += s[idx]
    f(s,idx+1,False,op)
    
s = 'uvqx'
f(s,0,False,op=s[0])
```
{% endtab %}

{% tab title="22" %}
```python
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def f(op,cl,s):
        # print(f'op = {op}, cl = {cl} , s = {s}')
        if cl == 0:
            ans.append(s)
            return

        if op > 0: f(op-1,cl,s+'(')
        if cl > 0 and op < cl:f(op,cl-1,s+')')

    f(n,n,'')
    return ans
```
{% endtab %}
{% endtabs %}



* [ ] [https://leetcode.com/problems/is-subsequence/](https://leetcode.com/problems/is-subsequence/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning/](https://leetcode.com/problems/palindrome-partitioning/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning-ii/](https://leetcode.com/problems/palindrome-partitioning-ii/)
* [ ] [https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)
* [ ] [https://leetcode.com/problems/unique-substrings-in-wraparound-string/](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)
* [ ] [https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
* [ ] [https://leetcode.com/problems/longest-string-chain/](https://leetcode.com/problems/longest-string-chain/)
* [ ] [https://leetcode.com/problems/longest-happy-string/](https://leetcode.com/problems/longest-happy-string/)
* [ ] [https://leetcode.com/problems/longest-valid-parentheses/](https://leetcode.com/problems/longest-valid-parentheses/)
* [ ] [https://leetcode.com/problems/distinct-subsequences/](https://leetcode.com/problems/distinct-subsequences/)
* [ ] [https://leetcode.com/problems/count-the-repetitions/](https://leetcode.com/problems/count-the-repetitions/)
* [ ] [https://leetcode.com/problems/concatenated-words/](https://leetcode.com/problems/concatenated-words/)
* [ ] [https://leetcode.com/problems/count-different-palindromic-subsequences/](https://leetcode.com/problems/count-different-palindromic-subsequences/)
* [ ] [https://leetcode.com/problems/distinct-subsequences-ii/](https://leetcode.com/problems/distinct-subsequences-ii/)
* [ ] [https://leetcode.com/problems/longest-chunked-palindrome-decomposition/](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning-iii/](https://leetcode.com/problems/palindrome-partitioning-iii/)
* [ ] [https://leetcode.com/problems/find-all-good-strings/](https://leetcode.com/problems/find-all-good-strings/)
* [ ] [https://leetcode.com/problems/string-compression-ii/](https://leetcode.com/problems/string-compression-ii/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)

##

## Yet To Solve

* [ ] [https://leetcode.com/problems/divisor-game/](https://leetcode.com/problems/divisor-game/)
* [ ] [https://leetcode.com/problems/unique-binary-search-trees/](https://leetcode.com/problems/unique-binary-search-trees/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
* [ ] [https://leetcode.com/problems/counting-bits/](https://leetcode.com/problems/counting-bits/)
* [ ] [https://leetcode.com/problems/integer-break/](https://leetcode.com/problems/integer-break/)
* [ ] [https://leetcode.com/problems/count-numbers-with-unique-digits/](https://leetcode.com/problems/count-numbers-with-unique-digits/)
* [ ] [https://leetcode.com/problems/wiggle-subsequence/](https://leetcode.com/problems/wiggle-subsequence/)
* [ ] [https://leetcode.com/problems/maximum-length-of-pair-chain/](https://leetcode.com/problems/maximum-length-of-pair-chain/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
* [ ] [https://leetcode.com/problems/delete-and-earn/](https://leetcode.com/problems/delete-and-earn/)
* [ ] [https://leetcode.com/problems/domino-and-tromino-tiling/](https://leetcode.com/problems/domino-and-tromino-tiling/)
* [ ] [https://leetcode.com/problems/knight-dialer/](https://leetcode.com/problems/knight-dialer/)
* [ ] [https://leetcode.com/problems/minimum-cost-for-tickets/](https://leetcode.com/problems/minimum-cost-for-tickets/)
* [ ] [https://leetcode.com/problems/partition-array-for-maximum-sum/](https://leetcode.com/problems/partition-array-for-maximum-sum/)
* [ ] [https://leetcode.com/problems/filling-bookcase-shelves/](https://leetcode.com/problems/filling-bookcase-shelves/)
* [ ] [https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)
* [ ] [https://leetcode.com/problems/greatest-sum-divisible-by-three/](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
* [ ] [https://leetcode.com/problems/student-attendance-record-ii/](https://leetcode.com/problems/student-attendance-record-ii/)
* [ ] [https://leetcode.com/problems/decode-ways-ii/](https://leetcode.com/problems/decode-ways-ii/)
* [ ] [https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)
* [ ] [https://leetcode.com/problems/maximum-profit-in-job-scheduling/](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
* [ ] [https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)
* [ ] [https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)
* [ ] [https://leetcode.com/problems/stone-game-iii/](https://leetcode.com/problems/stone-game-iii/)
* [ ] [https://leetcode.com/problems/restore-the-array/](https://leetcode.com/problems/restore-the-array/)
* [ ] [https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/)
* [ ] [https://leetcode.com/problems/stone-game-iv/](https://leetcode.com/problems/stone-game-iv/)



* [ ] [https://leetcode.com/problems/triangle/](https://leetcode.com/problems/triangle/)
* [ ] [https://leetcode.com/problems/combination-sum-iv/](https://leetcode.com/problems/combination-sum-iv/)
* [ ] [https://leetcode.com/problems/out-of-boundary-paths/](https://leetcode.com/problems/out-of-boundary-paths/)
* [ ] [https://leetcode.com/problems/knight-probability-in-chessboard/](https://leetcode.com/problems/knight-probability-in-chessboard/)
* [ ] [https://leetcode.com/problems/champagne-tower/](https://leetcode.com/problems/champagne-tower/)
* [ ] [https://leetcode.com/problems/largest-sum-of-averages/](https://leetcode.com/problems/largest-sum-of-averages/)
* [ ] [https://leetcode.com/problems/minimum-falling-path-sum/](https://leetcode.com/problems/minimum-falling-path-sum/)
* [ ] [https://leetcode.com/problems/video-stitching/](https://leetcode.com/problems/video-stitching/)
* [ ] [https://leetcode.com/problems/longest-arithmetic-subsequence/](https://leetcode.com/problems/longest-arithmetic-subsequence/)
* [ ] [https://leetcode.com/problems/stone-game-ii/](https://leetcode.com/problems/stone-game-ii/)
* [ ] [https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
* [ ] [https://leetcode.com/problems/dice-roll-simulation/](https://leetcode.com/problems/dice-roll-simulation/)
* [ ] [https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
* [ ] [https://leetcode.com/problems/create-maximum-number/](https://leetcode.com/problems/create-maximum-number/)
* [ ] [https://leetcode.com/problems/frog-jump/](https://leetcode.com/problems/frog-jump/)
* [ ] [https://leetcode.com/problems/split-array-largest-sum/](https://leetcode.com/problems/split-array-largest-sum/)
* [ ] [https://leetcode.com/problems/freedom-trail/](https://leetcode.com/problems/freedom-trail/)
* [ ] [https://leetcode.com/problems/minimum-number-of-refueling-stops/](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
* [ ] [https://leetcode.com/problems/number-of-music-playlists/](https://leetcode.com/problems/number-of-music-playlists/)
* [ ] [https://leetcode.com/problems/count-vowels-permutation/](https://leetcode.com/problems/count-vowels-permutation/)
* [ ] [https://leetcode.com/problems/minimum-falling-path-sum-ii/](https://leetcode.com/problems/minimum-falling-path-sum-ii/)
* [ ] [https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)
* [ ] [https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)
* [ ] [https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
* [ ] [https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/)
* [ ] [https://leetcode.com/problems/paint-house-iii/](https://leetcode.com/problems/paint-house-iii/)
* [ ] [https://leetcode.com/problems/count-all-possible-routes/](https://leetcode.com/problems/count-all-possible-routes/)
* [ ] [https://leetcode.com/problems/guess-number-higher-or-lower-ii/](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)
* [ ] [https://leetcode.com/problems/arithmetic-slices/](https://leetcode.com/problems/arithmetic-slices/)
* [ ] [https://leetcode.com/problems/predict-the-winner/](https://leetcode.com/problems/predict-the-winner/)
* [ ] [https://leetcode.com/problems/palindromic-substrings/](https://leetcode.com/problems/palindromic-substrings/)
* [ ] [https://leetcode.com/problems/stone-game/](https://leetcode.com/problems/stone-game/)
* [ ] [https://leetcode.com/problems/minimum-score-triangulation-of-polygon/](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)
* [ ] [https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)
* [ ] [https://leetcode.com/problems/stone-game-vii/](https://leetcode.com/problems/stone-game-vii/)
* [ ] [https://leetcode.com/problems/burst-balloons/](https://leetcode.com/problems/burst-balloons/)
* [ ] [https://leetcode.com/problems/remove-boxes/](https://leetcode.com/problems/remove-boxes/)
* [ ] [https://leetcode.com/problems/strange-printer/](https://leetcode.com/problems/strange-printer/)
* [ ] [https://leetcode.com/problems/valid-permutations-for-di-sequence/](https://leetcode.com/problems/valid-permutations-for-di-sequence/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-merge-stones/](https://leetcode.com/problems/minimum-cost-to-merge-stones/)
* [ ] [https://leetcode.com/problems/allocate-mailboxes/](https://leetcode.com/problems/allocate-mailboxes/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-cut-a-stick/](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [https://leetcode.com/problems/stone-game-v/](https://leetcode.com/problems/stone-game-v/)

