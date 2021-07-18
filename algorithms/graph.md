---
description: Patterns & their problem list
---

# Graph

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

{% tabs %}
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
DFS-recursive(G, s):
    mark s as visited
    for all neighbours w of s in Graph G:
        if w is not visited:
            DFS-recursive(G, w)
```
{% endtab %}
{% endtabs %}

* [x] [The Maze](https://leetfree.com/problems/the-maze)
* [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
* [x] [1020.Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)
* [x] [1376.Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)
* [ ] [1254.Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)
* [ ] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* [x] [841.Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
* [ ] [895. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
* [ ] [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
* [ ] [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
* [ ] [1162.As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/)
* [x] [994.Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) 🍊🍊
* [x] [1091.Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) //see 'Why DP doesnt work here!!'
* [x] [797.All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) \| dfs + backtrack

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
```
{% endtab %}

{% tab title="Floyd-Warshall" %}
```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
def floydWarshall_SSSS(matrix):
    # adjacency matrix works best for FloydWarshall algo
    dist = [[float("inf") for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i] = 0    # dist of node from self: diagonal
    for u,v,w in matrix:
        dist[u-1][v-1] = w
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    
# DP relation ::makes code O(V^2) - implement similar to matrix-chain-multiplication
# LOGIC: dist(i,j) = min( dist(i,k) + dist(k,j)) for all nodes k other than i & j
if k==0 : dp[k][i][j] = matrix[i][j] 
else    : dp[k][i][j] = min( dp[k-1][i][j] ,dp[k-1][i][k] + dp[k-1][k][j] )    
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
* [x] [1929.Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) \| @contest 🚀❤️[ ](https://leetcode.com/problems/cheapest-flights-within-k-stops/

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
import heapq
import collections

def minimumCost(N: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a,b,w in connections:
        graph[a].append((b,w))
        graph[b].append((a,w))
    visited,cost = set(),0
    minHeap = [(0,1)]        # min Priority Queue
    while minHeap:
        minCost,city = heapq.heappop(minHeap)
        if city not in visited:
            cost += minCost
            visited.add(city)
            for nxt,c in graph[city]:
                if nxt not in visited:
                    heapq.heappush(minHeap,(c,nxt))
    return -1 if len(visited) < N else cost
```
{% endtab %}

{% tab title="Kruskals" %}
```python
def minimumCost(self, N: int, connections: List[List[int]]) -> int:
    def find(node,par):
        if par[node] == node:
            return node
        par[node] = find(par[node],par)
        return par[node]

    def union(a,b,par,rank1,a_rep,b_rep):
        parent_a, par_b = par[a], par[b]
        par[parent_a] = par[parent_b]=
            
    parent = [x for x in range(N+1)]
    res,i,e,result = 0,0,0,[]
    graph = sorted(connections,key = lambda x:x[2])
    while i < len(graph) and e < N - 1:
        u,v,w = graph[i]
        uroot,vroot = find(u,parent),find(v,parent)
        if uroot != vroot:
            result.append([u,v])
            res += w
            e += 1
            union(u,v,parent)
        i += 1
    if len(result) == N-1:
        return res
    else:
        return -1
```
{% endtab %}
{% endtabs %}

### 2.2 Problems: MST

