---
description: Patterns & their problem list
---

# ✅Graph

## **Notes**

* Graph representation: use `defaultdict`

```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
from collections import defaultdict
graph = defaultdict(list)
# making adjacency list
for i,j,w in matrix:
    graph[i].append((j,w))
```



## 0. BFS/DFS : both `O(V+E)`

{% hint style="info" %}
FOR SHORTES PATH: **USE BFS!!!!!!!!!!!!!!!!!!!!**

**E.g.:** Below CSES: Labyrinth; DFS doesnt work!!!
{% endhint %}

{% tabs %}
{% tab title="" %}
```

```
{% endtab %}

{% tab title="BFS" %}
```python
from collections import deque

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
vis = [[False for _ in m]for _ in n]    # order of n & m is very imp here!!
def bfs(grid: List[List[int]])
    
    n, m = len(grid), len(grid[0])
    de = deque()
    de.append(K)
    vis[K] = True
    
    while de:
        top_x,top_y = de.popleft()
        for dx, dy in dirs:
            x = top_x + dx
            y = top_y + dy
            if 0<=x<n and 0<=y<m and not vis[x][y]:
                de.append((x,y))
                vis[x][y] = True    
```
{% endtab %}

{% tab title="DFS" %}
```python
dfs(x):
    vis[x] = True
    for i in graph[x]:
        if not vis[i]:
            dfs(i)
```
{% endtab %}

{% tab title="1254. Grid" %}
```python
''' If you hit a border, this is not an island '''
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
cnt = 0

N, M = len(grid), len(grid[0])
    
def dfs(sx,sy):
    if sx == 0 or sy == 0 or sx == N-1 or sy == M-1:
        return 0
    grid[sx][sy] = 2
    res = 1
    for dx,dy in dirs:
        x, y = sx+dx, sy+dy
        if 0<=x<N and 0<=y<M and grid[x][y]==0:
            res *= dfs(x,y)
    return res

for i in range(1,N-1):
    for j in range(1,M-1):
        if grid[i][j] == 0:
            cnt += dfs(i,j)
return cnt
```
{% endtab %}

{% tab title="932.✅BFS+DFS" %}
```python
N,M = len(g), len(g[0])
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
Q = deque()

def dfs(sx,sy):
    g[sx][sy] = 2           # paint this island with color '2'
    Q.append((sx,sy))
    
    for dx,dy in dirs:
        x, y = sx+dx , sy+dy
        if 0<=x<N and 0<=y<M and g[x][y] == 1:
            dfs(x,y)
            
#1. find first island & add to Q(for bfs later)
island1Found = False
for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            dfs(i,j)
            island1Found = True
            break
    if island1Found:
        break

#2. BFS - step by step expand island#1(col:2) until it collides with island#2(col:1)
dist = 0
while Q:
    # print(g)
    l = len(Q)
    for i in range(l):
        sx,sy = Q.popleft()

        for dx,dy in dirs:
            x, y = sx+dx , sy+dy
            if 0<=x<N and 0<=y<M:
                if g[x][y] == 1:
                    return dist
                if g[x][y] != 2:
                    g[x][y] = 2
                    Q.append((x,y))
    dist += 1
return -1


'''
elegant solution: =============================
1. First Do a DFS on one connected component, mark them visited, add them to the queue
2. Second Do a BFS to find the second connected component cause BFS guarantees Shortest Path optimally.

diagram: https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus
'''
```
{% endtab %}

{% tab title="MessageRoute" %}
```cpp
for(int i=0 ; i<m ; i++ )
{
    int u , v;
    cin >> u >> v ;
    g[u].pb(v);
    g[v].pb(u);
}
queue < int > q;
q.push( 1 );
par[1] = -1;
while( !q.empty() )
{
    int p = q.front() ;
    q.pop();
    if( p == n ) break;
    for( auto &i : g[p] )
        if( !par[i] ) par[i] = p , q.push( i );
}
if( par[n] )
{
    stack<int> s;
    s.push( n );
    int p = par[n] ;
    while( p != -1 )
    {
        s.push( p );
        p = par[p];
    }
    cout << (int)(s.size() ) << "\n";
    while( !s.empty() )
    {
        cout << s.top() << " " ;
        s.pop();
    }
}
else
    cout << "IMPOSSIBLE";
```
{% endtab %}

{% tab title="Monsters\| LavaFlow" %}
```python
n,m = I()

graph = []
monsters = []
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

#1. Construct lavas matrix ======================
lavas = [[float('inf') for _ in range(m)] for _ in range(n)]   #the min time when monster/laba reaches the cell
vis = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    s = str(input())
    row = []
    for j in range(len(s)):
        row.append(s[j])
        if s[j] == 'M':
            monsters.append((i,j))
        if s[j] == 'A':
            start = (i,j)
    graph.append(row)

q = deque()
# file lavas
for x,y in monsters:
    q.append((x,y,0))

while q:
    x,y,t = q.popleft()
    lavas[x][y] = min(lavas[x][y],t)

    for dx,dy in dirs:
        nx, ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '.' and lavas[nx][ny] > 1+t:
            q.append((nx,ny,t+1))

# for l in lavas:
#     print(l)
# 2. Make our player escape ===========================
def isEscape(x,y,t):
    return 0<=x<n and 0<=y<m and not vis[x][y] and graph[x][y] == '.' and lavas[x][y] > t

q = deque()
q.append((start[0],start[1],0,""))

while q:
    X,Y,T,path = q.popleft()
    vis[X][Y] = True
    if (X == n-1 or Y == m-1 or X == 0 or Y == 0) and (graph[X][Y]=='.') and T < lavas[X][Y]:
        print("YES")
        print(len(path))
        print(path)
        return
    
    x,y = X-1,Y
    if isEscape(x,y,T+1):
        q.append((x,y,T+1,path+"U"))
    x,y = X+1,Y
    if isEscape(x,y,T+1):
        q.append((x,y,T+1,path+"D"))
    x,y = X,Y-1
    if isEscape(x,y,T+1):
        q.append((x,y,T+1,path+"L"))
    x,y = X,Y+1
    if isEscape(x,y,T+1):
        q.append((x,y,T+1,path+"R"))
print("NO")

```
{% endtab %}
{% endtabs %}

