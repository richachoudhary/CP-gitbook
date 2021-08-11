# Tree

## Notes:

* **DFS vs BFS:: How to Pick One?**
  1. Extra Space can be one factor \(Explained above\)
  2. Depth First Traversals are typically recursive and recursive code requires function call overheads.
  3. The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search something that is more likely to closer to root, we would prefer BFS. And if the target node is close to a leaf, we would prefer DFS.

## 1. General Tree Problems



##  2. DP on Trees

* [ ] [https://leetcode.com/problems/unique-binary-search-trees-ii/](https://leetcode.com/problems/unique-binary-search-trees-ii/)
* [ ] [https://leetcode.com/problems/house-robber-iii/](https://leetcode.com/problems/house-robber-iii/)
* [ ] [https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)
* [ ] [https://leetcode.com/problems/linked-list-in-binary-tree/](https://leetcode.com/problems/linked-list-in-binary-tree/)
* [ ] [https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)
* [ ] [https://leetcode.com/problems/binary-tree-cameras/](https://leetcode.com/problems/binary-tree-cameras/)
* [ ] [https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

### 2.1 Resources: Tree DP

* ✅Kartik Arora's Playlist: [Tree DP](https://www.youtube.com/watch?v=fGznXJ-LTbI&list=PLb3g_Z8nEv1j_BC-fmZWHFe6jmU_zv-8s&ab_channel=KartikArora)
* Aditya Verma's Playlist: [TreeDP](https://www.youtube.com/watch?v=qZ5zayHSH2g&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&ab_channel=AdityaVerma)

## 3. Adv Trees Problems

### 3.1 Segment Trees

* **Complexity:** Tree Construction: `O( n )` 
* **Complexity:** Query in Range: `O( Log n )` 
* **Complexity:**Updating an element: `O( Log n )`

{% tabs %}
{% tab title="IMPLEMENTATION: recursive" %}
```cpp
onst int N = 100000;
int tree[2 * N];
 
void build(int node, int start, int end)
{
    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = A[start];
    }
    else
    {
        int mid = (start + end) / 2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, end);
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}

void update(int node, int start, int end, int idx, int val)
{
    if(start == end)
    {
        // Leaf node
        A[idx] += val;
        tree[node] += val;
    }
    else
    {
        int mid = (start + end) / 2;
        if(start <= idx and idx <= mid)
        {
            // If idx is in the left child, recurse on the left child
            update(2*node, start, mid, idx, val);
        }
        else
        {
            // if idx is in the right child, recurse on the right child
            update(2*node+1, mid+1, end, idx, val);
        }
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}

int query(int node, int start, int end, int l, int r)
{
    if(r < start or end < l)
    {
        // range represented by a node is completely outside the given range
        return 0;
    }
    if(l <= start and end <= r)
    {
        // range represented by a node is completely inside the given range
        return tree[node];
    }
    // range represented by a node is partially inside and partially outside the given range
    int mid = (start + end) / 2;
    int p1 = query(2*node, start, mid, l, r);
    int p2 = query(2*node+1, mid+1, end, l, r);
    return (p1 + p2);
}
```
{% endtab %}

{% tab title="IMPLEMENTATION\(RSQ\): efficient✅" %}
```python
N = 100000  # Upper limit for array size
tree = [0] * (2 * N)
    
def buildTree(a):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = a[i]
    # creating parent node by adding left and right child
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]

def updateTree(index, value):
    # set value at position index 
    tree[index + n] = value
    index+=n
    # after updating the child node,update parents
    i = index
    while i > 1: 
    #update parent by adding new left and right child
        tree[i//2] = tree[i] + tree[i+1]
        i =i//2

#RSQ for sum in range [l,r) ----> 0-based index
def queryTree(l, r):
    sum = 0
    l += n
    r += n
    while l < r:
        if ((l & 1)>0):
            sum += tree[l]
            l += 1
        if ((r & 1)>0):
            r -= 1
            sum += tree[r]
        l =l// 2
        r =r// 2
    return sum

                      
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7,8]
    n = len(A)

    buildTree(A)
    print(queryTree(1, 4))  # 0-based index
    updateTree(2, 5)
    print(queryTree(1, 4))
```
{% endtab %}

{% tab title="RMQ:eff ✅" %}
```python
N = 200005  # Upper limit for array size
tree = [0] * (2 * N)
    
def buildTree(a):
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[2*i],tree[2*i+1])    # diff

def updateTree(index, value):
    tree[index + n] = value
    index+=n
    i = index
    while i > 1: 
        tree[i//2] = min(tree[i],tree[i+1])    # diff
        i =i//2

def RMQ(l, r):
    l += n
    r += n
    res = min(tree[l],tree[r])
    while l < r:
        if (l & 1):
            res = min(res,tree[l])
            l += 1
        if (r & 1):
            r -= 1
            res = min(res,tree[r])
        l =l// 2
        r =r// 2
    return res

                      
if __name__ == '__main__':
    I = lambda : map(int, input().split())
    n,q = I()
    A = list(I())
    buildTree(A)

    for _ in range(q):
        l,r = I()
        l,r = l-1, r-1
        print(RMQ(l,r))
```
{% endtab %}
{% endtabs %}

* [ ] CSES: [Josephus Problem II](https://cses.fi/problemset/result/2607517/) 🐽✅

### 3.2 BIT 

* [ ] CSES: [Nested Range Check](https://cses.fi/problemset/task/2168) 🐽
* [ ] CSES: [Nested Range Count](https://cses.fi/problemset/task/2169) 🐽

 

## ProblemSet

* [https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement](https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement)
* [https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem](https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem)

## Resources:

* Youtube playlist by **WilliamFiset**  : [here](https://www.youtube.com/watch?v=0qgaIMqOEVs&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=9&ab_channel=WilliamFiset)