* [ ] [https://leetcode.com/problems/connecting-cities-with-minimum-cost/](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
* [ ] 
## 3. Topological Sort `O(V+E)`

* Only DAGs can have topological sorting\(graphs with a cycle CANNOT\)
* **How to find if graph has cycle?** =&gt; use **SCC algos** \(see section\#7: SCC below\)
* Most optimized Topological Sort implementation: **Kahn's Algo  =&gt;  `O(V+E)`**

  * **Logic**: Repeatedly remove the vertices with no dependencies

{% tabs %}
{% tab title="Kahn\'s Algo for Topological Sort" %}
```python
from collections import defaultdict

def canFinish(N, prerequisites):
    graph,queue,cnt = defaultdict(list),[],0
    inDeg = [0] * N
    for j,i in prerequisites:
        graph[i].append(j)
        inDeg[j] += 1
    for i in range(numCourses):
        if inDeg[i] == 0:
            queue.append(i)
    while queue:
        ele = queue.pop(0)
        for j in graph[ele]:
            inDeg[j] -= 1
            if inDeg[j] == 0:
                queue.append(j)
        cnt += 1
    return queue
    # check if all vertices are in topo OR is topo-traversal possible?
    if cnt == N:
        return True
    else:
        return False
```
{% endtab %}
{% endtabs %}

### **3.2 Problems: Topological Sort**

* [x] [997.Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
  * [x] SIMILAR: [1557.Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)
  * **`return list(set(range(n)) - set(y for x,y in edges))`**
* [ ] 
## **4. Union Find `O(logV)`**

### 4.1 Template

* [x] [684.Redundant Connection](https://leetcode.com/problems/redundant-connection/)
* [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) \| DSU in matrix graph ⭐️⭐️ 💯

{% tabs %}
{% tab title="684" %}
```python
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def find(who,x):                    # find
        while who[x] != x:
            who[x] = who[who[x]]
            x = who[x]
        return x
    
    def union(who,x,y):                 # union
        whox = find(who,x)
        whoy = find(who,y)
        who[whox] = whoy
    
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
    who[whoy] = whoy
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
* [ ] 261, [https://leetcode.com/problems/graph-valid-tree/](https://leetcode.com/problems/graph-valid-tree/) 💲
* [ ] 1697, [https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) 352, [https://leetcode.com/problems/data-stream-as-disjoint-intervals/](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) 1434, [https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) 1632, [https://leetcode.com/problems/rank-transform-of-a-matrix/](https://leetcode.com/problems/rank-transform-of-a-matrix/) 128, [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/) 305, [https://leetcode.com/problems/number-of-islands-ii/](https://leetcode.com/problems/number-of-islands-ii/) 💲 1202, [https://leetcode.com/problems/smallest-string-with-swaps/](https://leetcode.com/problems/smallest-string-with-swaps/) 749, [https://leetcode.com/problems/contain-virus/](https://leetcode.com/problems/contain-virus/) 1627, [https://leetcode.com/problems/graph-connectivity-with-threshold/](https://leetcode.com/problems/graph-connectivity-with-threshold/) 1168, [https://leetcode.com/problems/optimize-water-distribution-in-a-village/](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) 1579, [https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) 1061, [https://leetcode.com/problems/lexicographically-smallest-equivalent-string/](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) 1101, [https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) 1258, [https://leetcode.com/problems/synonymous-sentences/](https://leetcode.com/problems/synonymous-sentences/) 1319, [https://leetcode.com/problems/number-of-operations-to-make-network-connected/](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) 737, [https://leetcode.com/problems/sentence-similarity-ii/](https://leetcode.com/problems/sentence-similarity-ii/) 990, [https://leetcode.com/problems/satisfiability-of-equality-equations/](https://leetcode.com/problems/satisfiability-of-equality-equations/) 924, [https://leetcode.com/problems/minimize-malware-spread/](https://leetcode.com/problems/minimize-malware-spread/) 928, [https://leetcode.com/problems/minimize-malware-spread-ii/](https://leetcode.com/problems/minimize-malware-spread-ii/) 839, [https://leetcode.com/problems/similar-string-groups/](https://leetcode.com/problems/similar-string-groups/) 711, [https://leetcode.com/problems/number-of-distinct-islands-ii/](https://leetcode.com/problems/number-of-distinct-islands-ii/)

### **4.3 Resources:**

* [WilliamFiset videos](https://www.youtube.com/watch?v=ibjEGG7ylHk&ab_channel=WilliamFiset)

\*\*\*\*

## 5. **Graph colouring/Bipartition**

## 6. Cycle Detection

6.1 for Directed graphs

6.2 for Undirected graphs

### 6.3 Problems: Cycle Detection

* [ ] [802.Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

## 7. SCCs \(Strongly Connected Cycles\)

* **What?** self contained cycles in graph in & from every vertex in cycle you can reach every other vertex.
* **Low link value:** the smallest node index which is reachable from the given node
* **Algos**: 

  * Kosaraju's  =&gt; `O(V+E)`  :  [hackerearth](https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/tutorial/)  , [TusharRoy](https://www.youtube.com/watch?v=RpgcYiky7uw&ab_channel=TusharRoy-CodingMadeSimple)  
  * Tarjan's       =&gt; `O(V+E)`  : [WilliamFiset\#23](https://www.youtube.com/watch?v=wUgWX0nc4NY&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=23&ab_channel=WilliamFiset)  

{% tabs %}
{% tab title="Kosaraju\'s" %}
```cpp
vector<vector<bool>> grev;
vector<vector<int> > fin;
vector<int> t;
vector<int> mark;
void dfs1(int node, int running){//scc 
    mark[node]=running;
    fin[running].push_back(node);
    for(int nex=0;nex<26;++nex){
        if(grev[node][nex]==0){continue;}
        if(mark[nex]==-1){
            dfs1(nex, running);
        }
        else if(mark[nex]!=running){
            t[mark[nex]]=(running);
        }
    }
}
vector<vector<bool>> g;
vector<int> topo;
vector<bool>vis;
void dfs(int node){
    vis[node]=true;
    for(int nex=0;nex<26;++nex){
        if(g[node][nex]==0){continue;}
        if(vis[nex]==false){
            dfs(nex);
        }
    }
    topo.push_back(node);
}
vector<string> maxNumOfSubstrings(string s) {
    int n=s.size();
    fin.resize(26);
    g.resize(26,vector<bool>(26,false));//initialisatin of the graph
    t.resize(26,-1);//initialisation of the scc
    grev.resize(26,vector<bool>(26,false));
    
    vis.resize(26,false);
    
    vector<int> eps(26,-1);//end position 
    vector<int> beg(26,-1);//beginning position
    
    for(int i=0;i<n;++i){
        if(beg[s[i]-'a']==-1){beg[s[i]-'a']=i;}
        eps[s[i]-'a']=i;
    }
    
    for(int ch=0;ch<26;++ch){
        
        if(beg[ch]!=-1){
            for(int i=beg[ch];i<=eps[ch];++i){
                g[ch][s[i]-'a']=true;
                grev[s[i]-'a'][ch]=true;
            }
        }
    }
    
    //finding topologically sorted array
    for(int i=0;i<26;++i){
        if(!vis[i] and beg[i]!=-1){
            dfs(i);
        }
    }//obtained topologically sorted array
    reverse(topo.begin(),topo.end());
    
    //finding scc
    mark.assign(26,-1);
    int cnt =0;
    for(auto it:topo){
        if(mark[it]==-1){dfs1(it,cnt);++cnt;}
    }
    vector<string> ans;
    for(int i=0;i<cnt;++i){
        if(t[i]==-1){
            int st=n,en=-1;
            for(auto it:fin[i]){
                st=min(st,beg[it]);
                en=max(en,eps[it]);
            }
            ans.push_back(s.substr(st,en-st+1));
        }
    }
    return ans;
    
    
}
```
{% endtab %}
{% endtabs %}

### 7.1 Problems: SCCs

* [ ] [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)  🐽🐽
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

* Eulers Path: [GfG](https://www.geeksforgeeks.org/eulerian-path-and-circuit/)
* **Hierholzer's algorithm** for Euler Circuit: [GfG](https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/)

{% tabs %}
{% tab title="Eulers path" %}
```text
#TODO:
```
{% endtab %}

{% tab title="Hierholzers Algo" %}
```
#TODO
```
{% endtab %}
{% endtabs %}

### 8.2 Problems: Euler Path & Circuits

* [ ] [https://leetcode.com/problems/reconstruct-itinerary/](https://leetcode.com/problems/reconstruct-itinerary/) 🐽🐽
* [ ] [https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) 🐽🐽
* [ ] [https://www.hackerearth.com/practice/algorithms/graphs/euler-tour-and-path/practice-problems/algorithm/wildcard-tree-problem-c2a1fbac/](https://www.hackerearth.com/practice/algorithms/graphs/euler-tour-and-path/practice-problems/algorithm/wildcard-tree-problem-c2a1fbac/) 
* [ ] [https://leetcode.com/problems/cracking-the-safe/](https://leetcode.com/problems/cracking-the-safe/)  🐽🐽🐽 `+Google`

## **9. Network Flow**

### 9.1.1 Ford-Fulkerson Algo

* **Logic:** The algo repeatedly finds **augmenting paths** through the **residual graph** & **augments the flow** until no more augmenting paths can be found.
* **Augmenting Paths?** =&gt; is a path of edges with flow capacity &gt; 0 from **source** to **sink.**
  * Every Augmenting path has a _bottleneck_ \(the smallest capacity wali edge\) 
* **Augmenting the flow?** =&gt; means updating the flow values of the edge along the augmenting path.
* **Ref:** [WilliamFiset](https://www.youtube.com/watch?v=LdOnanfc5TM&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=34&ab_channel=WilliamFiset)

{% hint style="info" %}
Ford Fulkerson gives **min-cut** value as byproduct!
{% endhint %}

### 9.1.2 Edmonds Karp Algo

### 9.1.3 Dinic's Algo

### 9.2 Problems:  **Maximum Flow**

## **10. Articulation Point & Bridges**

\*\*\*\*[https://leetcode.com/discuss/general-discussion/709997/questions-based-on-articulation-points-and-bridges/799168](https://leetcode.com/discuss/general-discussion/709997/questions-based-on-articulation-points-and-bridges/799168)

## Resources:

* For patterns/templates:
  * [https://leetcode.com/discuss/general-discussion/971272/Python-Graph-Algorithms-One-Place-for-quick-revision](https://leetcode.com/discuss/general-discussion/971272/Python-Graph-Algorithms-One-Place-for-quick-revision)
  * [https://leetcode.com/discuss/general-discussion/655708/graph-for-beginners-problems-pattern-sample-solutions/](https://leetcode.com/discuss/general-discussion/655708/graph-for-beginners-problems-pattern-sample-solutions/)
  * DSU: [https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-\(DSU\)Union-Find-A-Complete-Guide](https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-%28DSU%29Union-Find-A-Complete-Guide)
  * [https://leetcode.com/discuss/interview-question/753236/List-of-graph-algorithms-for-coding-interview](https://leetcode.com/discuss/interview-question/753236/List-of-graph-algorithms-for-coding-interview)
* Youtube:
  * \[\] WilliamFiset's playlist: [https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab\_channel=WilliamFiset](https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab_channel=WilliamFiset)



























