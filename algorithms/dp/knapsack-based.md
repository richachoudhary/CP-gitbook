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
* [x] GfG: [Rod Cutting Problem](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)
  * [ ] Similar(but Hard)[1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

{% tabs %}
{% tab title="UB knapsack(MEMO; SC-O(N*N)" %}
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

{% tab title="UB Knapsack: SC-O(N)" %}
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

##
