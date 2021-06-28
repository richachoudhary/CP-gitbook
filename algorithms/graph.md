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

#### **1.2.1 Dijkstra  ::** `V+ElogE`

* Fastest among three
* Fails when _negative cycle_ exists in graph
* **IMPLEMENTATIONS:**
  * **1.2.1.1** Lazy Implementation
  * 1.2.1.2 Eager Implementation

**1.2.2 Bellman-Ford :: `VE`** 

* Use when _negative cycles_ exist in graph. 

**1.2.3 Floyd Warshall ::** $$V^3$$

{% tabs %}
{% tab title="1.1 Dijkstra" %}

{% endtab %}

{% tab title="1.2 Bellman-Ford" %}

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



























