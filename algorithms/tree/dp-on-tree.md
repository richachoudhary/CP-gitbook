# DP on Tree

## 2. DP on Trees ✅ : // does the job in O(N)

* [CF tutorial](https://codeforces.com/blog/entry/20935?locale=en)

### 2.1 Trivial Questions

* [x] **BOOK#1: Number of nodes in subtree**

![](../../.gitbook/assets/screenshot-2021-09-10-at-12.43.41-pm.png)

* [x] **BOOK#2: Counting the number of paths till node X**

![](../../.gitbook/assets/screenshot-2021-09-10-at-1.13.22-pm.png)

* [x] **CF#1**: [Find max coins s.t. no two adjacent edges get collected](https://codeforces.com/blog/entry/20935?locale=en)
  * Do **`dfs()`** & build our dp1 & dp2

![CF#1](../../.gitbook/assets/screenshot-2021-09-12-at-2.07.09-am.png)

* [x] CSES:[ Tree Diameter](https://cses.fi/problemset/task/1131) ✅✅ | Basic level Tree DP | AdityaVerma | [KartikArora- N-ary tree](https://www.youtube.com/watch?v=qNObsKl0GGY\&list=PLb3g\_Z8nEv1j\_BC-fmZWHFe6jmU\_zv-8s\&index=3\&ab\_channel=KartikArora)
* [x] CSES: [Tree Distances I](https://cses.fi/problemset/task/1132) | aka. **`All Longest Paths`** | Same code as TreeDiameter=> use 2 dfs to get endpoints of dia ==> dfs b/w them | [underrated amazing video by HiteshTripathi](https://www.youtube.com/watch?v=Rnv4qvoxsTo\&ab\_channel=HiteshTripathi) 🚀✅✅🚀 | **must\_do**
* [x] LC: [Diameter of N-ary tree](http://leetcode.libaoj.in/diameter-of-n-ary-tree.html) | `TreeDistances I 's` code works here too

{% tabs %}
{% tab title="template" %}
```python
def f(node):
    #1. Base Condition
        if node is None: return 0
    #-----------------
    #2. HYPOTHESIS :: Recursive call on left & right 
        lr = f(node->left)
        rr = f(node-right)
    #------------------
    #3. INDUCTION :: Take decision & return it
         opt1 = g(lr,rr)    # case when 'node' cant be part of final ans
         opt2 = h()         # case when 'node cant be part of final ans
         
         return max(opt1, opt2)
```
{% endtab %}

{% tab title="CF#1." %}
```cpp
/ =====================================Complexity is O(N).

vector<int> adj[N];
int dp1[N],dp2[N];        //functions as defined above

//p is parent of node x
void dfs(int x, int p){

    //for storing sums of dp1 and max(dp1, dp2) for all children of V
    int sum1=0, sum2=0;

    //traverse over all children
    for(auto y: adj[x]){
        if(y == p) continue;
        dfs(y, x);        // ===> now we have calculated dp1[y] & dp2[y]
        sum1 += dp2[y];
        sum2 += max(dp1[y], dp2[y]);
    }

    dp1[x] = C[x] + sum1;
    dp2[x] = sum2;
}

int main(){
    int n;
    cin >> n;

    for(int i=1; i<n; i++){
    cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);
    int ans = max(dp1[1], dp2[1]);
    cout << ans << endl;
}
```
{% endtab %}

{% tab title="TreeDiameter" %}
```python
---------------------- works only for binary tree❌

def recurse(x):
    if not x: 
        return 0
    ldia = recurse(x.left)
    rdia = recurse(x.right)

    self.result = max(self.result, ldia+rdia)  # this is the dia of node x
    return 1 + max(ldia,rdia)  # passes this to its parent

self.result = 0
recurse(root)
return self.result    
    
------------------------- for n-arry tree✅
int n, ans;
vector<int> adj[MAX];
int d[MAX];
 
 void dfs(int u = 1, int p = -1){
     for(auto v:adj[u]){
         if(v==p)continue;
         dfs(v,u);
         ans = max(ans, d[u]+d[v]+1); # max v1--u--v2 
         d[u] = max(d[u],1+d[v]) # max v---u ::max depth of node u(i.e. longest path in its subtree)
     }
 }
 
int main() {
    cin >> n;
    for(int i=1;i<n;i++)
    {
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(1,-1);
    cout<<ans;
}
```
{% endtab %}

{% tab title="TreeDistance I" %}
```python
from collections import defaultdict

G = [[1,2],[2,3],[2,4],[3,5],[4,6]]
N = 6
adj = defaultdict(list)

for x,y in G:
    adj[x].append(y)
    adj[y].append(x)

def dfs(x,p,d):
    vis.add(x)
    par[x] = p
    dists[x] = d
    for y in adj[x]:
        if y not in vis and y != p:
            dfs(y,x,d+1)
            
#=================== DFS#1: getting one end of diameter: ndoe1
par = [-1]*(N+1)
dists = [0]*(N+1)
vis = set()

dfs(1,-1,0)     # start dfs from any arbitraily rooted node
node1 = -1
max_dist = float('-inf')

for i in range(1,N+1):
    if max_dist < dists[i]:
        node1 = i
        max_dist = dists[i]

print('node1 = ', node1)

#=================== DFS#1: getting the other end of diameter: ndoe2
par = [-1]*(N+1)
dists = [0]*(N+1)
vis = set()

dfs(node1,-1,0) # start dfs from tree rooted @node1
node2 = -1
max_dist = float('-inf')

for i in range(1,N+1):
    if max_dist < dists[i]:
        node2 = i
        max_dist = dists[i]

print('node2 = ', node2)

# node1 & node2 mil gye
# ab unse dfs call karo aur dists calculate karo

dists = [0]*(N+1)
vis = set()

dfs(node1,-1,0)
d1 = dists[::]

dists = [0]*(N+1)
vis = set()

dfs(node2,-1,0)
d2 = dists[::]

print(d1)
print(d2)
print(f'========> Tree Diameter = {d1[node2]}')

print('======== Now printing max longest paths for all nodes =========')
for i in range(1,N+1):
    print(f' Node: {i} => {max(d1[i],d2[i])}')
```
{% endtab %}

{% tab title="MaxPathSum" %}
```python
# From any node to any node
def solve(node):
    if node is null: return 0
    
    lsum = solve(node.left)
    rsum = solve(node.right)
    
    opt1 = max(node.val,                    # path startes from node
                node.val + max(lsum,rsum))  # 'node' is in beech-mei of path
    opt2 = max(node.val , lsum+rsum+node.val)
    return max(opt1, opt2)            
```
{% endtab %}

{% tab title="MaxLeafPathSum" %}
```python
# From Leaf node to leaf node
def solve(node):
    if node is None: return 0
    
    lsum = solve(node.left)
    rsum = solve(node.right)
    
    opt1 = node.val + max(lsum,rsum)  # 'node' is in beech-mei of path
    # path can start from node only if its a leaf node
    if node.left is None and node.right is None:
        opt1 = max(node.val, opt1)
        
    opt2 = max(lsum+rsum+node.val)
    return max(opt1, opt2) 
```
{% endtab %}

{% tab title="BOOk#2" %}
```python
def solve(G,N):
    adj = defaultdict(list)
    inDeg = [0]*(N+1)

    for x,y in G:
        adj[x].append(y)
        inDeg[y] += 1
        
    topo = []
    Q = deque()
    for i in range(1,N+1):
        if inDeg[i] == 0:
            Q.append(i)
    while Q:
        x = Q.popleft()
        topo.append(x)
        
        for y in adj[x]:
            inDeg[y] -= 1 
            if inDeg[y] == 0:
                Q.append(y)
                
    if len(topo) != N:
        return -1
    # print(topo
    ways = [0]*(N+1)
    ways[topo[0]] = 1
    for i in range(N):
        curr = topo[i]
        for x in adj[curr]:
            ways[x] += ways[curr]
    return ways[1:]


N = 6
G = [[1,2],[1,4],[4,5],[5,2],[2,3],[5,3],[3,6]]
res = solve(G,N)
print(res)
```
{% endtab %}
{% endtabs %}

###

### 2.2 Not-so trivial Questions

* [x] CSES: [Subordinates](https://cses.fi/problemset/task/1674) ✅
* [x] CSES: [Tree Distances II](https://cses.fi/problemset/task/1133) | \*\*`Tree Rerooting` ✅✅✅💪💪💪❤️❤️❤️| \*\*[video](https://www.youtube.com/watch?v=lWCZOjUOjRc\&t=42s)
  * **When is Rerooting DP applicable?**
  * \*\*===> \*\*when **given** `dp(x)`; you can calculated **`dp(y)`** for y:children\[x]
  * \========> mane; parent ki value mei kuch adjust karke uske children ki value nikali jaa sakti ho.
  * \========> e.g. \*\*Tree Distance ||(^) \*\*: get sum of all nodes from node X
  * **FINALLY SAMAJH AAYAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!❤️**
* [x] CSES: [Tree Matching](https://cses.fi/problemset/task/1130) | [kartikArora](https://www.youtube.com/watch?v=RuNAYVTn9qM\&list=PLb3g\_Z8nEv1j\_BC-fmZWHFe6jmU\_zv-8s\&index=2\&ab\_channel=KartikArora) ✅
* [x] CF: [Distance in Tree](https://codeforces.com/contest/161/problem/D) | #nodes at dist K from each other
* [x] 968.[Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | @kartikArora 📷✅✅✅✅✅✅✅✅
  * [x] LC [979.Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/) |**@uber**
* [x] 337\. [House Robber III](https://leetcode.com/problems/house-robber-iii/) ✅
* [x] 95\. [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) ✅| @MindTickle
* [x] 1339\. [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)| ❤️✅| looks so complicated, yet so easy
* [ ] [https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)
* [ ] [https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

faf

{% tabs %}
{% tab title="Subordinates" %}
```python
'''
TC: O(N)
'''
from collections import defaultdict
I = lambda : map(int,input().split())

# ===============================================
def dfs(x,p):
    dp[x] = 0
    
    for y in adj[x]:
        if y == p: continue
        dfs(y,x)
        dp[x] += 1+dp[y]

# ==============================================
n = int(input())
l = list(I())
adj = defaultdict(list)
dp = [0]*(n+1)
for i in range(2,n+1):
    adj[l[i-2]].append(i)
    
dfs(1,1)
print(dp[1:])
```
{% endtab %}

{% tab title="TreeDist2💪" %}
```python
# STEP:1 ======================= preprocessing :: rooted@1
def preprocess_dfs(x, p):

    subtree_size[x] = 1

    for y in adj[x]:
        if y != p:
            preprocess_dfs(y, x)
            subtree_size[x] += subtree_size[y]
            subtree_dist[x] += subtree_dist[y] + subtree_size[y]

# STEP:2 ======================= use values w.r.t 1 to get values for other nodes
def dfs(x, p):
    dp[x] = dp[p] - subtree_size[x] - subtree_dist[x] # detatch x from p
    dp[x] += n - subtree_size[x] + subtree_dist[x]    # add all nodes to x
    
    for y in adj[x]:
        if y != p:
            dfs(y,x)
            
n = int(input())
adj = defaultdict(list)
subtree_size = [0] * (n + 1)
subtree_dist = [0] * (n + 1)
dp = [0] * (n + 1)

for _ in range(n - 1):
    x, y = I()
    adj[x].append(y)
    adj[y].append(x)

# root the tree at any(here 1) node & preprocess values w.r.t. it
preprocess_dfs(1, -1)

# now use those precomputed values w.r.t. 1 to get values for other nodes
dp[1] = subtree_dist[1]
for x in adj[1]:
    dfs(x,1)

print(subtree_size)
print(subtree_dist)

print(dp[1:])
```
{% endtab %}

{% tab title="TreeMatching" %}
```cpp
/*
STATES: 
    * u : root node
    * picked = 0/1 : whether any edge(u--v) was picked 
ANS: max(dp(1,0), dp(1,1))
RECUR: 
    * dp(u,0) = SUM{ max(y,0), max(y,1) } for y:children[x]
    * dp(u,1) = SUM{max(y,0),max(y,1)}     # for y: c1...c(i-1)
                + 1 + dp(ci, 1)            # select this edge (u---ci)
                + SUM{max(y,0), max(y,1)}  # for y: c(i+1)....cn 
*/
vector<int>adj[MAX];
ll dp[MAX][2];
 
void dfs (int src){
    int leaf=1;
    dp[src][1]=0;
    dp[src][0]=0;

    for(auto child:adj[src]){
        leaf = 0;
        dfs(child);
    }
    if(leaf==1)return;

    for(auto child:adj[src]){
        dp[src][0]+=max(dp[child][0],dp[child][1]);
    }

    for(auto child:adj[src]){
        dp[src][1]=max(
                dp[src][1],
                1+ dp[child][0]+( dp[src][0]-max(dp[child][0],dp[child][1]))
            );
    }
}
 
 int main(){
     int n;
     cin>>n;
     for(int i=0;i<n-1;i++){
        int ss,ee;
        cin>>ss>>ee;
        adj[ss].push_back(ee);
     }
     dfs(1);
     cout<<max(dp[1][0],dp[1][1])<<endl;
}
```
{% endtab %}

{% tab title="968.📷✅" %}
```python
@lru_cache(None)
def minCameras(node=root, parent_covered=True, parent_camera=False):
    if not node: return 0
    camera_here = 1 + minCameras(node.left, parent_camera=True) + minCameras(node.right, parent_camera=True)

    if parent_camera:
        no_camera_here = minCameras(node.left) + minCameras(node.right)
        return min(camera_here, no_camera_here)

    if parent_covered:
        mincams = camera_here
        if node.right:
            mincams = min(mincams, minCameras(node.right, False) + minCameras(node.left, True))
        if node.left:
            mincams = min(mincams, minCameras(node.left, False) + minCameras(node.right, True))
        return mincams

    return camera_here

return minCameras()
```
{% endtab %}

{% tab title="97" %}
```cpp
res = 0
def distributeCoins(self, root):
    def dfs(root):
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        self.res += abs(left) + abs(right)
        return root.val + left + right - 1
    dfs(root)
    return self.res
```
{% endtab %}
{% endtabs %}

###

{% tabs %}
{% tab title="HouesRobber3" %}
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

{% tab title="95" %}
```python
 def solve(arr):
		#Base conditions
    if len(arr) < 1:
        return [None]
    if len(arr) == 1:
        return [TreeNode(arr[0])]
    
    ret = []
    for i,item in enumerate(arr):
        leftTrees = f(arr[0:i])
        rightTrees = f(arr[i+1:])
        
        for lt in leftTrees:
            for rt in rightTrees:
                r = TreeNode(arr[i])
                r.left = lt
                r.right = rt
                ret.append(r)
    return ret

return solve(list(range(1,n+1)))
```
{% endtab %}

{% tab title="1339.❤️✅" %}
```python
def maxProduct(self, root: Optional[TreeNode]) -> int:
        
    # dfs to get sum of subtree rooted @node
    def dfs(node):
        if not node: return 0
        ans = dfs(node.left) + dfs(node.right) + node.val
        res.append(ans)
        return ans
    
    res = []
    dfs(root)
    sum_all = max(res)
    return max(i*(sum_all-i) for i in res) % (10**9 + 7)
```
{% endtab %}

{% tab title="PlanetQueries!" %}
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e5+5;
const int MAXD = 30; // ceil(log2(10^9))

// number of planets and queries
int n, q;
// parent matrix where [i][j] corresponds to i's (2^j)th parent
int parent[MAXN][MAXD];

int jump(int a, int d) {
	for(int i=0; i<MAXD; i++) if(d & (1<<i))
		a = parent[a][i];
	return a;
}

int main() {
	cin >> n >> q;
	for(int i=1; i<=n; i++) {
		cin >> parent[i][0];
	}
	// evaluate the parent matrix
	for(int d=1; d<MAXD; d++){
	    for(int i=1; i<=n; i++) {
		    parent[i][d] = parent[parent[i][d-1]][d-1];
        }
	}   
	// process queries
	while(q--) {
		int a, d;
		cin >> a >> d;
		cout << jump(a, d) << '\n';
	}
}
/*
Time Complexity :  O(NlogN)
*/
```
{% endtab %}
{% endtabs %}





## 3. Binary Lifting

* [x] [1483.Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) 📌 | template for binary lifting
  * [x] \=> [Errichto Video](https://www.youtube.com/watch?v=oib-XsjFa-M\&ab\_channel=Errichto)
* [x] CSES#1: [Company Queries I](https://cses.fi/problemset/task/1687) | **`Binary Lifting` 💪✅✅❤️**
* [x] CSES#2: [Company Queries II](https://cses.fi/problemset/task/1688) | **`LCA + Binary Lifting` 🐽🐽**
* [ ] CSES: [Planets Queries I](https://cses.fi/problemset/task/1750) | Binary Lifting

{% tabs %}
{% tab title="1483" %}
![](<../../.gitbook/assets/Screenshot 2021-12-04 at 4.34.59 PM (1).png>)

```python
def __init__(self, n: int, parent: List[int]):
    self.LOG = 20   # log(5*(10^4))
    self.up = [[-1]*self.LOG for _ in range(n)]  # matrix dim: N*LOG      

    for j in range(self.LOG):
        for v in range(n):
            if j == 0: self.up[v][j] = parent[v]
            elif self.up[v][j-1] != -1:     #dont mess up with uncalculated values yet. eg: [-1,2,3,0]
                self.up[v][j] = self.up[ self.up[v][j-1] ][j-1]


def getKthAncestor(self, node: int, k: int) -> int:

    for j in range(self.LOG):
        if k & (1<<j):
            node = self.up[node][j]
        if node == -1:
            return node
    return node
'''
Complexities: 
    #1. Preprocessing => TC: O(N*logN), SC: O(N*logN)
    #2. Query=> O(LogN)
'''
```
{% endtab %}

{% tab title="CSES#1: Binary Lifting 101" %}
```python
"""
# Binary Lifting

up(u,x) : parent of node 'u' which is 2^x level up
x = log2(N)

TC: O(NlogN)

RECURSION:

* up(u,x) = up(up(u,x-1),x-1)   # because 2^(x-1) + 2^(x-1) = 2^x

BC:
1. up(u,0) = par[u]
2. up(root,x) = -1

"""

from collections import defaultdict
I = lambda: map(int, input().split())

def dfs(u, p):
    up[(u, 0)] = p  # BC.1

    # setup values for node u
    for i in range(1, 20):
        if (u, i - 1) in up and up[(u, i - 1)] != -1:
            up[(u, i)] = up[(up[u, i - 1], i - 1)]
        else:
            up[(u, i)] = -1  # BC.2
    # recurs on u's children
    for v in adj[u]:
        if v != p:
            dfs(v, u)

def query(x, k):
    if x == -1 or k == 0:
        return x

    for i in range(19, -1, -1):  # jump the highest --> lowest set bit
        if k >= (1 << i):
            return query(up[(x,i)], k - (1 << i))


n, q = I()
l = list(I())
adj = defaultdict(list)
up = {}

for i in range(2, n + 1):
    adj[i].append(l[i - 2])
    adj[l[i - 2]].append(i)

dfs(1, -1)
# print(up)
for _ in range(q):
    x, k = I()
    print(query(x, k))
```
{% endtab %}

{% tab title="CSES#2: LCA in LlogN" %}
```cpp
#include<bits/stdc++.h>
using namespace std;
  
int n, q, a, b, p[200005][20], d[200005];
  
int dp(int x){
    if (d[x]) return d[x];
    if (x == 1) return d[x] = 1;
    return d[x] = dp(p[x][0])+1;
}
int solve(int a, int b){
    int x = dp(a), y = dp(b);
    if (x > y){
        swap(a, b);
        swap(x, y);
    }
    y -= x;
    for (int i = 0; i < 20; i++){
        if (y & (1<<i)) b = p[b][i];
    }
    if (a == b) return a;
    for (int i = 19; i >= 0; i--){
        if (p[a][i] != p[b][i]){
            a = p[a][i];
            b = p[b][i];
        }
    }
    return p[a][0];
}
  
int main() {
    cin >> n >> q;
    for (int i = 2; i <= n; i++){
        cin >> p[i][0];
    }
    for (int i = 1; i < 20; i++){
        for (int j = 1; j <= n; j++){
            p[j][i] = p[p[j][i-1]][i-1];
        }
    }
    while (q--){
        cin >> a >> b;
        cout << solve(a, b) << "\n";
    }
}
```
{% endtab %}
{% endtabs %}

##

##
