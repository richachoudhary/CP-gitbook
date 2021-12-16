# GoogleQB: Round#2

* [x] [1-> List All Bad Commits between consecutive releases](https://leetcode.com/discuss/interview-question/1623205/Google-Onsite-Question)
* [x] [2-> Cord Tree/Rope Tree](https://leetcode.com/discuss/interview-question/1593355/google-phone-interview-rejected)
* [ ] 3-> [LC 552.Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/)
* [ ] 4-> [Recipe Finder](https://leetcode.com/discuss/interview-question/1504849/google-onsite) //topological sort
* [ ] 5-> [Compressed Paths](https://leetcode.com/discuss/interview-question/1595072/Google-L4-or-Banglore-or-Onsite) 🐽
* [x] 6-> [Starts & Ends at same char](https://leetcode.com/discuss/interview-question/1586927/Google-or-OA)
* [x] 7-> [IPs Mapping to City](https://leetcode.com/discuss/interview-question/1584626/Google-India-or-Phone-Screen)
* [x] 8-> [LC.45 Jump Game II](https://leetcode.com/problems/jump-game-ii/)
* [ ] 9-> [LC.1138 Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/)

{% tabs %}
{% tab title="1" %}
You are working on a project and you noticed that there has been a performance decrease between two releases. You have a function:\
boolean worseCommit(int commit1, int commit2)

that runs performance tests and returns true if commit2 is worse than commit1 and false otherwise.\
Find all the bad commits that have decreased the performance between releases. Performance can only decrease not increase with each successive commit.

### App#1: Linear Scan :: TC- O(N)&#x20;

![](<../.gitbook/assets/Screenshot 2021-12-13 at 3.59.44 AM.png>)

```python
commits = [10,10,9,8,6,6,6,5,1]

def worse_commit(commit1, commit2)->bool:
	return commits[commit1] > commits[commit2]

def find_bad_commits(left, right): 
    bad_commits = []
    for i in range(left, right):
        if worse_commit(i,i+1):
            bad_commits.append(i+1)
    return bad_commits

# func call
print(find_bad_commits(0,len(commits)-1))
'''
TC: O(N) - assuming :worse_commit" takes O(1) time
SC: O(N) - to store the return list of bad commits
'''
```

### App#2: Binary Search / DnQ

![](<../.gitbook/assets/Screenshot 2021-12-13 at 4.20.07 AM.png>)

````python
bad_commits = []

def f(l,r):
    if l>r: return
    if l == r-1 and worse_commit(l,r):
        bad_commits.append(r)
        return
    mid = (l+r)//2
    if worse_commit(l,mid):
        f(l,mid)
    if worse_commit(mid,r):
        f(mid,r)
        
f(0,len(commits)-1)
print(bad_commits)
```
TC: 
    * Avg Case: O(logN)
    * Worst Case: O(N) => for strictly decreasing commits_arr
```
````
{% endtab %}

{% tab title="2.CordTree" %}
```python
class LeafNode:
    def __init__(self):
        self.val = ""
        self.length = 0
        
class InternalNode:
    def __init__(self):
        self.length = 0
        self.left = self.right = None
        
class Cord:
    def __init__(self, s):
        self.threshold = 5
        self.root = self.build(s)
        
    def build(self, s):
        if len(s) > self.threshold:
            mid = len(s) // 2
            node = InternalNode()
            node.left = self.build(s[:mid])
            node.right = self.build(s[mid:])
            node.length = node.left.length + node.right.length
            return node
        else:
            node = LeafNode()
            node.val = s
            node.length = len(s)
            return node
        
    def toString(self, node = None):
        if not node:
            node = self.root
        if isinstance(node, LeafNode):
            return node.val
        return self.toString(node.left) + self.toString(node.right)
    
    def charAt(self, i, node = None):
        if node == None:
            node = self.root
        if i >= node.length:
            raise Exception("Out of bound")
        if isinstance(node, LeafNode):
            return node.val[i]
        if i < node.left.length:
            return self.charAt(i, node.left)
        return self.charAt(i - node.left.length, node.right)
    
    def merge(self, other):
        newRoot = InternalNode()
        newRoot.left = self.root
        newRoot.right = other.root
        newRoot.length = self.root.length + other.root.length
        self.root = newRoot
        
    def substring(self, left, right, node = None):
        if node == None:
            node = self.root
        if not 0 <= left < node.length or not left <= right or not 0 <= right <= node.length:
            raise Exception("Substring size is incorrect")
        if isinstance(node, LeafNode):
            return node.val[left:right]
        ans = ""
        if left < node.left.length:
            ans += self.substring(left, min(node.left.length, right), node.left)
        if right > node.left.length:
            ans += self.substring(max(0, left - node.left.length), right - node.left.length, node.right)
        return ans

    
    
#Tests
s = "abcde"
s2 = "pdgsadfssagdasdgasda"
cord = Cord(s)
cord2 = Cord(s2)

for i in range(len(s)):
    for j in range(i, len(s) + 1):
        if cord.substring(i,j) != s[i:j]:
            print("Found Bug")
for i in range(len(s)):
    if s[i] != cord.charAt(i):
        print("Found Bug")
cord.merge(cord2)
s += s2
print(s == cord.toString())
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if cord.substring(i,j) != s[i:j]:
            print("Found bug")
for i in range(len(s)):
    if s[i] != cord.charAt(i):
        print("Found Bug")
        
'''
TC: O(H) where H is the height of the tree
'''        
```
{% endtab %}

{% tab title="3->552" %}
### My (MEMO) soln - TLE

```python
MOD = 10**9 + 7

DP = {}
def is_eligible(record):
    if record.count('A') >= 2: return False
    for i in range(2,len(record)):
        if record[i-2] == 'L' and record[i-1] == 'L' and record[i] == 'L' : return False
    return True

def recur(n,curr_record):
    if n == 0:
        if is_eligible(curr_record):
            return 1
        return 0
    if (n,curr_record) in DP:
        return DP[(n,curr_record)]

    #op1: P
    op1 = recur(n-1,curr_record+'P')%MOD

    #op2: A
    op2 = 0
    if curr_record.count('A') < 2:
        op2 = recur(n-1, curr_record+'A')%MOD

    #op3: L
    op3 = 0
    if len(curr_record) < 2 or (len(curr_record) >= 2 and not(curr_record[-1] == 'L' and curr_record[-2] == 'L')):
        op3 = recur(n-1, curr_record+'L')%MOD

    DP[(n,curr_record)] = ((op1+op2)%MOD+op3)%MOD
    return DP[(n,curr_record)]

return recur(n,'')
```

### LC's soln

```python
if not n:
    return 0

if n == 1:
    return 3

MOD = 10 ** 9 + 7
dp = [1, 2, 4] + [0] * (n - 2)

# Calculate sequences without 'A'.
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

# Calculate final result.
rslt = dp[n] % MOD
for i in range(n):
    rslt += (dp[i] * dp[n - 1 - i]) % MOD

return rslt % MOD

"""
Suppose dp[i] is the number of all the rewarded sequences without 'A'
having their length equals to i, then we have:
    1. Number of sequence ends with 'P': dp[i - 1]
    2. Number of sequence ends with 'L':
        2.1 Number of sequence ends with 'PL': dp[i - 2]
        2.2 Number of sequence ends with 'LL':
            2.2.1 Number of sequence ends with 'PLL': dp[i - 3]
            2.2.2 Number of sequence ends with 'LLL': 0 (not allowed)

    So dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3], 3 <= i <= n

Then all the rewarding sequences with length n are divided into
two cases as follows:
    1. Number of sequences without 'A': dp[n]
    2. Number of sequence with A in the middle, since we could only 
        have at most one A in the sequence to get it rewarded, 
        suppose A is at the ith position, then we have:
            A[i] = dp[i] * dp[n - 1 - i]

        Then the number of such sequences is:
            sum(A[i] for i in range(n))

Then our final result will be dp[n] + sum(A[i] for i in range(n)).

Corner cases:
    1. dp[0] = 1: which means the only case when the sequence is an
        empty string.
    2. dp[1] = 2: 'L', 'P'
    3. dp[2] = 4: 'LL', 'LP', 'PL', 'PP'
"""        
```
{% endtab %}

{% tab title="4" %}
```python
class Recipe:
    def __init__(self, name: str, rawIngredients, intermediateRecipes):
        self.name = name
        self.raw = rawIngredients
        self.dep = intermediateRecipes


class RecipeFinder:
    # initialization happens exactly once, time complexity is O(V + E)
    # where V is the number of recipes, and E is the number of "edges"
    # between those recipes created by the "intermediateRecipes" list
    def __init__(self, recipes):
        self.parents = {recipe.name: set() for recipe in recipes}
        for recipe in recipes:
            for child in recipe.dep:
                self.parents[child].add(recipe)

        self.leaves = set([recipe for recipe in recipes if len(recipe.dep) == 0])

    # time complexity is O(V + E + total number of raw ingredients) in the
    # worst case. total number of raw ingredients is probably very small per
    # recipe, easily less than 30 for any specific recipe in the real world.
    # so essentially O(V + E).
    def findRecipes(self, ingredients):
        search = self.leaves.copy()
        # number of satisfied "dependencies" (intermediate ingredients) per
        # recipe. topological sort
        satisfied = {recipe: 0 for recipe in self.parents}
        ret = []
        givenIngredientSet = set(ingredients)

        while search:
            recipe = search.pop()

            if not all(ing in givenIngredientSet for ing in recipe.raw):
                continue

            ret.append(recipe.name)
            for parent in self.parents[recipe.name]:
                satisfied[parent.name] += 1
                if satisfied[parent.name] == len(parent.dep):
                    search.add(parent)

        return ret

```
{% endtab %}

{% tab title="5🐽" %}

{% endtab %}

{% tab title="6" %}
```python
def solution(S):
    d = {}

    # store the furthest index of the letters in S
    for i in range(len(S) - 1, -1, -1):
        if S[i] not in d:
            d[S[i]] = i

    max_length = float("-infinity")
    best_index = 0

    # loop from the beginning of S
    for i, let in enumerate(S):
        # calculate the distance from current instance of the letter to the last
        sub_length = d[let] + 1 - i
        # only update if the distance is greater than max
        # this means we always start our answer from the earliest index possible. 
        if sub_length > max_length:
            best_index = i
            max_length = sub_length
            
    return S[best_index:d[S[best_index]] + 1]

print(solution("performance") == "erformance")
print(solution("adsaas") == "adsaa")
print(solution("adsaass") == "adsaa")
print(solution("adsaasss") == "saasss")
```
{% endtab %}

{% tab title="7" %}
### Simple Approach: O(len(Dict))

```python
IPs = dict()    #city -> [from,to]
IPs["bangalore"] = ['100.100.100.100','200.200.200.200'] 
IPs["mumbai"] = ['101.100.100.100','201.200.200.200'] 

def find_ips_city(ip) -> str:
    #TODO: handle out of bound err
    ip_to_str = ''.join(list(ip.split('.')))
    for city, [fromm,to] in IPs.items():
        if fromm<= ip_to_str <= to:
            return city
    return "NA"

# test 
ip1 = "100.100.100.101"    #-> blr
print(find_ips_city(ip1))

ip2 = "100.100.199.100"    #-> blr
print(find_ips_city(ip2))

ip3 = "200.100.199.100"    #-> mumbai
print(find_ips_city(ip3))

ip4 = "900.100.199.100"    #-> NA
print(find_ips_city(ip4))


```

### Optimized Approach: use Trie :: O(logN)

[here](https://www.lewuathe.com/longest-prefix-match-with-trie-tree.html)
{% endtab %}

{% tab title="8" %}
```python
def jump(self, nums: List[int]) -> int:
    # 1. DP =============================== TC: O(N^2), SC: O(N)
    n = len(nums)

    @lru_cache(None)
    def dp(i):
        if i == n - 1: return 0  # Reached to last index
        ans = math.inf
        maxJump = min(n - 1, i + nums[i])
        for j in range(i + 1, maxJump + 1):
            ans = min(ans, dp(j) + 1)
        return ans

    return dp(0)

    # 2. Greedy (BETTER) ===================== TC: O(N), SC: O(1)
    jumps = 0
    farthest = 0
    left = right = 0
    while right < len(nums) - 1:
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jumps += 1

    return jumps
```
{% endtab %}

{% tab title="9" %}
```python
# BFS
from collections import deque
class Solution(object):
    def alphabetBoardPath(self, target):
        res=[]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        def bfs(x,y,target):
            if board[x][y]==target:
                return x,y,'!'
            q=deque([(x,y,"")])
            visited={(x,y)}
            while q:
                x,y,path=q.popleft()
                for i,j,s in [(1,0,'D'),(0,1,'R'),(-1,0,'U'),(0,-1,'L')]:
                    if 0<=x+i<=5 and 0<=y+j<len(board[x+i]) and (x+i,y+j) not in visited:
                        visited.add((x+i,y+j))
                        if board[x+i][y+j]==target:
                            return x+i,y+j,path+s+'!'
                        else:
                            q.append((x+i,y+j,path+s))
        
        x,y=0,0
        for ch in target:
            x,y,path=bfs(x,y,ch)
            res.append(path)
        return ''.join(res)
```
{% endtab %}
{% endtabs %}

* [x] 10-> [954.Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)
  * [x] 10.1 -> [2007.Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/)
* [ ] 11-> [1592.Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) | go see soln on leetcode
  * [ ] 11.1 -> [68.Text Justification](https://leetcode.com/problems/text-justification/) | go see soln on leetcode
* [x] 12-> [Split based on '\\'](https://leetcode.com/discuss/interview-question/1490881/Chances-of-google-L4)
* [ ] 13 -> [Max amount to rob a bank and Reach back to 0](https://leetcode.com/discuss/interview-question/1220530/Google-Phone-Screen-or-Graph)
* [x] 14-> [228.Summary Ranges](https://leetcode.com/problems/summary-ranges/) | go see soln on leetcode
* [ ] 15-> [947.Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)
* [x] 16-> [380.Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
* [x] 17-> [1910.Remove All Occurrences of a Substring](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)
* [x] 18-> [745.Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)
* [x] 19-> [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
* [x] 20-> [Put divider on screen to get minimum height on two text's split](https://leetcode.com/discuss/interview-question/1423422/Google-or-phone-screen)
* [x] 21-> [Minimum Number that doesnt occur in child subtree](https://leetcode.com/discuss/interview-question/1402524/Google-OA-For-FTE)
* [ ] 22-> [minimum number of swaps to be performed such that A\[i\] = i%3](https://leetcode.com/discuss/interview-question/1402524/Google-OA-For-FTE)
* [ ] 23-> [Snail Moving In Grid With Acceleration](https://leetcode.com/discuss/interview-question/1342117/Google-Interview-Phone)

{% tabs %}
{% tab title="10" %}
![](<../.gitbook/assets/Screenshot 2021-12-15 at 2.17.01 AM.png>)

```python
cnt = Counter(arr)
arr.sort()
for x in arr:
    if cnt[x] == 0: continue
    if x < 0 and x % 2 != 0: return False  # For example: arr=[-5, -2, 1, 2], x = -5, there is no x/2 pair to match
    y = x * 2 if x > 0 else x // 2
    if cnt[y] == 0: return False  # Don't have the corresponding `y` to match with `x` -> Return IMPOSSIBLE!
    cnt[x] -= 1
    cnt[y] -= 1
return True

```
{% endtab %}

{% tab title="10.1" %}
This problem is very similar to problem **0954**. Array of Doubled Pairs. (prev)

The idea is that for the smallest number there is unique way to find its pair. So, we sort numbers and then start from the smallest numbers, each time looking for pairs. If we can not find pair, return `[]`.&#x20;

The only difference, which costs me 5 minutes fine was that we need to deal with `0` as well.

**Complexity**

It is `O(n log n)` for time and `O(n)` for space.

```python
def findOriginalArray(self, arr: List[int]) -> List[int]:
    cnt, ans = Counter(arr), []
    for num in sorted(arr, key = lambda x: abs(x)):
        if cnt[num] == 0: continue
        if cnt[2*num] == 0: return []
        ans += [num]
        if num == 0 and cnt[num] <= 1: return []
        cnt[num] -= 1
        cnt[2*num] -= 1

    return ans
```
{% endtab %}

{% tab title="12" %}
```python
s = "I love leet\ code" # -> 'I', 'love', 'leet code']
s = "I love \\ leetcode"   # ->  'I', 'love', ' leetcode']

res = []
curr = ''
got_slash = False
for c in s:
    print(f'\t c = {c}')
    if c == ' ' and not got_slash:
        res.append(curr)
        curr = ''
    elif c == '\\':
        got_slash = True
        print(f'\t\t -> got_slash = {got_slash}')
    else:
        curr += c
res.append(curr)

print(res)
'''
"I love leet\ code" output ll be {"I", "love", "leet code"}. 

i missed cases like "I love \\ leetcode".

'''
```
{% endtab %}

{% tab title="13" %}
Djikstra might not help given u can revisit the same node or even re-use the same edge again&#x20;

This has similarity to the Travelling-Salesman-Problem but obviously quite different, since we can revisit the same bank again I propose a DFS from the starting-bank keeping track of the money we picked up from each bank, WITHOUT restricting us to come back to the same bank again as part of our route.&#x20;

We keep track of all the aux\_money, collected during our journey => until we reach start-bank anytime => thats when we dump this money to the collected\_money&#x20;

Good example to explain (4) would be something like: B3 ---------- B1 --------- B2 (with B1 being starting point)

```python
def maxRobbedMoneyWithinTime(edge_map, money_map, start_node, time_limit):
    @lru_cache(None)
    def dfs(u, T, collected_money, aux_money, visited_banks):
        bank_money = money_map[u] if u not in visited_banks else 0
        aux_money += bank_money
        if u == start_node:
            collected_money += aux_money
        if T<=0:
            return collected_money
            
        max_money = 0
        visited_banks.add(u)
        for v,travel_time in emap[u]:
            if travel_time > T:
                continue
            max_money = max(max_money, self.dfs(v, T-travel_time, collected_money, aux_money, visited_banks))
        visited_banks.remove(u)
        return max_money
    
    return dfs(start_node, time_limit, 0, 0, set())
```
{% endtab %}

{% tab title="16" %}
```python
import random

class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False
            
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
    
'''
TC: O(1)
'''
```
{% endtab %}

{% tab title="21" %}
```python
=> TC:: O(N) SC ::O(N)

def sol(root):
    def helper(node):
        if node is None:
            return set([]),0
        occur_left, least_left = helper(node.left)
        occur_right, least_right = helper(node.right)
        occur = occur_left | occur_right | set([node.val])
        least = max(least_left, least_right)
        while least in occur:
            least += 1
        node.val = least
        return occur, least
    _, _ = helper(root)
    return root
```
{% endtab %}

{% tab title="22" %}
```python
def minimumSwap(A):                                                     # variation of bucket sort O(N²) in place.
    n, res = len(A), 0
    for i in range(n):
        if A[i] == i % 3:                       continue                # excluding the one already in place.

        j, k = i + 1, n
        while j < n:                                                    # try to find swap candidate forwards;
            if A[j] == i % 3 and A[i] == j % 3: break                   # local optimum found to swap;
            if A[j] == i % 3 and A[j] != j % 3: k = j                   # be greedy, candidate except the one already in place on hold.
            j += 1

        if j == k == n:                         return -1               # can't swap.

        if j < n:                               A[i], A[j] = A[j], A[i] # optimal swap;
        else:                                   A[i], A[k] = A[k], A[i] # suboptimal swap;
        res += 1                                                        # count swap.

    return res


def minimumSwap(A):                                                     # O(N) w/ O(1) space, ideas @shk10
    pos = [[0] * 3 for _ in range(3)]
    for i in range(len(A)):
        pos[i % 3][A[i]] += 1

    once, twice = list(zip(*[(min(pos[i][j], pos[j][i]), pos[i][j] - pos[j][i]) for i, j in [(0, 1), (1, 2), (2, 0)]]))
    return twice[:-1] == twice[1:] and sum(once) + abs(twice[0]) * 2 or -1
```
{% endtab %}

{% tab title="23" %}
We know that

1 + 2 + ... + k = m + n\
let A = subset(1 + 2 + ... + k) = m\
then n = another part\
also 2 \* (1 + 2 + ... + k) = k \* (k+1) = 2 \* (m + n)\
we can probably check if m+n can be archieved by binary search O(log (m + n))

would be sth like this

```python
def get_K(m, n):
	left = 1
	right = m+n

	target = 2 * (m+n)

	while(left < right):
		mid = (left+right)//2
		res = (mid * (mid+1))
		if res == target:
			return k
		elif res < target:
			left = mid + 1
		else:
			right = mid - 1
	retrun -1
```

then it will be reduced to a knapsack problem

```python
@lru_cache
def knapsack(i, m):
	if i == k:
		if m == 0:
			return 1
		else:
			return 0
	else:
		choice1 = knapsack(i+1, m)
		choice2 = knapsack(i+1, m-i) if m >= i else 0
		return choice1 + choice2
```

This part takes O(k \* min(m, n)) time and space due to the cache, you can further reducing the space complexity by button up

Overall complexity would be O(log (m + n) + k \* min(m, n)), you may also convert the binary search part into equation and get the k in O(1)py
{% endtab %}
{% endtabs %}

* [ ] 24-> [1383.Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) 🐽
  * [ ] 24.2 -> [857.Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) 🐽
* [ ] 25 -> [startCost\[startIndex\] + endCost\[endIndex\] + abs(cord\[endIndex\] - cord\[startIndex\])](https://leetcode.com/discuss/interview-question/1302863/Google-L3-Rejected)
* [ ] 26 ->[ 1882.Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/) 🐽
* [ ] 27 -> [1834.Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

{% tabs %}
{% tab title="24" %}
```python
class Solution:
    def maxPerformance(self, n, S, E, k):
        sm, ans, heap = 0, 0, []
        
        for eff, speed in sorted(zip(E, S))[::-1]:
            if len(heap) > k - 1: sm -= heappop(heap)
            heappush(heap, speed)
            sm += speed
            ans = max(ans, sm*eff)
        
        return ans % (10**9 + 7)
        
        
'''
SOLN: https://leetcode.com/problems/maximum-performance-of-a-team/discuss/1252381/Python-short-heap-solution-explained
'''
```
{% endtab %}

{% tab title="27|1834" %}
```python
def getOrder(self, tasks: List[List[int]]) -> List[int]:
    res = []
    tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
    i = 0
    h = []
    time = tasks[0][0]
    while len(res) < len(tasks):
        while (i < len(tasks)) and (tasks[i][0] <= time):
            heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
            i += 1
        if h:
            t_diff, original_index = heapq.heappop(h)
            time += t_diff
            res.append(original_index)
        elif i < len(tasks):
            time = tasks[i][0]
    return res
```
{% endtab %}
{% endtabs %}

