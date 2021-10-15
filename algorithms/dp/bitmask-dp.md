# Bitmask DP



### 1. From KartikArora's Playlist

* [x] GfG: [Min cost for doing N jobs with N people](https://www.geeksforgeeks.org/job-assignment-problem-using-branch-and-bound/)
* [x] Traveling Salesman Problem:✅💯
  * Bruteforce: O(N!)
  * **DP**: SC: O(N\*(2^N)) , TC: O((N^2)\*(2^N))
* [ ] CF: [Fish - Probability that i-th fish is alive at last](https://codeforces.com/contest/16/problem/E) | [Video@KartikArora](https://www.youtube.com/watch?v=d7kvyp6dfz8\&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g\&index=5\&ab_channel=KartikArora) 😓🐽🐽
* [ ] Codechef: **Little Elephant:** [People Wearing diff t-shrits in party](https://www.codechef.com/problems/TSHIRTS) | [Video@KartikArora](https://www.youtube.com/watch?v=Smem2tVQQXU\&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g\&index=6\&ab_channel=KartikArora)
* [ ] **CSES: **[**Counting Tiling**](https://cses.fi/problemset/task/2181)** : **number of ways to fill NxM board with 1x2 or 2x1 tiles** |**[** KartikArora**](https://www.youtube.com/watch?v=lPLhmuWMRag\&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g\&index=7\&ab_channel=KartikArora)** 🐽**

{% tabs %}
{% tab title="#1" %}
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

{% tab title="#2.TSP" %}
```python
'''
dp(i,S) = min ( dist(i,j) + dp(j, S-{j}) ) 
i.e. min dist to travel when you're @i & you need to visit cities in Set

==> S is the bitmask of size 2^n 

SC: O(N*(2^N))
TC: O((N^2)*(2^N)) : (N^2) because of transactional time
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
//Space Complexity: O(2^N)
//Time Complexity: O(N^2 * 2^N)

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
```cpp
//https://www.codechef.com/viewsolution/28505745
/*
dp(i,mask) = 
    no of ways to assign t-shirts from i...N 
    to the people in mask
    who are not wearing any t-shirt now(i.e. unassigned people)

mask = [0..100] (mentioned in Ques)
ANS = dp(1, (2^N))

dp(i,mask) = dp(i+1,mask) + SUM[dp(i+1, mask-{j}) s.t. own[i][j] == true]
*/


```
{% endtab %}

{% tab title="Counting Tiling🐽" %}
```cpp
void generate_next_masks(int current_mask, int i, int next_mask, int n, 
                            vector<int>& next_masks){
      if(i == n + 1){
        next_masks.push_back(next_mask);
        return;
      }
      
      if((current_mask & (1 << i)) != 0)
          generate_next_masks(current_mask, i + 1, next_mask, n, next_masks);
      
      if(i != n)
        if((current_mask & (1 << i)) == 0 && (current_mask & (1 << (i+1))) == 0)
          generate_next_masks(current_mask, i + 2, next_mask, n, next_masks);      
      
      if((current_mask & (1 << i)) == 0)
          generate_next_masks
                (current_mask, i + 1, next_mask + (1 << i), n, next_masks);    
}
 
int dp[1001][1<<11];
int solve(int col, int mask, const int m, const int n){
    // BASE CASE
    if(col == m + 1){
        if(mask == 0)
          return 1;
        return 0;
    }
 
    if(dp[col][mask] != -1)
      return dp[col][mask];
 
    int answer = 0;
    vector<int> next_masks;
    generate_next_masks(mask, 1, 0, n, next_masks);
 
    for(int next_mask: next_masks){
        answer = (answer + solve(col + 1, next_mask, m, n)) % mod;
    }
 
    return dp[col][mask] = answer;
}
 
int main() {
   init_code();
   int t = 1; //cin >> t;
   while(t--){
        read(n); read(m);
        memset(dp, -1, sizeof dp);
        cout << solve(1, 0, m, n); 
   }
   return 0;
}
```
{% endtab %}
{% endtabs %}

### 2. My Own Solves:

* [x] [464.Can I Win](https://leetcode.com/problems/can-i-win/)
* [x] [698.Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) 💯💯✅
* [ ] CSES: [Elevator Rides](https://cses.fi/problemset/task/1653/) 🐽✅
* [ ] CSES: [Counting Tiles ](https://cses.fi/problemset/task/2181) | [KartikArora](https://www.youtube.com/watch?v=lPLhmuWMRag\&ab_channel=KartikArora) 🐽🐽
* [ ] 1986.[Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) 🐽
* [ ] LC [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) 🐽| BFS + bitmask
* [ ] 804\. [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) | 🐽
* [x] @Google: [Team Standup Problem](https://leetcode.com/discuss/interview-question/978112/Google-or-L4-or-Onsite-SWE-or-Standups) 🤯🤯

{% tabs %}
{% tab title="464." %}
```python
'''
dp(player,curr_score,mask) = OR (for all valid i's) 
                            [ 
                                    (curr_score+i>=Target) 
                                            or 
                            NOT dp(next_player,scrore+i,mask with i-th bit turn off) 
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
            res = res or solve(i+1,k,cursum+nums[i],mask^(1<<i))
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

{% tab title="804" %}
```python
def splitArraySameAverage(self, A: List[int]) -> bool:
        
    def n_sum_target(n, tgt, j):    # helper fn, can we find n numbers in A[j:] that sum to tgt?

        if (n, tgt, j) in invalid:  # already know this is impossible
            return False
        if n == 0:                  # if no more numbers can be chosen,
            return tgt == 0         # then True if and only if we have exactly reached the target

        for i in range(j, len(C)):

            if C[i] > tgt:          # remaining numbers are at least as large because C is sorted
                break
            if n_sum_target(n - 1, tgt - C[i], i + 1):  # recurse having used num in B
                return True

        invalid.add((n, tgt, j))
        return False

    n, sum_A = len(A), sum(A)
    invalid = set()                 # memoize failed attempts
    C = sorted(A)                   # C initially contains all of A

    for len_B in range(1, (n // 2) + 1):  # try all possible lengths of B

        target = sum_A * len_B / float(n)
        if target != int(target):  # target must be an integer
            continue

        if n_sum_target(len_B, target, 0):
            return True

    return False
```
{% endtab %}

{% tab title="Stadnup@google" %}
```python
'''
Question:
N people are formed in a circle during standup. 
The first person starts the conversation and then calls on someone non-adjacent to them to go next. 
This process repeats until everyone has spoken only once. 
Given N, how many different combinations can standup take place?

N = 5 ==> ANS = 2
N = 9 ==> ANS = 4106
'''
memo = dict()

def standup(n, mask, last): # last -> the one who just spoke

    if mask == 2 ** n - 1:
        return 1
    
    if (mask, last) in memo:
        return memo[(mask, last)]
    
    ans = 0
    p = 0
    blocked = {}
    if last == 0:
        blocked = {1, n-1}
    elif last == n-1:
        blocked = {0,n-2}
    else:
        blocked = {last-1, last+1}
    while p < n:
        p_mask = 1 << p
        if mask & p_mask == 0 and p not in blocked:
            ans += standup(n, mask | p_mask, p)
        p += 1
    memo[(mask, last)] = ans
    return ans

N = 9 #change this
print(standup(N, 1, 0)) #leave second parameters as 1 and 0


'''
Time: O(2^N * N^2)
Space O(2^N * N)
'''
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
* [ ] [1411.Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) | 🔒| Contest-repeat! 
* [ ] [1931.Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/)  | 🔒| Contest-repeat!
* [ ] [1434.Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | Same as Little Elephant & T-shirts!!!!!

### 3. Resources: Bit DP

* ✅Kartik Arora's Playlist: [Bitwise DP](https://www.youtube.com/watch?v=6sEFap7hIl4\&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g\&ab_channel=KartikArora)
