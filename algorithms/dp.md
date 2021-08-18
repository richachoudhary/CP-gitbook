---
description: 'All the problems from LC, categorised'
---

# DP

## \# Notes 

*  **Approach for DP problem:**  find Recursion **===&gt;** Memoize it **===&gt;** \(optional\) Top-Down OR matrix
* Using **MEMO** in python: \(using **dict**-  constant lookup time\)

```python
MEMO = {}
# ... use memo inside recur fn
if (a,b,c) in MEMO: return MEMO[(a,b,c)]
# find res & set in MEMO
MEMO[(a,b,c)] = res
#------------------------------------------
# Using python's built-in MEMO:
@lru_cache(None)
def solve().....
```

* Memoization vs Top-Down: \(_both have same space & time complexities_\)
  * **Recursion+Memoization** is easy to think & code.**should be your goto** approach for all DP ques.
    * in Rarest of rare cases; it might lead to _recursive stack overflow err_
  * **Top-Down:** nobody can write it w/o recursive. Avoid for new/unseen problems
    * If recursion+memo gives stack-overflow err, use Top-Down!

## 1. Linear DP

* [x] CSES: [Projects](https://cses.fi/problemset/task/1140) \| [Kartik Arora](https://www.youtube.com/watch?v=MJn3ogwsUbo&ab_channel=KartikArora) ✅🐽🚀
  * Binary Search!!!! Dont skip!
  * Dekhke lagta nhi ki DP lagegi!!!
* [ ] [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [ ] [https://leetcode.com/problems/min-cost-climbing-stairs/](https://leetcode.com/problems/min-cost-climbing-stairs/)
* [ ] [https://leetcode.com/problems/divisor-game/](https://leetcode.com/problems/divisor-game/)
* [ ] [https://leetcode.com/problems/unique-binary-search-trees/](https://leetcode.com/problems/unique-binary-search-trees/)
* [ ] [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)
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

## 2.1 0/1 Knapsack

{% tabs %}
{% tab title="Knapsack" %}
```python
def knapsack(wt, val, W):    #NOTE: wt is sorted here; if not->first sort
    MEMO = {}
    def recur(wt,val,W,n):
        if n == 0 or W == 0:        # base case
            return 0
        if (W,n) in MEMO: return MEMO[(W,n)]
        if wt[n-1] <= W:
            opt1 = val[n-1] + recur(wt,val,W-wt[n-1],n-1)    # inclue
            opt2 = recur(wt,val,W,n-1)                       # dont inclue
            MEMO[(W,n)] = max(opt1,opt2)
         else:
            MEMO[(W,n)] = recur(wt,val,W,n-1)      # too heavy, cant inclue
        return MEMO[(W,n)]
                
    n = len(wt)
    return recur(wt,val,W,n)
```
{% endtab %}

{% tab title="MoneySums.cpp" %}
```cpp
int n;
cin >> n;
int max_sum = n*1000;
vector<int> x(n);
for (int&v : x) cin >> v;
vector<vector<bool> > dp(n+1,vector<bool>(max_sum+1,false));
dp[0][0] = true;
for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= max_sum; j++) {
        dp[i][j] = dp[i-1][j];
        int left = j-x[i-1];
        if (left >= 0 && dp[i-1][left]) {
            dp[i][j] = true;
        }
    }
}

vector<int> possible;
for (int j = 1; j <= max_sum; j++) {
    if (dp[n][j]) {
        possible.push_back(j);
    }
}
cout << possible.size() << endl;
for (int v : possible) {
    cout << v << ' ';
}
cout << endl;
```
{% endtab %}

{% tab title="MoneySums.py" %}
```python
def dp(n,curr,coins):
    if curr == 0:
        return True
    if n == 0:
        return False

    if (n,curr) in MEMO:
        return MEMO[(n,curr)]
    op1 = dp(n-1,curr-coins[n-1],coins)
    op2 = dp(n-1,curr,coins)
    MEMO[(n,curr)] =  op1 or op2
    return MEMO[(n,curr)]

def f():
    I = lambda : map(int, input().split())
    n = int(input())
    coins = list(I())
    coins.sort()
    maxsum = sum(coins)
    
    # ============================== o/w solution wont work!!
    for i in range(maxsum+1):
        dp(n,i,coins)

    res = []
    for x,y in MEMO:
        if MEMO[(x,y)]:
            res.append(y)
    res = list(set(res))
    print(len(res))

    for e in res:
        print(e, end = ' ')
```
{% endtab %}

{% tab title="TwoSets" %}
```cpp
int sum = n*(n+1)/2;
if(sum&1){
    cout<<0<<endl;
}else{
    sum /= 2;
    ll dp[n][sum+1];
    memset(dp,0,sizeof(dp));
    dp[0][0] = 1;
    for(int i=1;i<n;i++){
        for(int j=0;j<=sum;j++){
            dp[i][j] = dp[i-1][j];
            if (j >= i) dp[i][j] += dp[i-1][j-i] %= MOD;
        }
    }
    cout<<dp[n-1][sum]<<endl;
}
```
{% endtab %}
{% endtabs %}

#### 2.1.1 0/1 Knapsack Standard Variations \| source : [AdityaVerma](https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10&ab_channel=AdityaVerma)

* [x] GfG: [Subset Sum Problem](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
* [x] [416.Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
* [x] [GfG:: Count of subsets sum with a Given sum](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)
  * Replace `or` with `+` in Subset Sum Problem
* [x] [GfG: Sum of subset differences](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/)
  * [x] **Similar:**  [1049.Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/submissions/)
* [x] [494.Target Sum](https://leetcode.com/problems/target-sum/)  🎖
* [x] CSES: [Book Shop](https://cses.fi/problemset/task/1158/)
* [x] CSES: [Money Sums](https://cses.fi/problemset/task/1745/) \| Aisa Knapsack jo pehchaan na pao ✅⭐️💪💪🚀 \| **MUST DO**
* [x] CSES: [Two Sets II](https://cses.fi/problemset/task/1093)

#### 2.1.2  Problems: 0/1 Knapsack 

* [ ] [https://leetcode.com/problems/house-robber-ii/](https://leetcode.com/problems/house-robber-ii/)
* [ ] [https://leetcode.com/problems/ones-and-zeroes/](https://leetcode.com/problems/ones-and-zeroes/)
* [ ] [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)
* [ ] [https://leetcode.com/problems/shopping-offers/](https://leetcode.com/problems/shopping-offers/)
* [ ] [https://leetcode.com/problems/2-keys-keyboard/](https://leetcode.com/problems/2-keys-keyboard/)
* [ ] [https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)
* [ ] [https://leetcode.com/problems/best-team-with-no-conflicts/](https://leetcode.com/problems/best-team-with-no-conflicts/)
* [ ] [https://leetcode.com/problems/profitable-schemes/](https://leetcode.com/problems/profitable-schemes/)
* [ ] [https://leetcode.com/problems/tallest-billboard/](https://leetcode.com/problems/tallest-billboard/)
* [ ] [https://leetcode.com/problems/pizza-with-3n-slices/](https://leetcode.com/problems/pizza-with-3n-slices/)
* [ ] [https://leetcode.com/problems/reducing-dishes/](https://leetcode.com/problems/reducing-dishes/)

## 2.2 Unbounded Knapsack 

{% tabs %}
{% tab title="UB knapsack\(MEMO; SC-O\(N\*N\)" %}
```python
def knapsack(wt, val, W):    #NOTE: wt is sorted here; if not->first sort
    MEMO = {}
    def recur(wt,val,W,n):
        if n == 0 or W == 0:  
            return 0
        if (W,n) in MEMO: return MEMO[(W,n)]
        if wt[n-1] <= W:
            # we can again take all n elements
            opt1 = val[n-1] + recur(wt,val,W-wt[n-1],n)  # just this much change
            opt2 = recur(wt,val,W,n-1)             
            MEMO[(W,n)] = max(opt1,opt2)
         else:
            MEMO[(W,n)] = recur(wt,val,W,n-1)    
        return MEMO[(W,n)]
                
    n = len(wt)
    return recur(wt,val,W,n)
```
{% endtab %}

{% tab title="UB Knapsack: SC-O\(N\)" %}
```cpp
int dp[x+1];
dp[0] = 0;
for(int i=1;i<=x;i++){
	dp[i] = 1e9;
	for(int j=0;j<n;j++){
		if(a[j] <= i){
			dp[i] = min(dp[i], 1+dp[i-a[j]]);
		}
	}
}
if(dp[x] >= 1e9){
	cout<<-1;
}else{
	cout<<dp[x]<<endl;
}
```
{% endtab %}

{% tab title="CoinCombinations I" %}
```cpp
int dp[n][x+1];

for(int i=0;i<n;i++){
	for(int j=0;j<=x;j++){
		if(j==0){
			dp[i][j] = 1;
		}else{
			int opt1 = (j >= a[i]) ? dp[i][j-a[i]]%MOD : 0;
			int opt2 = (i > 0) ? dp[i-1][j]%MOD : 0;
			dp[i][j] = (opt1 + opt2)%MOD;
		}
	}
} 
```
{% endtab %}

{% tab title="Coin Combinations II" %}
```cpp
dp[0] = 1;
for (int weight = 0; weight <= x; weight++) {
	for (int i = 1; i <= n; i++) {
		if(weight - coins[i - 1] >= 0) {
			dp[weight] += dp[weight - coins[i - 1]];
			dp[weight] %= MOD;
		}
	}
}
cout << dp[x] << '\n';
```
{% endtab %}
{% endtabs %}

#### 2.2.1 Standard Problems: Unbounded Knapsack 

* [x] CSES: [Minimizing Coins](https://cses.fi/problemset/task/1634/)
* [x] CSES: [Coin Combinations 1](https://cses.fi/problemset/task/1635/) ✅
  * [x] CSES: [Coin Combinations 2](https://cses.fi/problemset/task/1636) ✅
  * **NOTE**: Switch the order of loops from 1 to get 2
* [x] [322.Coin Change](https://leetcode.com/problems/coin-change/) 🌟
* [x] [518.Coin Change 2](https://leetcode.com/problems/coin-change-2/)
* [x] GfG: [Rod Cutting Problem](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)         
  * [ ] Similar\(but Hard\)[1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

#### 2.2.2  Problems: Unbounded Knapsack 

## 3. Multi Dimension DP

* [x] CSES: [Grid Paths](https://cses.fi/problemset/task/1638/)
* [ ] CSES: [Array Description](https://cses.fi/problemset/task/1746) \| [KartikArora](https://www.youtube.com/watch?v=d1H5JylYG4I&ab_channel=KartikArora) .🐽✅🐽 
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
* [x] [https://leetcode.com/problems/dice-roll-simulation/](https://leetcode.com/problems/dice-roll-simulation/)
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
{% endtabs %}

## 4. Interval DP

* [x] CSES: [Removal Game](https://cses.fi/problemset/task/1097/)
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

## 5. Bit DP

### From KartikArora's Playlist

* [x] GfG: [Min cost for doing N jobs with N people](https://www.geeksforgeeks.org/job-assignment-problem-using-branch-and-bound/)
* [x] Traveling Salesman Problem:✅💯
  * Bruteforce: O\(N!\)
  * **DP**: SC: O\(N\*\(2^N\)\) , TC: O\(\(N^2\)\*\(2^N\)\)
* [x] CF: [Fish - Probability that i-th fish is alive at last](https://codeforces.com/contest/16/problem/E) \| [Video@KartikArora](https://www.youtube.com/watch?v=d7kvyp6dfz8&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=5&ab_channel=KartikArora) 😓
* [x] Codechef: [People Wearing diff t-shrits in party](https://www.codechef.com/problems/TSHIRTS) \| [Video@KartikArora](https://www.youtube.com/watch?v=Smem2tVQQXU&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=6&ab_channel=KartikArora)

{% tabs %}
{% tab title="\#1" %}
```python
MASK = 1<<21
dp = [[-1] for _ in MASK for _ in n] #n: no of people & jobs, 2^n is the BITMASK
def solve(i,mask,n):
    if i==n:     # no more people left 
        return 0
    if dp[i][mask] != -1:
        return dp[i][mask]
    ans = float('inf')
    for j in range(n):
        if mask&(1<<j):    # means j-th person is available
            ans = min(ans, cost[j][i] + solve(i+1, mask^(1<<j) , n)
    dp[i][mask] = ans
    return ans

solve(0,(1<<n) -1, n) 
# DP STATES:
'''
dp[i][mask] = cost of doing doing jobs with people i....N with 
              availability bitmask 'mask'
INIT: mask = 1111....(2^n) times .....11 :: all people are available  
'''
#COMPLEXITY:
1. Brute Force: O(N!)
2. DP: SC: O(N*(2^N)) , TC: O((N^2)*(2^N))
```
{% endtab %}

{% tab title="\#2.TSP" %}
```python
'''
dp(i,S) = min ( dist(i,j) + dp(j, S-{j}) )
S is the bitmask of size 2^n 
'''

@lru_cache(None)
def travellingSalesMan(i, mask, n):
    # Base Case
    if i == n and mask == 0:
        return cost[i-1][1]

    min_distance = sys.maxsize
    for j in range(n):
        if(mask & (1 << j)):
            min_distance = min(min_distance, cost[i][j] + travellingSalesMan(i+1, (mask ^ (1 << j)), n))
    return min_distance
```
{% endtab %}

{% tab title="CF-Fish" %}
```cpp
//#define double db
double prob[20][20];
double dp[(1 << 19)];
 
double pmove(int previous_bitmask, int must_die, int &n){
     
     int total_fishes = __builtin_popcount(previous_bitmask);
     long long  deno = ((total_fishes)*(total_fishes-1))/2;
     
     double move_prob = 0;
     for(int fish = 0; fish < n; fish++){
         if(previous_bitmask&(1 << fish)){
         move_prob += prob[fish + 1][must_die + 1];
        }  
    }
    return move_prob/(1.0*deno); 
}
 
double solve(int bitmask, int n){
    
    // Base case
    if(__builtin_popcount(bitmask) == n){
        return 1;
    }
    
    if(dp[bitmask] > -0.9){
        return dp[bitmask];
    }
    
    double answer = 0;
    for(int fish = 0; fish < n; fish++){
        bool alive = bitmask&((1 << fish));
        if(!alive){
           int previous_bitmask = bitmask^(1 << fish);
           double previous_day = solve(previous_bitmask, n);
           
           answer += previous_day*pmove(previous_bitmask, fish, n); 
        }
    }
    //cout << answer << endl;
    return dp[bitmask] = answer;
    
    
}
 
```
{% endtab %}

{% tab title="CC-tshirts" %}
```
https://www.codechef.com/viewsolution/28505745
```
{% endtab %}
{% endtabs %}

### My Own Solves:

* [x] [464.Can I Win](https://leetcode.com/problems/can-i-win/)
* [x] [698.Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) 💯💯
* [ ] CSES: [Elevator Rides](https://cses.fi/problemset/task/1653/) 🐽✅
* [ ] CSES: [Counting Tiles ](https://cses.fi/problemset/task/2181) \| [KartikArora](https://www.youtube.com/watch?v=lPLhmuWMRag&ab_channel=KartikArora) 🐽🐽

{% tabs %}
{% tab title="464." %}
```python
'''
dp(player,curr_score,mask) = OR (for all valid i's) 
                            [ 
                                    (curr_score+i>=Target) 
                                            or 
                            dp(next_player,scrore+i,mask with i-th bit turn off) 
                            ]
'''
def canIWin(self, N: int, Target: int) -> bool:
    MEMO = {}
    
    def solve(p,score, mask):
        if (p,mask) in MEMO: 
            return MEMO[(p,mask)]
        res = False
        for i in range(N+1):
            if mask&(1<<i): #is available
                this_res = (score + i +1>= Target or not solve(p^1, score+i+1,mask^(1<<i)))
                res = res or this_res
                if res: 
                    break
        MEMO[(p,mask)] = res
        return res
    
    p, score = 0,0
    mask = (1<<N) -1
    if N*(N+1)//2 < Target: 
        return False
    solve(p,score,mask)
    return MEMO[(0,mask)]
```
{% endtab %}

{% tab title="698.⭐️" %}
```python
MEMO = {}

def solve(x,k,cursum, mask):
    if k == 1:
        return True
    if cursum == target:
        return solve(0,k-1,0,mask)
    
    if cursum > target:
        return False
    
    res = False
    for i in range(x,N):
        if mask & (1<<i):
            res = res or solve(i,k,cursum+nums[i],mask^(1<<i))
    return res

# -------------------------------- Basic Validation: START
tot = sum(x for x in nums)
if tot%k != 0:
    return False
target = tot//k
for x in nums:
    if x > target:
        return False
# -------------------------------- Basic Validation: END
N = len(nums)

mask = (1<<N) - 1
cursum = 0

return solve(0,k,cursum,mask)
```
{% endtab %}

{% tab title="ElevatorRides" %}
```cpp
int n, k; cin>>n>>k;
int a[n];
for (int i = 0; i < n; i++)
    cin>>a[i];
pair<int, int> dp[1<<n];
dp[0] = {0, k+1};
for (int s = 1; s < (1<<n); s++) {
    dp[s] = {25, 0};
    for (int i = 0; i < n; i++) {
        if (s>>i&1){
            auto [c, w] = dp[s^(1<<i)];
            if (w + a[i] > k) {
                c++;
                w = min(a[i], w);
            }
            else
                w += a[i];
            dp[s] = min(dp[s], {c, w});
        }
    }
}
cout<<dp[(1<<n)-1].first;
```
{% endtab %}
{% endtabs %}

* [ ] [https://leetcode.com/problems/stickers-to-spell-word/](https://leetcode.com/problems/stickers-to-spell-word/)
* [ ] [https://leetcode.com/problems/shortest-path-visiting-all-nodes/](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
* [ ] [https://leetcode.com/problems/smallest-sufficient-team/](https://leetcode.com/problems/smallest-sufficient-team/)
* [ ] [https://leetcode.com/problems/maximum-students-taking-exam/](https://leetcode.com/problems/maximum-students-taking-exam/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/)
* [ ] [https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)
* [ ] [https://leetcode.com/problems/distribute-repeating-integers/](https://leetcode.com/problems/distribute-repeating-integers/)
* [ ] [https://leetcode.com/problems/maximize-grid-happiness/](https://leetcode.com/problems/maximize-grid-happiness/)
* [ ] [https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)
* [ ] [1411.Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) \| 🔒\| Contest-repeat! 
* [ ] [1931.Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/)  \| 🔒\| Contest-repeat!
* [ ] [1434.Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) \| Same as Little Elephant & T-shirts!!!!!

### 5.1 Resources: Bit DP

* ✅Kartik Arora's Playlist: [Bitwise DP](https://www.youtube.com/watch?v=6sEFap7hIl4&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&ab_channel=KartikArora)

## 6. Digit DP🔒

#### Pattern of problems:

* find all X in range \[L,R\] which follow some f\(x\)    . L,R could be very huge here ~ `10^18`
* [x] Q1: [Count numbers in range \[L,R\] s.t. sum of its digits == X.](https://www.youtube.com/watch?v=heUFId6Qd1A&list=PLb3g_Z8nEv1hB69JL9K7KfEyK8iQNj9nX&ab_channel=KartikArora)   \(1&lt;=L&lt;=R&lt;pow\(10,18\) , 1&lt;=X&lt;=180\)
* [ ] CSES: [Counting Numbers](https://cses.fi/problemset/task/2220/) \| [Kartik Arora](https://www.youtube.com/watch?v=lD_irvBkeOk&ab_channel=KartikArora) 🐽✅

{% tabs %}
{% tab title="\#1." %}
```python
'''
dp(N,X) = dp(N-1,X)   # put '0' at 1st postition
          + dp(N-1,X-1) # put '0' at 1st postition, sum needed now is X-1
          + .... dp(N-1,X-9)
        = SUM ( dp(N-1,X-i) ) for i:[0,9]
COMPLEXITY = O(X*logR) ..... very very loww for such big R           
'''
MEMO = {}
def solve(str,n,x,tight):
          if (n,x,tight) in MEMO: return MEMO[(n,x,tight)]
          if x<0:return 0
          if n == 1:
               if 0<=x<=9: return 1
               return 0
           res = 0
           ub = str[(len(str)-n)] if tight else 9
           for dig in range(ub+1):
                     res += solve(strs,n-1,x-dig, (tight and dig == ub))
           MEMO[(n,x,tight)] = res
           return res
          
l, r = '', '1234'
return solve(r,len(r),5,1) - solve(l,len(l),5,1)
```
{% endtab %}
{% endtabs %}

* [ ] [902.Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) 🔒
* [ ] [1012. Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/discuss/560346/python-digit-dp)
* [ ] [788. Rotated Digits](https://leetcode.com/problems/rotated-digits/discuss/560601/python-digit-dp)
* [ ] [1397. Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/discuss/560841/Python-Digit-DP)
* [ ] [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/discuss/560876/Python-Digit-DP)
* [ ] [357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/560898/Python-Digit-DP)
* [ ] [600. Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/584350/Python-Digit-DP-%28Pattern-For-Similar-Questions%29)

#### CF Problems:

* [ ] [Investigation](https://vjudge.net/problem/LightOJ-1068)
* [ ] [LIDS](https://toph.co/p/lids)
* [ ] [Magic Numbers](https://codeforces.com/contest/628/problem/D)
* [ ] [Palindromic Numbers](https://vjudge.net/problem/LightOJ-1205)
* [ ] [Chef and Digits](https://www.codechef.com/problems/DGTCNT)
* [ ] [Maximum Product](https://codeforces.com/gym/100886/problem/G)
* [ ] [Cantor](http://www.spoj.com/problems/TAP2012C/en/)
* [ ] [Digit Count](https://vjudge.net/problem/LightOJ-1122)
* [ ] [Logan and DIGIT IMMUNE numbers](https://www.codechef.com/problems/DIGIMU)
* [ ] [Sanvi and Magical Numbers](https://devskill.com/CodingProblems/ViewProblem/392)
* [ ] [Sum of Digits](http://www.spoj.com/problems/CPCRC1C/)
* [ ] [Digit Sum](http://www.spoj.com/problems/PR003004/)
* [ ] [Ra-One Numbers](http://www.spoj.com/problems/RAONE/)
* [ ] [LUCIFER Number](http://www.spoj.com/problems/LUCIFER/)
* [ ] [369 Numbers](http://www.spoj.com/problems/NUMTSN/)
* [ ] [Chef and special numbers](https://www.codechef.com/problems/WORKCHEF)
* [ ] [Perfect Number](https://codeforces.com/contest/919/problem/B)
* [ ] [The Great Ninja War](https://www.hackerearth.com/problem/algorithm/sallu-bhai-and-ias-8838ac8d/)
* [ ] AtCoder:[ Digit Product](https://atcoder.jp/contests/abc208/editorial/2216)

### 6.1 Resources: Digit DP

* CF: [Blog](https://codeforces.com/blog/entry/84928)
* ✅Kartik Arora's playlist: [Digit DP](https://www.youtube.com/watch?v=heUFId6Qd1A&list=PLb3g_Z8nEv1hB69JL9K7KfEyK8iQNj9nX&ab_channel=KartikArora)

## 7. DP on Trees

   ➡️See Trees section.

## 8. DP on Graph

* [x] CSES: [Forest Queries](https://cses.fi/problemset/result/2670872/) \| **`classic`**
* [ ] [https://leetcode.com/problems/cheapest-flights-within-k-stops/](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
* [ ] [https://leetcode.com/problems/find-the-shortest-superstring/](https://leetcode.com/problems/find-the-shortest-superstring/)

{% tabs %}
{% tab title="ForestQueries" %}
```python
I = lambda : map(int, input().split())
n,q = I()
graph = [[0]*(n+1)]

for _ in range(n):
    s = str(input())
    graph.append([0] + [c for c in s])

DP = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        DP[i][j] = 1 if graph[i][j] == '*' else 0
        DP[i][j] = DP[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

for _ in range(q):
    x1,y1,x2,y2 = I()
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])

```
{% endtab %}
{% endtabs %}

## 9. String DP

* [x] LC 5. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) \| [Video](https://www.youtube.com/watch?v=0CKUjDcUYYA) \| **NOT A DP Problem!!!** \| expand from all mid pts✅🚀✅
* [x] LC 44: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) ✅ \| very similar to **Edit Distance!!**
* [x] LC 10: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) ✅✅\| **diff from \#44**. Freq asked in FAANG!! \| [**TusharRoy**](https://www.youtube.com/watch?v=l3hda49XcDE)\*\*\*\*
* [x] LC 90: [Decode Ways](https://leetcode.com/problems/decode-ways/)
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
* [ ] [https://leetcode.com/problems/word-break-ii/](https://leetcode.com/problems/word-break-ii/)
* [ ] [https://leetcode.com/problems/count-the-repetitions/](https://leetcode.com/problems/count-the-repetitions/)
* [ ] [https://leetcode.com/problems/concatenated-words/](https://leetcode.com/problems/concatenated-words/)
* [ ] [https://leetcode.com/problems/count-different-palindromic-subsequences/](https://leetcode.com/problems/count-different-palindromic-subsequences/)
* [ ] [https://leetcode.com/problems/distinct-subsequences-ii/](https://leetcode.com/problems/distinct-subsequences-ii/)
* [ ] [https://leetcode.com/problems/longest-chunked-palindrome-decomposition/](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning-iii/](https://leetcode.com/problems/palindrome-partitioning-iii/)
* [ ] [https://leetcode.com/problems/find-all-good-strings/](https://leetcode.com/problems/find-all-good-strings/)
* [ ] [https://leetcode.com/problems/string-compression-ii/](https://leetcode.com/problems/string-compression-ii/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)

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
{% endtabs %}

## 9. Probability DP

* [ ] [https://leetcode.com/problems/soup-servings/](https://leetcode.com/problems/soup-servings/)
* [ ] [https://leetcode.com/problems/new-21-game/](https://leetcode.com/problems/new-21-game/)
* [ ] [https://leetcode.com/problems/airplane-seat-assignment-probability/](https://leetcode.com/problems/airplane-seat-assignment-probability/)

## 10. Classic DPs

### 10.1 Cadane's Algorithm

* [x] CSES: [Maximum Subarray Sum](https://cses.fi/problemset/task/1643)
* [ ] [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
* [ ] [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)
* [ ] [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] [https://leetcode.com/problems/longest-turbulent-subarray/](https://leetcode.com/problems/longest-turbulent-subarray/)
* [ ] [https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)
* [ ] [https://leetcode.com/problems/k-concatenation-maximum-sum/](https://leetcode.com/problems/k-concatenation-maximum-sum/)
* [ ] [https://leetcode.com/problems/largest-divisible-subset/](https://leetcode.com/problems/largest-divisible-subset/)
* [ ] [https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)

### 10.2 LCS

* [ ] [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)
* [ ] [https://leetcode.com/problems/longest-palindromic-subsequence/](https://leetcode.com/problems/longest-palindromic-subsequence/)
* [ ] [https://leetcode.com/problems/maximum-length-of-repeated-subarray/](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)[**=**](https://leetcode.com/problems/longest-common-subsequence/)
* [ ] [https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)
* [ ] [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)
* [ ] [https://leetcode.com/problems/wildcard-matching/](https://leetcode.com/problems/wildcard-matching/)
* [ ] [https://leetcode.com/problems/edit-distance/](https://leetcode.com/problems/edit-distance/)
* [ ] [https://leetcode.com/problems/interleaving-string/](https://leetcode.com/problems/interleaving-string/)
* [ ] [https://leetcode.com/problems/shortest-common-supersequence/](https://leetcode.com/problems/shortest-common-supersequence/)
* [ ] [https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
* [ ] [https://leetcode.com/problems/max-dot-product-of-two-subsequences/](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

### 10.3 LIS

#### 

*  **LIS in O\(NlogN\)** : [KartikArora](https://www.youtube.com/watch?v=66w10xKzbRM&ab_channel=KartikArora) \| [Leetcode Post](https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O%28nlogn%29-time-with-explanation) =&gt; Maintain Tails arr
  * `Tails` arr contains all the **starting** points of all **LISs**\(aptly named\)=&gt; use `bisect_left` for LIS
  * `Tails` arr contains all the **ending** points of all **LIDs**\(aptly named\) =&gt; use `bisect_right` for LDS

{% tabs %}
{% tab title="LIS in O\(NlogN\)⭐️" %}
```python
# dp keeps some of the visited element in a sorted list, and its size is lengthOfLIS sofar.
# It always keeps the our best chance to build a LIS in the future.
tails = []
for num in nums:
    i = bisect.bisect_left(tails, num)
    if i == len(tails):
        tails.append(num)    #append if bigger
    else: 
        tails[i] = num    # replace if in-btw
return len(tails)  

```
{% endtab %}

{% tab title="Towers✅" %}
```python
tails = []
for i in range(n):
    idx = bisect.bisect_right(tails,A[i])
    if idx == len(tails):
        tails.append(A[i])
    else:
        tails[idx] = A[i]
print(len(tails))
```
{% endtab %}
{% endtabs %}

* [x] CSES: [Towers](https://cses.fi/problemset/task/1073) ✅=&gt; Longest Decreasing Sequence: \(exactly same as LIS\)
* [x] [300.Longest Increasing Subsequence ](https://leetcode.com/problems/longest-increasing-subsequence/)
* [ ] [https://leetcode.com/problems/number-of-longest-increasing-subsequence/](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
* [ ] [https://leetcode.com/problems/russian-doll-envelopes/](https://leetcode.com/problems/russian-doll-envelopes/)
* [ ] [https://leetcode.com/problems/delete-columns-to-make-sorted-iii/](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)
* [ ] [https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/)
* [ ] [https://leetcode.com/problems/maximum-height-by-stacking-cuboids/](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/)
* [ ] [https://leetcode.com/problems/make-array-strictly-increasing/](https://leetcode.com/problems/make-array-strictly-increasing/)



### 10.4  2D Grid Traversal

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

### 10.5 Cumulative Sum

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

### 10.6 Hashmap\(SubArray\)

* [ ] [https://leetcode.com/problems/continuous-subarray-sum/](https://leetcode.com/problems/continuous-subarray-sum/)
* [ ] [https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)
* [ ] [https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

## 11. DP + Alpha \(Tricks/DS\)

* [ ] [https://leetcode.com/problems/arithmetic-slices-ii-subsequence/](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)
* [ ] [https://leetcode.com/problems/odd-even-jump/](https://leetcode.com/problems/odd-even-jump/)
* [ ] [https://leetcode.com/problems/constrained-subsequence-sum/](https://leetcode.com/problems/constrained-subsequence-sum/)
* [ ] [https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)

## 12. Insertion DP

* [ ] [https://leetcode.com/problems/k-inverse-pairs-array/](https://leetcode.com/problems/k-inverse-pairs-array/)

## 13. Memoization

* [ ] [https://leetcode.com/problems/minimum-jumps-to-reach-home/](https://leetcode.com/problems/minimum-jumps-to-reach-home/)
* [ ] [https://leetcode.com/problems/scramble-string/](https://leetcode.com/problems/scramble-string/)
* [ ] [https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/)
* [ ] [https://leetcode.com/problems/jump-game-v/](https://leetcode.com/problems/jump-game-v/)
* [ ] [https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/)

## 14. Binary Lifting

* [ ] [https://leetcode.com/problems/kth-ancestor-of-a-tree-node/](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)

## 15. Math

* [ ] [https://leetcode.com/problems/ugly-number-ii/](https://leetcode.com/problems/ugly-number-ii/)
* [ ] [https://leetcode.com/problems/count-sorted-vowel-strings/](https://leetcode.com/problems/count-sorted-vowel-strings/)
* [ ] [https://leetcode.com/problems/race-car/](https://leetcode.com/problems/race-car/)
* [ ] [https://leetcode.com/problems/super-egg-drop/](https://leetcode.com/problems/super-egg-drop/)
* [ ] [https://leetcode.com/problems/least-operators-to-express-number/](https://leetcode.com/problems/least-operators-to-express-number/)
* [ ] [https://leetcode.com/problems/largest-multiple-of-three/](https://leetcode.com/problems/largest-multiple-of-three/)
* [ ] [https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)

## 16. Geometrical DP \(blocks, rectangles etc\)

* [x] CSES: [Counting Towers](https://cses.fi/problemset/task/2413) \| [KartikArora](https://www.youtube.com/watch?v=pMEYMYTX-r0&ab_channel=KartikArora) ✅
* [x] CSES: [Rectangle Cutting](https://cses.fi/problemset/task/1744) \| [Kartik Arora](https://www.youtube.com/watch?v=LdynQjWsO5Q&ab_channel=KartikArora) ✅

{% tabs %}
{% tab title="CountingTowers" %}
```python
'''
STATES: 
    * height of tower = i
    * isLinked: 0/1     => whether brick of width 2 or 1
        0: | | |  : 2 bricks of with 1 each
        1: |   |  : brick of width 2
RECUR:
    * dp(i,0): 
        1. Dont extend any tile : 
            1.1 can place a tile of width 2  => dp(i-1,1)
            1.2 can palce 2 tiles of widht 1 => dp(i-1,0)
        2. Extend both:                      => dp(i-1,0)
        3. Extend Either:                    => 2*dp(i-1,0) 
    * dp(i,1):
        1. Dont extend any tile....         => 1.1 + 1.2
        4. Extend the linked piece          => dp(i-1,1)

ANS: dp(n,0) + dp(n,1)
'''
def dp(i,linked):
    if i == 1:
        return 1

    if (i,linked) in MEMO:
        return MEMO[(i,linked)]
    op1 = dp(i-1,1)%MOD         # 1.1
    op2 = dp(i-1,0)%MOD         # 1.2
    op3 = dp(i-1,0)%MOD     # 2
    op4 = 2*dp(i-1,0)%MOD   #3
    op5 = dp(i-1,1)%MOD     #4

    if linked == 0:
        MEMO[(i,linked)] = (op1 + op2 + op3 + op4)%MOD 
    else:
        MEMO[(i,linked)] = (op1 + op2 + op5)%MOD
    return MEMO[(i,linked)]

def f():
    # I = lambda : map(int, input().split())
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = (dp(n,0) + dp(n,1))%MOD
        print(res)

```
{% endtab %}

{% tab title="Rect Curring" %}
```python
'''       m
    _____________
    |           |
   n|           |
    |           |
'''
@lru_cache(None)
def dp(n,m):
    if n == m:
        return 0
    if (n,m) in MEMO:
        return MEMO[(n,m)]
    v_cut, h_cut = mxn,mxn

    for i in range(1,m):
        v_cut = min(v_cut, 1+dp(n,i)+dp(n,m-i))

    for i in range(1,n):
        h_cut = min(h_cut, 1+dp(i,m)+dp(n-i,m))
    
    MEMO[(n,m)] = min(v_cut,h_cut)
    return MEMO[(n,m)] 

def f():
    I = lambda : map(int, input().split())
    n,m = I()
    print(dp(n,m))
```
{% endtab %}
{% endtabs %}











## Resources

* DP Patterns for Beginners: [https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions](https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions)
* **Solved all DP problems in 7 months:** [**https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months**](https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months) ****
* DP pattens list: [https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491](https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491)
* @youtube:
  * WilliamFiset Playlist: [https://www.youtube.com/watch?v=gQszF5qdZ-0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&ab\_channel=WilliamFiset](https://www.youtube.com/watch?v=gQszF5qdZ-0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&ab_channel=WilliamFiset)
  * **✅Aditya Verma Playlist**: [https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL\_z\_8CaSLPWekqhdCPmFohncHwz8TY2Go&ab\_channel=AdityaVerma](https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&ab_channel=AdityaVerma)
    * Good for problem classification & variety, but poor for intuition building
  * **✅Kartik Arora's Playlist:** [https://www.youtube.com/watch?v=24hk2qW\_BCU&list=PLb3g\_Z8nEv1h1w6MI8vNMuL\_wrI0FtqE7&ab\_channel=KartikArora](https://www.youtube.com/watch?v=24hk2qW_BCU&list=PLb3g_Z8nEv1h1w6MI8vNMuL_wrI0FtqE7&ab_channel=KartikArora)

