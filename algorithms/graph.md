---
description: Patterns & their problem list
---

# Graph

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

#### **1.2.1 Dijkstra  ::** `V+ ElogE`

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
* Run the regular Bellman-ford : \(N-1\) times for the graph. After that do one more run; if any points distance updates =&gt; this is due to negative cycle =&gt; hence neg cycle exists.
{% endhint %}

**1.2.3 Floyd Warshall ::** $$V^3$$

{% tabs %}
{% tab title="1.2.1 Dijkstra" %}
```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
from collections import defaultdict
import heapq

def dijkstras_SSSS():
    graph = defaultdict(matrix)
    # making adjacency list
    for i,j,w in times:
        graph[i].append((j,w))
    heap = [(0,K)]
    dist = [0] + [float("inf")] * N
    vis = [False]*N         # (vis[] is needed only for optimisation; not logic)
    vis[k] = True                                   # optimisation :1
    while heap:
        src_dist,src = heapq.heappop(heap)
        vis[src] = True                             # optimisation :1
        if dist[src] > src_dist:
            dist[nei] = src_dist
            for j,w in graph[src]:
                if vis[j] == True: continue         # optimisation :1 
                heapq.heappush(heap,(src_dist+w,j))
        if src == X: return dist[src]                # optimisation :2
    return dist
```
{% endtab %}

{% tab title="1.2 Bellman-Ford" %}
```python
# input matrix = [[2,1,1],[2,3,1],[3,4,1]] : [from,to,weight]; src = k; dst = X
def bellmanFord_SSSS(matrix):
    dist = [0] + [float("inf")] * N
    dist[k] = 0
    for node in range(1,N):        # relax each edge (N-1) times
        for u,v,w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
```
{% endtab %}

{% tab title="Floyd-Warshall" %}

{% endtab %}
{% endtabs %}

### 1.x Problems

* [ ] [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)  🍪🍪

 

 

### **2. MST** 

Prim: O\(\(V+E\)logV\) because each vertex is inserted in heap  
Kruskal : O\(ElogV\) most time consuming operation is sorting

### 3. Topological Sort `O(V+E)`

### **4. Union Find `O(logV)`**

### 5. **Graph coloring/Bipartition**

### 6. Cycle Detection

6.1 for Directed graphs

6.2 gor Undirected graphs









## Resources:

* For patterns/templates:
  * [https://leetcode.com/discuss/general-discussion/971272/Python-Graph-Algorithms-One-Place-for-quick-revision](https://leetcode.com/discuss/general-discussion/971272/Python-Graph-Algorithms-One-Place-for-quick-revision)
  * [https://leetcode.com/discuss/general-discussion/655708/graph-for-beginners-problems-pattern-sample-solutions/](https://leetcode.com/discuss/general-discussion/655708/graph-for-beginners-problems-pattern-sample-solutions/)
  * DSU: [https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-\(DSU\)Union-Find-A-Complete-Guide](https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-%28DSU%29Union-Find-A-Complete-Guide)
* Youtube:
  * WilliamFiset's playlist: [https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab\_channel=WilliamFiset](https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab_channel=WilliamFiset)



























