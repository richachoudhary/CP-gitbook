# Knapsack Based

## 1. 0/1 Knapsack

* [x] GfG: [Subset Sum Problem](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
* [x] [416.Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
* [x] [GfG:: Count of subsets sum with a Given sum](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)
  * Replace `or` with `+` in Subset Sum Problem
* [x] [GfG: Sum of subset differences](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/)
  * [x] \*\*Similar: \*\* [1049.Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/submissions/)
* [x] [494.Target Sum](https://leetcode.com/problems/target-sum/) 🎖
* [x] CSES: [Book Shop](https://cses.fi/problemset/task/1158/)
* [x] CSES: [Money Sums](https://cses.fi/problemset/task/1745/) | Aisa Knapsack jo pehchaan na pao ✅⭐️💪💪🚀 | **MUST DO**
* [x] CSES: [Two Sets II](https://cses.fi/problemset/task/1093)
* [x] **Rubrik#1**. [Maximum Sum of numerically non-consecutive numbers in Arr](https://leetcode.com/discuss/interview-question/959412/Rubrik-or-Phone-Interview-or-Maximum-Sum) | **@rubrik** ✅

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

{% tab title="MoneySums" %}
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
MOD = 10**9 + 7
n = int(input())
 
DP = {}
def solve(i,curr):
    if curr > subset_sum or i > n:
        return 0
    if curr == subset_sum:
        return 1
 
    if (i,curr) in DP:
        return DP[(i,curr)]
    op1 = solve(i+1,curr+i)
    op2 = solve(i+1,curr)
    DP[(i,curr)] = (op1 + op2)%MOD
    return DP[(i,curr)]
    
total_sum = n*(n+1)//2
 
if total_sum%2 != 0:
    print('0')
else:
    subset_sum = total_sum//2
    ans = solve(0,0)
    print(ans//2) # removing the duplicates of type {a},{b} & {b},{a}
 
```
{% endtab %}

{% tab title="Rubrik#1" %}
```python
MEMO = {}
def dp(i,prev):
    if i >= n:
        return 0
    
    if (i,prev) in MEMO: 
        return MEMO[(i,prev)]
    opt1,opt2 = 0,0
    
    if A[i] == prev+1:
        opt1 = dp(i+1,prev)         # here you CANNOT take
    else:   
        opt1 = A[i] + dp(i+1,A[i])  # take A[i]
        opt2 = dp(i+1,prev)         # dont take A[i]
    
    MEMO[(i,prev)] = max(opt1,opt2)
    return MEMO[(i,prev)]

A = [1, 1, 1, 2, 2, 3, 6]    #==> 12
# A = [1, 1, 1, 2]             #==>3
n = len(A)
print(dp(0,-1))  
```
{% endtab %}
{% endtabs %}

## 2. Unbounded Knapsack

* [x] CSES: [Minimizing Coins](https://cses.fi/problemset/task/1634/)
* [x] CSES: [Coin Combinations 1](https://cses.fi/problemset/task/1635/) ✅ (unordered)
  * [x] CSES: [Coin Combinations 2](https://cses.fi/problemset/task/1636) ✅ (ordered)
  * [ ] **NOTE**: Switch the order of loops from 1 to get 2
* [x] [322.Coin Change](https://leetcode.com/problems/coin-change/) 🌟
* [x] [518.Coin Change 2](https://leetcode.com/problems/coin-change-2/)
* [ ] GfG: [Rod Cutting Problem](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/) 🐽
  * [ ] Similar(but Hard)[1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

{% tabs %}
{% tab title="MiniCoins" %}
```python
def f(a,i,x):
    if i > len(a) or x<0:
        return float('inf')
    if i == len(a):
        if x == 0: return 0
        else: return float('inf')
    op1 = f(a,i+1,x) 
    op2 = f(a,i,x-a[i])+1
    return min(op1 , op2)

n, x = 3,11
a = [1,7,5]
print(f(a,0,x))
```
{% endtab %}

{% tab title="UB Kp: SC-O(N)" %}
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

{% tab title="CoinComs I" %}
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

{% tab title="CoinCombs II" %}
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

{% tab title="RodCutting" %}
```python
fa
```
{% endtab %}
{% endtabs %}

##