* [x] CSES: [Message Route](https://cses.fi/problemset/task/1667/) \| BFS+backtrack ✅✅
* [x] [The Maze](https://leetfree.com/problems/the-maze)
* [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
* [x] [1020.Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)
* [x] [1376.Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)
* [x] [1254.Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)
* [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [x] [841.Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [x] [895. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
* [x] [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
* [x] [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
* [x] [1162.As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) \| **DP**\(2 traversal\)**:** \(i\) top\_to\_bottom \(ii\) bottom\_to\_top 
* [x] [994.Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) 🍊🍊
* [x] [1091.Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) //see 'Why DP doesnt work here!!'
  * _i.e. for a lonnngggg zigzag path going through \(7,0\)....-&gt;\(1,1\)-&gt;... ; by you wont have value of dp\[7\]\[0\] when you're calculating dp\[1\]\[1\]_
* [x] [797.All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) \| dfs + backtrack
* [x] [332.Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) \| dfs + backtrack ✅✈️
* [x] [1443.Minimum Time to Collect All Apples in a Tree](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) 🍎
* [x] [932.Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) \| **Google** \| BFS+DFS ✅
* [ ] CSES:[ Grid Paths](https://cses.fi/problemset/task/1625) ✅✅✅🐽\| [WilliamLin](https://www.youtube.com/watch?v=dZ_6MS14Mg4&t=2440s&ab_channel=WilliamLin)
* [x] CSES: [Labyrinth](https://cses.fi/problemset/task/1193) ==&gt; **DFS** fails, **ALWAYS USE BFS for SHORTEST PATH ✅✅**
* [x] **CSES:** [Monsters](https://cses.fi/problemset/task/1194) \| `Lava Flow Problem✅✅✅🔥🔥` \| [video](https://www.youtube.com/watch?v=hB59dxdDLII&ab_channel=Dardev)

## **1. Single Source Shortest/Longest Path - SSSP/SSLP** 

### **1.1 For DAGs**

#### **1.1.1 SSSP** 

* Can be done easily in `O(E+V)` using topological sort. 
* Ref [video](https://www.youtube.com/watch?v=TXkDpqjDMHA&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=17&ab_channel=WilliamFiset)

{% tabs %}
{% tab title="Logic" %}
```python
topo_list = [...]     # get any topological order of the DAG
dist = [sys.maxint]*n
dist[s] = 0
for node in topo_list:
    for x in node.neighbors:
        if dist[x] > dist[node] + graph[node][x].weight:
            dist[x] = dist[node] + graph[node][x].weight
```
{% endtab %}
{% endtabs %}

#### 1.1.2 SSLP 

* while SSLP on undirected graphs is **NP-HARD,** for DAGs, it could be easily solved in O\(E+V\). 
* **Logic**: 
  * multiply all edges with `-1` --&gt; find shorted path --&gt; multiply all edges with `-1` again
* Ref [video](https://www.youtube.com/watch?v=TXkDpqjDMHA&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=17&ab_channel=WilliamFiset)

### 1.2 For Graphs \(non-DAG wale\)

#### **1.2.1 Dijkstra  ::** `(V+E)logV`

* Fastest among three
* Fails when _negative cycle_ exists in graph
* **IMPLEMENTATIONS:**
  * **1.2.1.1** Lazy Implementation
    * **Why Lazy ?** because it inserts duplicate key-val pairs & then _lazily_ deletes them.
    * This is done because: insertion in PQ\(`NlogN`\) is more efficient than update\( `N` \) in PQ
    * **Why Bad:** for _dense_ graphs we end up with several _stale outdate_ key-value pair in PQ
  * **1.2.1.2** Eager Implementation
    * This avoids duplicate key-value pair & supports efficient value updates\( `logN`\) by using `Index PQ`

**1.2.2 Bellman-Ford :: `VE`** 

* Use when _negative cycles_ exist in graph. 

{% hint style="info" %}
**Negative Cycle** means there exists \(i\)a cycle OR \(ii\)self loop in graph, whose net sum == 0. Negative edges doesn't ensure negative cycle.

**How to find Negative Cycle:** using Bellman-ford.

* **Logic**: For a regular graph, shorted dist path to any node can have _atmax_ \(N-1\) nodes. But for _graph with negative cycle_, there are inf shorted path for the nodes in neg.cycle.
* Run the regular Bellman-ford : \(i.e. N-1\) times for the graph. After that do one more run; if any points distance updates =&gt; this is due to negative cycle =&gt; hence neg cycle exists.
{% endhint %}

**1.2.3 Floyd Warshall ::** $$V^3$$OR  $$V^2 $$ if MEMO is used!

* Its an **APSP**\(All Pair Shortest Path\) algo. Means it can find shortest distance b/w all 2 node pairs.
* **Code Optimisation:** use MEMOIZATION \(similar to _matrix chain multiplication_\) : see below code

{% tabs %}
{% tab title="1.2.1 Dijkstra" %}
```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
from collections import defaultdict
import heapq

def dijkstras_SSSP():
    graph = defaultdict(list)    
    for x,y,w in matrix:
        graph[x].append((y,w))
    
    dist = [float("inf")]*(n+1) # if nodes start from 1..n
    vis = [False]*(n+1) 
    
    heap = [(0,k)]
    dist[k] = 0
    
    while heap:
        W,s = heapq.heappop(heap)
        if vis[s] : continue
            
        vis[s] = True
        
        for y,w in graph[s]:
            if dist[y] > W + w:
                dist[y] = W + w
                heapq.heappush(heap,(dist[y],y))
    return dist
```
{% endtab %}

{% tab title="1.2 Bellman-Ford" %}
```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
def bellmanFord_SSSP(matrix):
    dist = [0] + [float("inf")] * N
    dist[k] = 0
    for node in range(1,N):        # relax each edge (N-1) times
        for u,v,w in matrix:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
#============ USAGE ==================
for _ in range(m):
    u,v,w = I()
    graph.append([u,v,w])

def bellmanFord(src):
    dist = [float("-inf")] * (n+1)
    dist[src] = 0
    for node in range(n+1):        # relax each edge (N-1) times
        for u,v,w in graph:
            dist[v] = min(dist[v],dist[u] + w)
    res1 = dist[n]

    #2. check for neg cycle
    for u,v,w in graph:
        old_v = dist[v]
        dist[v] = min(dist[v],dist[u] + w)
        if dist[v] != old_v:
            dist[v] = float('inf')    # Negative cycle detected
    res2 = dist[n]


    if res1 != res2:
        return '-1'
    return res1
```
{% endtab %}

{% tab title="Floyd-Warshall" %}
```python
n,m,q = I()

dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u,v,w = I()
    dp[u][v] = min(dp[u][v],w)
    dp[v][u] = min(dp[v][u],w)

#---------------------------------------------------------------------------
def floyd_warshall(n):
    # 1.form adj-matrix
    for i in range(1,n+1):
        dp[i][i] = 0

    #2. Apply dp similar to matrix-chain-multiplication
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
#---------------------------------------------------------------------------
floyd_warshall(n)

for _ in range(q):
    a,b = I()
    if dp[a][b] >= float('inf'):
        print('-1')
    else:
        print(dp[a][b])
```
{% endtab %}
{% endtabs %}

### 1.3 Algorithm Comparison for Shortest Path\(SP\) 

| - | BFS | Dijkstra's | BellmanFord | FloydWarshall |
| :--- | :--- | :--- | :--- | :--- |
| **Complexity** | `O(V+E)` | `O(ElogV)` | `O(EV)` | `O(V^3)` |
| **Recommended Graph Size** | large | large/medium | medium/small | small |
| **Good for APSP?** | only works on unweighted graphs | Ok | Bad | Yes |
| **Can Detect Neg. Cycles?** | No | No  | Yes | Yes |
| **SP on graph weighted graph** | Incorrect SP answer | Best Algorithm | Works | Bad in general |
| **SP on unweighted graph** | Best algorithm | Ok | Bad | Bad in general |

{% tabs %}
{% tab title="LongestFlighRoute" %}
```python
for _ in range(m):
    u,v = I()
    adj[u].append(v)

dist = [-1]*(n+1)
par = [-1]*(n+1)
res = []
dist[1] = 1
H = [(1,1)] # dist, node

while H:
    D,X = heappop(H)
    D = abs(D)
    dist[X] = D

    for x in adj[X]:
        if dist[x] < 1 + D:
            dist[x] = 1 + D
            par[x] = X
            heappush(H,(-dist[x],x))

if dist[n] == -1:
    print("IMPOSSIBLE")
else:
    res = [n]
    e = par[n]
    while e != -1:
        res.append(e)
        e = par[e]
    
    print(len(res))
    for i in reversed(res):
        print(i, end = " ")
```
{% endtab %}

{% tab title="FlightRoutes" %}
```python
n,m,k = I()
adj = defaultdict(list)
          
for _ in range(m):
    u,v,w = I()
    adj[u].append((v,w))
                         
dist = [[float('inf') for _ in range(k)] for _ in range(n+1)]
                      
H = [(0,1)] # dist,node
dist[1][0] = 0
         
while H:
    D,X = heappop(H)
                 
    for x,w in adj[X]:
        if dist[x][k-1] > w+D:
            dist[x][k-1] = w+D
            heappush(H, (dist[x][k-1],x))
            dist[x].sort()

# print(dist)
for e in dist[-1]:
    print(e, end = " ")
```
{% endtab %}
{% endtabs %}

### 1.x Problems: **SSSP/SSLP** 

* [x] [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)  🍪🍪
* [x] [1631.Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
* [x] [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)[ ✅](https://leetcode.com/problems/cheapest-flights-within-k-stops/

  )
* [ ] [882. Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)
* [x] [1514.Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) \| maxHeap
* [ ] [1334.Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
* [ ] [1368.Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
* [ ] [1786. Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/)
* [ ] [The Maze II](https://leetfree.com/problems/the-maze-ii)
* [ ] [The Maze III ](https://leetfree.com/problems/the-maze-iii)
* [x] [1928.Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) \| @contest 🚀❤️ \| **Google**
* [x] **CSES:** [Longest Flight Route](https://cses.fi/problemset/task/1680) \| print paths with `Dijkstras`
* [x] CSES: [Shortest Routes II](https://cses.fi/problemset/task/1672/) \| **`Floyd-Warshall |`**&lt;standardQ&gt; \| must do 🔖🍪🚀🔖
* [x] CSES: [High Score](https://cses.fi/problemset/task/1673/) \| **`Bellman-Ford`** `with Negative Cycle Detection`  \| &lt;standardQ&gt; \| must do  🔖🍪🚀🔖
* [x] CSES: [Cycle Finding](https://cses.fi/problemset/task/1197/) ✅🐽
* [x] CSES: [Flight Discount](https://cses.fi/problemset/result/2664805/) \| reversed dij: \| [approach](https://usaco.guide/problems/cses-1195-flight-discount/solution) ✅✅
* [x] CSES: [Flight Routes](https://cses.fi/problemset/task/1196) \| 2-D Dijkstras ✅✅ \| [approach](https://www.youtube.com/watch?v=009PBKHXtyA&ab_channel=Dardev)

  [  
  ](https://leetcode.com/problems/cheapest-flights-within-k-stops/

  )

 

 

## **2. MST** 

#### 2.1.1 Prim's Algo : `O(ElogE)`

* Its a greedy approach.
* Does well on _dense graphs_ \(better than Kruskal's\)
* Doesnt work well on disconnected graph; have to run it on each connected component individually.

#### 2.1.2 Kruskal's Algo

Prim: O\(\(V+E\)logV\) because each vertex is inserted in heap  
Kruskal : O\(ElogV\) most time consuming operation is sorting

{% tabs %}
{% tab title="Prims" %}
```python
heap = []
vis = set()
mst_dist = 0

heappush(heap,(0,1))    # w,x
while heap:
    w,x = heappop(heap)

    if x in vis:
        continue
    mst_dist += w
    vis.add(x)

    for j,jw in graph[x]:
        if j not in vis:
            heappush(heap,(jw,j))

if len(vis) < n:
    print(-1)
else:
    print(mst_dist)
```
{% endtab %}

{% tab title="Kruskals" %}
```python
def find(who,x):
    while who[x] != x:
        who[x] = who[who[x]]
        x = who[x]
    return x

def union(who,x,y):
    whox, whoy = who[x], who[y]
    who[whoy] = whox

graph = []

for _ in range(m):
    x,y,w = map(int,input().split())
    graph.append((x,y,w))

graph.sort(key = lambda x: x[2])    # the costliest step in complexity
who = [i for i in range(n+1)]

mst_dist,mst_nodes = 0,[]

for x,y,w in graph:
    whox, whoy = find(who,x),find(who,y)
    if whox != whoy:
        union(who,x,y)
        mst_dist += w
        mst_nodes.append([x,y])
if len(mst_nodes) != n-1:
    print(-1)
else:
    print(mst_dist)
```
{% endtab %}
{% endtabs %}

### 2.2 Problems: MST

* [x] [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) 💯
* [ ] [https://leetcode.com/problems/connecting-cities-with-minimum-cost/](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) 💲
* [ ] 
## 3. Topological Sort `O(V+E)`

* Only DAGs can have topological sorting\(graphs with a cycle CANNOT\)
* **How to find if graph has cycle?** =&gt; use **SCC algos** \(see section\#7: SCC below\)
* Most optimized Topological Sort implementation: **Kahn's Algo  =&gt;  `O(V+E)`**

  * **Logic**: Repeatedly remove the vertices with no dependencies

{% tabs %}
{% tab title="Kahn\'s Algo for Topological Sort\(BFS Way\)" %}
```python
graph = defaultdict(list)
indeg = [0 for _ in range(N)]
for x,y in prereq:
    graph[y].append(x)
    indeg[x] += 1
res,q = [],[]
for i in range(N):
    if indeg[i] == 0:
        q.append(i)
while q:
    e = q.pop()
    res.append(e)
    
    for j in graph[e]:
        indeg[j] -= 1
        if indeg[j] == 0:
            q.append(j)
return len(res) == N # check if all vertices are in topo OR is topo-traversal possible?
return res
```
{% endtab %}

{% tab title="TopoSort\(DFS way\)" %}
```python
def topological_sort():
    for each node:
        if visited[node] is False:
            dfs(node)

def dfs(node):
    visited[node] = True
    for nei in neighbours[node]:
        dfs(node)
	if visited(node) = false:
		ret.insert_at_the_front(node)
```
{% endtab %}

{% tab title="LongestFlightRoute" %}
```cpp
queue<int> q;
for(int i = 2; i <= n; ++i)
{
	if(inDegree[i] == 0)
	{
		q.push(i);	
	}
}
while(!q.empty())
{
	int u = q.front();
	q.pop();
	for(auto v: g[u])
	{
		--inDegree[v];
		if(inDegree[v] == 0)
			q.push(v);
	}
}
q.push(1);
cnt[1] = 1;
while(!q.empty())
{
	int u = q.front();
	q.pop();
	for(auto v: g[u])
	{
		--inDegree[v];
		cnt[v] = cnt[v] + cnt[u];
		cnt[v] %=  modb;
		if(inDegree[v] == 0)
			q.push(v);
	}
}
```
{% endtab %}
{% endtabs %}

### **3.2 Problems: Topological Sort**

* [x] [997.Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
  * [x] SIMILAR: [1557.Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)
  * **`return list(set(range(n)) - set(y for x,y in edges))`**
* [x] [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
* [x] [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
* [x] 1462.[Course Schedule IV](https://leetcode.com/problems/course-schedule-iv) ⭐️ \| see how to maintain all-inclusive prerequisite list 
* [x] [269. Alien Dictionary](https://leetfree.com/problems/alien-dictionary) 💲
* [x] [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) 💯
* [x] [444. Sequence Reconstruction](https://leetfree.com/problems/sequence-reconstruction) 💲
* [ ] [1203. Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)
* [ ] -------------------------------------- \[Medium\] -----------------------------------------------
* [ ] 851.[Loud and Rich](https://leetcode.com/problems/loud-and-rich)
* [ ] 802.[Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states)
* [ ] 1786. [Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node)
* [ ] 310. [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees)
* [ ] 444.[Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction)
* [ ] --------------------------------------- \[Hard\] ---------------------------------------------------
* [ ] 1591.[Strange Printer II](https://leetcode.com/problems/strange-printer-ii)
* [ ] 1916.[Count Ways to Build Rooms in an Ant Colony](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony)
* [ ] 1719.[Number Of Ways To Reconstruct A Tree](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree)
* [ ] 1857.[Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph)
* [ ] 631.[Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula)
* [ ] 1632.[Rank Transform of a Matrix](https://leetcode.com/problems/rank-transform-of-a-matrix)
* [x] CSES: [Longest Flight Route](https://cses.fi/problemset/task/1680) ✅





## **4. Union Find `O(logV)`**

### 4.1 Template

* [x] [684.Redundant Connection](https://leetcode.com/problems/redundant-connection/)
* [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) \| DSU in matrix graph ⭐️⭐️ 💯

{% tabs %}
{% tab title="684" %}
```python
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def find(who,x):                    # find
        if x != who[x]:
            who[x] = find(who[x])
        return who[x]                    #NOTE: dont do `return x` here!!!!!!!!
    
    def union(who,x,y):                 # union
        if x<y:
            who[find(y)] = find(x)
        else:
            who[find(x)] = find(y)
    
    n = len(edges)                
    who = [i for i in range(n+1)]        # init
    
    for x,y in edges:
        whox = find(who,x)
        whoy = find(who,y)
        if whox != whoy:
            union(who,x,y)
        else:
            return [x,y]
    return []
```
{% endtab %}

{% tab title="200. ⭐️" %}
```python
n,m = len(g), len(g[0])
        
cnt = sum(g[i][j] == 0 for i in range(n) for j in range(m))  #initialize to #0cells
who = [i for i in range(n*m)]    #just its id in a decoupled matrix

def find(x,y):
    while who[x] != x:
        who[x] = who[who[x]]
        x = who[x]
    return x
def union(cnt,x,y):
    whox,whoy = who[x],who[y]
    who[whoy] = whox                # x <--- y    
    cnt -= 1

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            if j<len(g[0])-1 :union(cnt,i,i+1)    #sequentially add down & right
            if i<len(g)-1 :union(cnt,i,i+j)
return cnt
```
{% endtab %}
{% endtabs %}

 

### 4.2 Problems

* [x] [721.Accounts Merge](https://leetcode.com/problems/accounts-merge/) 🐽
* [x] [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
* [x] [959.Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) \| 💯\| `/\\ /` 🤩
  * Convert every `/` into 3X3 matrix to boil this Q down to \#200.Number of Islands
* [x] [261. Graph Valid Tree](https://protegejj.gitbook.io/algorithm-practice/leetcode/union-find/261-graph-valid-tree)  💲\| check both: cycle & connected
* [x] [990.Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) \| ✅\| how to choose `x<---y`  OR `x-->y`in **`union()`**
  * Took one day & 7 fucking attempts to get it right!
* [x] [1697.Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) 🍪🍪🍪\|also the SMART way to retain index
* [x] [947.Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) \| leave everything & Do this!!  ✅🚀🚀
* [x] [1331.Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) \| tag:Easy
* [x] [1632.Rank Transform of a Matrix](https://leetcode.com/problems/rank-transform-of-a-matrix/) \| **GOOGLE!!!!..........last time 🐽🐽🐽**
* [x] CSES :[ Building Roads](https://cses.fi/problemset/task/1666) ✅
* [ ] [352.Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
* [ ] 128, [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/) 305, [https://leetcode.com/problems/number-of-islands-ii/](https://leetcode.com/problems/number-of-islands-ii/) 💲 1202, [https://leetcode.com/problems/smallest-string-with-swaps/](https://leetcode.com/problems/smallest-string-with-swaps/) 749, [https://leetcode.com/problems/contain-virus/](https://leetcode.com/problems/contain-virus/) 1627, [https://leetcode.com/problems/graph-connectivity-with-threshold/](https://leetcode.com/problems/graph-connectivity-with-threshold/) 1168, [https://leetcode.com/problems/optimize-water-distribution-in-a-village/](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) 1579, [https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) 1061, [https://leetcode.com/problems/lexicographically-smallest-equivalent-string/](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) 1101, [https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) 1258, [https://leetcode.com/problems/synonymous-sentences/](https://leetcode.com/problems/synonymous-sentences/) 1319, [https://leetcode.com/problems/number-of-operations-to-make-network-connected/](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) 737, [https://leetcode.com/problems/sentence-similarity-ii/](https://leetcode.com/problems/sentence-similarity-ii/) 990, [https://leetcode.com/problems/satisfiability-of-equality-equations/](https://leetcode.com/problems/satisfiability-of-equality-equations/) 924, [https://leetcode.com/problems/minimize-malware-spread/](https://leetcode.com/problems/minimize-malware-spread/) 928, [https://leetcode.com/problems/minimize-malware-spread-ii/](https://leetcode.com/problems/minimize-malware-spread-ii/) 839, [https://leetcode.com/problems/similar-string-groups/](https://leetcode.com/problems/similar-string-groups/) 711, [https://leetcode.com/problems/number-of-distinct-islands-ii/](https://leetcode.com/problems/number-of-distinct-islands-ii/)

{% tabs %}
{% tab title="990.✅" %}
```python
indeg = dict(zip(string.ascii_lowercase, [1]*26))
who = dict(zip(string.ascii_lowercase, string.ascii_lowercase))

def find(x):
    if who[x] != x:
        who[x] = find(who[x])
    return who[x]
def union(x,y):
    if indeg[x] == indeg[y]:
        who[find(x)] = find(y)
        indeg[x], indeg[y] = indeg[x]+1, indeg[y]+1
    elif indeg[x] > indeg[y]:
        who[find(y)] = find(x)
        indeg[x] += 1
    else:
        who[find(x)] = find(y)
        indeg[y] += 1

for x,sign,_,y in equations:
    if sign == '=':
        union(x,y)
        
for x,sign,_,y in equations:
    if sign == '!':
        if find(x) == find(y):
            return False
return True
```
{% endtab %}

{% tab title="947.✅🚀" %}
```python
'''
-> stones_to_be_removed = #total_stones - #forests(or Unions)
-> union row -> cols (to distinguish b/w row & col index, do col = col + 1000) 
'''
n = len(stones)
parent = [i for i in range(n)]  # id = index here

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x == parent_y:
        return 
    elif parent_x > parent_y:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x

# check if stones are connected
def check(i,j):
    return stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]

Xs = {} # set for x axis
Ys = {} # set for y axis
for i,(x,y) in enumerate(stones):
    if x not in Xs:
        Xs[x] = i
    if y not in Ys:
        Ys[y] = i

for i,(x,y) in enumerate(stones):
    if Xs[x] != i:
        union(i,Xs[x])
    if Ys[y] != i:
        union(i,Ys[y])

ans = 0
for i in range(n):
    if parent[i] != i:
        ans+=1

return ans
```
{% endtab %}

{% tab title="261.🔥" %}
```java
public boolean validTree(int n, int[][] edges) {
    List<Set<Integer>> adjList = new ArrayList<>();

    for (int i = 0; i < n; i++) {
        adjList.add(new HashSet<>());
    }

    for (int[] edge : edges) {
        adjList.get(edge[0]).add(edge[1]);
        adjList.get(edge[1]).add(edge[0]);
    }

    boolean[] visited = new boolean[n];

    // Check if graph has cycle
    if (hasCycle(0, visited, adjList, -1)) {
        return false;
    }

    // Check if graph is connected
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            return false;
        }
    }
    return true;
}

public boolean hasCycle(int node, boolean[] visited, List<Set<Integer>> adjList, int parent) {
    visited[node] = true;

    for (int nextNode : adjList.get(node)) {
        // (1) If nextNode is visited but it is not the parent of the curNode, then there is cycle
        // (2) If nextNode is not visited but we still find the cycle later on, return true;
        if ((visited[nextNode] && parent != nextNode) || (!visited[nextNode] && hasCycle(nextNode, visited, adjList, node))) {
            return true;
        }
    }
    return false;
}
```
{% endtab %}

{% tab title="1697.💪" %}
```python
# 1. DFS : O(N^2) fails for N = 10^5 =================================
def dfs(x,y,z):
    if x==y: return True
    vis[x] = True
    
    for j,wt in graph[x]:
        if not vis[j] and wt < z:
            if dfs(j,y,z):
                return True
    return False
        
res = []

graph = defaultdict(list)

for x,y,w in edgeList:
    graph[x].append((y,w))
    graph[y].append((x,w))

for x,y,w in queries:
    vis = [False for _ in range(N)]
    if dfs(x,y,w):
        res.append(True)
    else:
        res.append(False)
return res


# 2. DSU: NlogN (sorting) ===========================
'''
* Add edges to the graph from smallest to largest.
* Answer queries from smallest to largest.
* Use a Union-Find Data Structure to check connectivity.
'''

who = list(set(range(N)))
def find(x):
    while who[x] != x:
        who[x] = who[who[x]]
        x = who[x]
    return x

    
def union(x,y):
    whox, whoy = who[x], who[y]
    who[whox] = whoy    # x --> y
def areConnected(x,y):
    return find(x) == find(y)

# sort edges & queries by weight
e = deque(sorted((d,x,y) for (x,y,d) in edgeList))
q = list(sorted((lim,x,y,i) for i,(x,y,lim) in enumerate(queries)))

res = [False for _ in range(len(q))]

for lim,x,y,i in q:
    while e and e[0][0] < lim:
        _,u,v = e.popleft()
        union(u,v)            
    if areConnected(x,y):
        res[i] = True
return res
```
{% endtab %}

{% tab title="1632.🐽🐽" %}
```python
n, m = len(A), len(A[0])
rank = [0] * (m + n)
d = collections.defaultdict(list)
for i in range(n):
    for j in range(m):
        d[A[i][j]].append([i, j])

def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]

for a in sorted(d):
    p = list(set(range(m + n)))
    rank2 = rank[:]
    for i, j in d[a]:
        i, j = find(i), find(j + n)
        p[i] = j
        rank2[j] = max(rank2[i], rank2[j])
    for i, j in d[a]:
        rank[i] = rank[j + n] = A[i][j] = rank2[find(i)] + 1
return A

# https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/909142/Python-Union-Find
# https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/909212/C%2B%2B-with-picture
```
{% endtab %}

{% tab title="BuildingRoads" %}
```python
n,m = I()

who = dict()
for i in range(1,n+1):
    who[i] = i

def find(a):
    if a != who[a]:
        who[a] = find(who[a])
    return who[a]

def union(a,b):
    whoa,whob = find(a), find(b)
    who[whoa] = whob

for _ in range(m):
    a,b = I()
    union(a,b)

disjoints = []

for i in range(1,n+1):
    if who[i] == i:
        disjoints.append(i)

# print(who)
# print(disjoints)

print(len(disjoints)-1)
for i in range(0,len(disjoints)-1):
    print(f'{disjoints[i]} {disjoints[i+1]}')
```
{% endtab %}
{% endtabs %}

### **4.3 Resources:**

* [WilliamFiset videos](https://www.youtube.com/watch?v=ibjEGG7ylHk&ab_channel=WilliamFiset)

\*\*\*\*

## 5. **Graph colouring/Bipartition ⚪️🔴🔵**

* [x] \*\*\*\*[**785.** Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
* [x] [886.Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)
* [x] CSES:[ Building Teams](https://cses.fi/problemset/task/1668/) 

{% tabs %}
{% tab title="785" %}
```python
def dfs(src,col):
    if vis[src]:    # no need to process already visited node
        if color[src] != col:
            return False
        else:
            return True
    color[src] = col
    vis[src] = True
    for x in graph[src]:
        if not dfs(x,col^1):
            return False
    return True

color = [0 for _ in range(N)]  # 0:grey, 1:red, 2:blue
vis = [False for _ in range(N)]

# for every node- if not painted, paint red & do dfs
for i in range(N):
    if not vis[i]:
        if not dfs(i,1):
            return False
return True
```
{% endtab %}
{% endtabs %}

## 6. Cycle Detection

* **For Undirected graphs =&gt;** use DSU
* **For Directed graphs =&gt;** [Modified DFS](https://www.algotree.org/algorithms/tree_graph_traversal/depth_first_search/cycle_detection_in_directed_graphs/) \(**`inPath`**\)  OR topological ordering

{% tabs %}
{% tab title="1.Undir::DSU" %}
```python
''' 
=> use DSU on every edge
LOGIC: for 2 nodes(x,y) connected by an edge have same parent(z); they are in cycle
    # z-
    # | \
    # |  \
    # @   \
    # |    \
    # |     \
    # @      \
    # |       \
    # |        \
    # x----y----
'''
for x,y in edges:
    if who[x] == who[y]:
        return true    # cycle exists
    union(x,y)
```
{% endtab %}

{% tab title="2.1Direc::dfs" %}
```python
def dfs(x):
    vis[x] = True
    inPath[x] = True
    
    for j in graph[x]:
        if inPath[j]:
            return True        # cycle is present
        if not vis[j]:
            dfs(j)
    return False

vis = [False for _ in range(N)
inPath = [False for _ in range(N)]

for i in range(N):
    if not vis[i]:
        dfs(i)
```
{% endtab %}

{% tab title="2.2 Direc::topo" %}
```
Approach: 
In Topological Sort, the idea is to visit the parent node followed by the child node. 
If the given graph contains a cycle, 
    then there is at least one node which is a parent as well as a child 
    so this will break Topological Order.
     
Therefore, after the topological sort, 
    check for every directed edge whether it follows the order or not.
```
{% endtab %}

{% tab title="802." %}
```python
# find cycles in directed graph
MEMO = {}
def hasCycle(x,vis,inPath):
    if x in MEMO:
        return MEMO[x]
    vis[x] = True
    inPath[x] = True
    
    for j in graph[x]:
        if inPath[j]:
            MEMO[x] = True
            return True
        if not vis[j]:
            if hasCycle(j,vis,inPath):
                return True
    inPath[x] = False   # backtrack step
    MEMO[x] = False
    return False

N = len(adj)
graph = defaultdict(list)

for i,l in enumerate(adj):
    graph[i].extend(l)
    
cycleNodes = []

for i in range(N):
    vis = [False for _ in range(N)]
    inPath = [False for _ in range(N)]
    if hasCycle(i,vis,inPath):
        cycleNodes.append(i)

# print(cycleNodes)
return sorted(list(set(range(N)) - set(cycleNodes)))

```
{% endtab %}

{% tab title="RoundTrip" %}
```cpp
int n, m;
int sv, ev;
vector<vector<int>> g;
vector<int> vis;
vector<int> parent;
 
 
bool dfs(int u, int p)
{
	vis[u] = true;
	parent[u] = p;
	for(auto v: g[u])
	{
		if(v == p) continue;
		if(vis[v]) 
		{
			sv = v; 
			ev = u; 
			return true;
		} 
		if(!vis[v]) 
			if(dfs(v,u)) 
				return true;
	}
	return false;
}
 
 
bool visit_all()
{
	for(int i = 1; i <= n; ++i)
	{
		if(!vis[i])
			if(dfs(i,-1)) return true;
	}
	return false;
}
 
int32_t main()
{
	cin.tie(NULL);
	cin >> n >> m;
	g.resize(n+1);
	vis.resize(n+1);
	parent.resize(n+1);
	for(int i =0 ; i < m; ++i)
	{
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}
 
	if(!visit_all())
	{
		cout << "IMPOSSIBLE" << endl;
		return 0;
	}
 
	int tv = ev;
	vector<int> ans;
	ans.push_back(ev);
	while(tv != sv)
	{
		ans.push_back(parent[tv]);
		tv = parent[tv];
	}
	ans.push_back(ev);
	cout << ans.size() << endl;
	for(auto c: ans)
	{
		cout << c << " ";
	}
 
}
```
{% endtab %}

{% tab title="RoundTrip2" %}
```cpp
vector<set<int>> g;
vector<int> vis;
stack<int> recursionStack;
vector<bool> rsFlag;
 
bool dfs(int u)
{
	vis[u] = true;
	recursionStack.push(u);
	rsFlag[u] = true;
	for(auto v: g[u])
	{
		if(!vis[v])
			if(dfs(v))
				return true;
 
		if(rsFlag[v])
		{
			recursionStack.push(v);
			return true;
			//no more dfs;
		}
	}
	recursionStack.pop();
	rsFlag[u] = false;
	return false;
	//no cycle was detected
}
 
 
void visit_all()
{
	for(int u = 1; u <= n; ++u)
	{
		if(!vis[u])
		{
			if(dfs(u))
				break;
		}
	}
}
 
int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	g.resize(n+1);
	vis.resize(n+1);
	rsFlag.resize(n+1);
	for(int i = 0; i < m; ++i)
	{
		int u, v;
		cin >> u >> v;
		g[u].insert(v);
	}
	visit_all();
	if(recursionStack.empty())
	{		
		cout << "IMPOSSIBLE" << endl;
		return 0;
	}
 
	vector<int> ans;
	int temp = recursionStack.top();
	while(!recursionStack.empty())
	{
		ans.push_back(recursionStack.top());
		recursionStack.pop();
		if(ans.back() == temp and ans.size() != 1)
			break;
	}
	reverse(ans.begin(), ans.end());
	cout << ans.size() << endl;
	for(auto u: ans)
	{
		cout << u << " ";
	}
}
```
{% endtab %}
{% endtabs %}

### 6.3 Problems: Cycle Detection

* [x] [802.Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) .💯 
* [x] [886.Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)
* [x] CSES: [Round Trip](https://cses.fi/problemset/task/1669/) ✅✅ 🐽 \| Undirected Graph \|  cycle retrieval
* [x] CSES: [Round Trip II](https://cses.fi/problemset/task/1678) \| Directed Graph \| [Approach](https://www.youtube.com/watch?v=kzeAHV2Pw2o&ab_channel=Dardev)

## 7. SCCs \(Strongly Connected Cycles\)

* **What?** self contained cycles in graph in & from every vertex in cycle you can reach every other vertex.
* **Property:`SCC will always be disjoint from each other`**\(as shown in Kosaraju's. Ref:[ClementInterview](https://www.youtube.com/watch?v=qz9tKlF431k&ab_channel=Cl%C3%A9mentMihailescu)\)
* **Algos**: 

  * ✅Kosaraju's  =&gt; `O(V+E)`  :  [hackerearth](https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/tutorial/)  , [TusharRoy](https://www.youtube.com/watch?v=RpgcYiky7uw&ab_channel=TusharRoy-CodingMadeSimple)  
  * ❌Tarjan's       =&gt; `O(V+E)`  : [WilliamFiset\#23](https://www.youtube.com/watch?v=wUgWX0nc4NY&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=23&ab_channel=WilliamFiset)   \| wayyyy too sophisticated to apply in realtime

{% tabs %}
{% tab title="LOGIC:Kosaraju\'s" %}
```python
'''
1. do DFS on all nodes & build a stack of nodes based on their 'finish time'
2. reverse all edges
3. while stack has eles: pop ele from stack & do dfs; when done, we've got a SCC.

WHAT DO WE NEED TO IMPLEMENT:
* dfs1(), dfs2()
* a stack to keep finished nodes
* a set to keep visited nodes in both dfs's

WHY DOES THE ALGO WORKS:

THe Final SCC: 
(ABC)--->(DE)--->(F)-->(GHIJ) 
===> The final SCC will always be a Directed Acyclic Graph(DAG)
because if lets there was an edge from D-->A, the (ABCDE) would've been a SCC itself
'''
```
{% endtab %}

{% tab title="CODE:Kosaraju\'s" %}
```python
'''
1. do DFS on all nodes & build a stack of nodes based on their 'finish time'
2. reverse all edges
3. while stack has eles: pop ele from stack & do dfs; when done, we've got a SCC.
'''
def postorder_dfs(G):
    visited = set()
    postorder = []

    def helper(u):
        visited.add(u)
        for v in G[u]:
            if v not in visited:
                helper(v)
        postorder.append(u)    # u is 'finished' now, so add it to stack

    for u in set(G):
        if u not in visited:
            helper(u)
    return postorder


def reverse_graph(G):
    rev = defaultdict(set)
    for u in G.keys():
        for v in G[u]:
            rev[v].add(u)
    return rev


def kosaraju_scc(G):
    # First phase :: vertices in postorder ----------------
    postorder = postorder_dfs(G)

    # Second phase ----------------------------------------
    G = reverse_graph(G)

    visited = set()
    count = 0    # count of total SCCs in ans

    def dfs(u, scc):
        visited.add(u)
        scc.add(u)

        for v in G[u]:
            if v not in visited:
                dfs(v, scc)

    sccs = defaultdict(set)

    for u in reversed(postorder):
        if u not in visited:
            dfs(u, sccs[count])
            count += 1

    return sccs.values()
```
{% endtab %}

{% tab title="990." %}
```python
from collections import defaultdict
from typing import List


def postorder_dfs(G):
    visited = set()
    postorder = []

    def helper(u):
        visited.add(u)

        for v in G[u]:
            if v not in visited:
                helper(v)

        postorder.append(u)

    for u in set(G):
        if u not in visited:
            helper(u)

    return postorder


def reverse_graph(G):
    rev = defaultdict(set)

    for u in G.keys():
        for v in G[u]:
            rev[v].add(u)

    return rev


def kosaraju_sharir(G):
    # First phase
    # -----------

    # vertices in postorder
    postorder = postorder_dfs(G)

    # Second phase
    # ------------

    G = reverse_graph(G)

    visited = set()
    count = 0

    def dfs(u, scc):
        visited.add(u)
        scc.add(u)

        for v in G[u]:
            if v not in visited:
                dfs(v, scc)

    sccs = defaultdict(set)

    for u in reversed(postorder):
        if u not in visited:
            dfs(u, sccs[count])
            count += 1

    return sccs.values()


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        G = defaultdict(set)

        vertices = set()

        for eq in equations:
            if '==' in eq:
                x, y = eq.split('==')
                vertices.add(x)
                vertices.add(y)
                G[x].add(y)
                G[y].add(x)

        # build strongly connected components of equal numbers
        sccs = kosaraju_sharir(G)

        for x, e, _, y in equations:
            if e == '!':
                if x == y:
                    return False
                for scc in sccs:
                    # if x and y in  the same component - return false
                    if x in scc and y in scc:
                        return False

        return True
```
{% endtab %}
{% endtabs %}

### 7.1 Problems: SCCs

* [x] [990.Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)
* [x] **Clemment's interview**:[ Google Coding Interview With A High School Student](https://www.youtube.com/watch?v=qz9tKlF431k&ab_channel=Cl%C3%A9mentMihailescu) ✈️
* [x] [207.Course Schedule](https://leetcode.com/problems/course-schedule/) \| if SCC of len &gt; 1 exits ==&gt; there is cyclic dependency
* [x] [1192.Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
* [ ] [1520.Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)
* [ ] [https://leetcode.com/problems/number-of-operations-to-make-network-connected/](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)  🐽🐽
* [ ] [https://leetcode.com/problems/number-of-provinces/](https://leetcode.com/problems/number-of-provinces/) 🐽🐽
* [ ] [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/) 🐽🐽
* [ ] [https://leetcode.com/problems/critical-connections-in-a-network/](https://leetcode.com/problems/critical-connections-in-a-network/) 🐽🐽🐽
* [ ] [https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) 🐽🐽🐽
* [ ] [Airbnb \| Cover all vertices with the least number of vertices](https://leetcode.com/discuss/interview-question/algorithms/124861/airbnb-cover-all-vertices-with-the-least-number-of-vertices)

## 8. Euler Path & Circuits

* **Definitions:**
  * **Euler Path/Trail? =&gt;** a path of edges which visits every edge only once.
    * Depends on the starting vertex.
    * “Is it possible to draw a given graph without lifting pencil from the paper and without tracing any of the edges more than once”.
  * **Euler Circuit/Cycle ? =&gt;** an eulerian path which starts & ends at the same vertex.
    * If you know your graph has Euler Cycle, you can start from any vertex.
* **Conditions for Path & Circuits:**

<table>
  <thead>
    <tr>
      <th style="text-align:left">-</th>
      <th style="text-align:left"><b>Eulerian Path</b>
      </th>
      <th style="text-align:left">Eulerian Circuit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><b>Undirected Graph</b>
      </td>
      <td style="text-align:left">
        <ul>
          <li>Either every vertex has even degree.</li>
          <li>OR, exactly 2 vertexes have odd degree</li>
        </ul>
      </td>
      <td style="text-align:left">Every vertex has even degree.</td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Directed Graph</b>
      </td>
      <td style="text-align:left">
        <ul>
          <li>Exactly 2 vertex have: <b>abs(inDegree - outDegree) = 1</b>
          </li>
          <li>All other vertexes have equal InDegree &amp; outDegree.</li>
        </ul>
      </td>
      <td style="text-align:left">Every vertex has equal inDegree &amp; outDegree</td>
    </tr>
  </tbody>
</table>

### 8.1 Algos

* Eulers Path: [GfG](https://www.geeksforgeeks.org/eulerian-path-and-circuit/) \| see \#332. for algo: `O(E+V)` **\| Resource:** [this page](http://www.graph-magics.com/articles/euler.php)
* **Hierholzer's algorithm** for Euler Circuit: [GfG](https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/)

{% tabs %}
{% tab title="ALGO: Finding Euler Path" %}
```
1. Start with an empty stack and an empty circuit (eulerian path).
    - If all vertices have even degree - choose any of them.
    - If there are exactly 2 vertices having an odd degree - choose one of them.
    - Otherwise no euler circuit or path exists.
2. If current vertex has no neighbors - add it to circuit, remove the last vertex from the stack and set it as the current one. Otherwise (in case it has neighbors) - add the vertex to the stack, take any of its neighbors, remove the edge between selected neighbor and that vertex, and set that neighbor as the current vertex.
3.Repeat step 2 until the current vertex has no more neighbors and the stack is empty.

COMPLEXITY: O(V+E)
```
{% endtab %}

{% tab title="CODE:\(\#332.\) Finding Euler path" %}
```python
def dfs(x):
    while G[x]:
        i = G[x].pop()
        dfs(i)
    euler_path.append(x)

for x in G:
    G[x] = sorted(G[x], reverse = True)    # this sorting is specific to #332.

euler_path = []
dfs("JFK")        # "JFK" is the start node here
return euler_path[::-1]    # this reversing is part of the standard algo
```
{% endtab %}
{% endtabs %}

### 8.2 Problems

* [x] [332.Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) ✅✈️
* [ ] [753.Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/)   🐽🐽🐽 `+Google`
* [ ] [https://www.hackerearth.com/practice/algorithms/graphs/euler-tour-and-path/practice-problems/algorithm/wildcard-tree-problem-c2a1fbac/](https://www.hackerearth.com/practice/algorithms/graphs/euler-tour-and-path/practice-problems/algorithm/wildcard-tree-problem-c2a1fbac/) 



## **9. Articulation Point & Bridges\(bi-connected components\)**

* **Articulation Point:** The node, which if removed, will increase the number of connected components in graph.
  * Number of articulation points represent the **vulnerabilities in network**.
* **Algo** to find Articulation points: **Tarjan's algo** : **`O(V+E)`** \| [Abdul Bari](https://www.youtube.com/watch?v=jFZsDDB0-vo&ab_channel=AbdulBari) \(**see \#1192 for CODE**\)
* **Biconnected Graph** properties:
  1. It is connected, i.e. it is possible to reach every vertex from every other vertex, by a simple path.
  2. Even after removing any vertex the graph remains connected.

### 9.1 Problems

* [x] [1192.Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) ✅\| has Tarjan's algo implementation
* [ ] [https://leetcode.com/problems/minimize-malware-spread/](https://leetcode.com/problems/minimize-malware-spread/)
* [ ] [https://leetcode.com/problems/minimize-malware-spread-ii/](https://leetcode.com/problems/minimize-malware-spread-ii/)
* [ ] [https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)

{% tabs %}
{% tab title="1192.✅" %}
```python
def dfs(self, adj_map, dist, min_dist_child, visited, parent, i, n, curr_time, out):
    visited[i] = True
    dist[i] = min_dist_child[i] = curr_time+1
    for x in adj_map[i]:
        if visited[x]:
            if parent[i] != x:
                min_dist_child[i] = min(min_dist_child[i], dist[x])
        else:
            parent[x] = i
            self.dfs(adj_map, dist, min_dist_child, visited, parent, x, n, curr_time+1, out)
            min_dist_child[i] = min(min_dist_child[i], min_dist_child[x])
            if min_dist_child[x] > dist[i]:
                out.append([i, x])

def criticalConnections(self, n, connections):
    adj_map = {}
    for x in connections:
        if x[0] not in adj_map:
            adj_map[x[0]] = set()
        if x[1] not in adj_map:
            adj_map[x[1]] = set()

        adj_map[x[0]].add(x[1])
        adj_map[x[1]].add(x[0])

    out = []
    dist, min_dist_child, visited, parent = [float("Inf")]*n, [float("Inf")]*n, [False]*n, [-1]*n
    self.dfs(adj_map, dist, min_dist_child, visited, parent, 0, n, 0, out)

    return out
```
{% endtab %}
{% endtabs %}

## **10. Network Flow**

### 10.1.1 Ford-Fulkerson Algo

* **Logic:** The algo repeatedly finds **augmenting paths** through the **residual graph** & **augments the flow** until no more augmenting paths can be found.
* **Augmenting Paths?** =&gt; is a path of edges with flow capacity &gt; 0 from **source** to **sink.**
  * Every Augmenting path has a _bottleneck_ \(the smallest capacity wali edge\) 
* **Augmenting the flow?** =&gt; means updating the flow values of the edge along the augmenting path.
* **Ref:** [WilliamFiset](https://www.youtube.com/watch?v=LdOnanfc5TM&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=34&ab_channel=WilliamFiset)

{% hint style="info" %}
Ford Fulkerson gives **min-cut** value as byproduct!
{% endhint %}

### 10.1.2 Edmonds Karp Algo

### 10.1.3 Dinic's Algo

### 10.2 Problems:  **Maximum Flow**

## \*\*\*\*



























