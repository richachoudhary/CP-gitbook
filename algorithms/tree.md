# Tree

## Notes:

* **DFS vs BFS:: How to Pick One?**
  1. Extra Space can be one factor \(Explained below\)
  2. **Depth First Traversals** are typically recursive and recursive code requires **function call overheads**.
  3. The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search something that is more likely to **closer to root,** we would prefer **BFS**. And if the target node is **close to a leaf**, we would prefer **DFS**.
* **Rooting A tTee**: is like picking up the tree by a specific node and having all the edges point downwards
  * Res: [https://towardsdatascience.com/graph-theory-rooting-a-tree-fb2287b09779](https://towardsdatascience.com/graph-theory-rooting-a-tree-fb2287b09779)
* Node:

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
...
root = TreeNode(x)
```

* ffs

## 1. Regular Tree Problems

* [x] \*\*\*\*[**Inorder Successor in Binary Search Tree**](https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/) ✅💪
* [x] 501. [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) \| MindTickle!

{% tabs %}
{% tab title="InO\_Succ✅" %}
```python
# Method 1: (Uses Parent Pointer) 
'''
1. If right subtree of node is not NULL, then succ lies in right subtree. 
    => Go to right subtree and return the node with minimum key value in the right subtree.
2. If right sbtree of node is NULL, then succ is one of the ancestors. 
    => Travel up using the parent pointer until you see a node which is
       left child of its parent. The parent of such a node is the succ.
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def inOrderSuccessor(n):
     
        # Step 1 of the above algorithm
        if n.right is not None:
            return minValue(n.right)
     
        # Step 2 of the above algorithm
        p = n.parent
        while( p is not None):
            #if n != p.right :
            if n == p.left :
                break
            n = p
            p = p.parent
        return p
     
    def minValue(node):
        current = node
     
        # loop down to find the leftmost leaf
        while(current is not None):
            if current.left is None:
                break
            current = current.left
     
        return current


# Method 2: w/o parent pointer
'''
1. If right subtree of node is not NULL, then succ lies in right subtree. 
    => {same as above}
2. If right sbtree of node is NULL, then succ is one of the ancestors. 
    => Travel down the tree, if a node’s data is greater than root’s data
      then go right side, otherwise, go to left side.
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def inOrderSuccessor(root, n):
     
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)
 
    # Step 2 of the above algorithm
    succ=Node(None)
     
    while( root):
        if(root.data<n.data):
            root=root.right
        elif(root.data>n.data):
            succ=root
            root=root.left
        else:
            break
    return succ
 
def minValue(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current is not None):
        if current.left is None:
            break
        current = current.left
 
    return current
 
```
{% endtab %}

{% tab title="501" %}
```python
#1. O(N) space ==================================================
    cnts = collections.Counter()
    self.maxx = 0
    
    def helper(node):
        # nonlocal maxx
        if not node:
            return
        cnts[node.val] += 1
        self.maxx = max(self.maxx, cnts[node.val])
        helper(node.left)
        helper(node.right)
        
    helper(root)
    return [k for k,v in cnts.items() if v == self.maxx]

    #2. O(1) Space ===================================================
    prev,count=0,0
    ans=[]
    c=0
    def inorder(root):
        nonlocal prev,count,c,ans
        if root:
            inorder(root.left)
            if prev==root.val:
                count+=1
            else:
                prev=root.val
                count=1
            if count>c:
                c=count
                ans=[root.val]
            elif count==c:
                ans.append(root.val)
            inorder(root.right)
    inorder(root)
    return(ans)
```
{% endtab %}
{% endtabs %}

##  2. DP on Trees

{% tabs %}
{% tab title="<template>⭐️" %}
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

{% tab title="TreeDiameter" %}
```python
---------------------- works only for binary tree
def dia(node):
    if not node: return 0     #1. BC
        
    ldia = dia(node.left)    #2. Hypothesis
    rida = dia(node.right)
    
    opt1 = max(ldia, rdia)        # when node isnt part of final ans
    opt2 = 1 + ldia + rdia        # when node is part of final ans
    return max(opt1, opt2)
------------------------- for n-arry tree
int n, ans;
vector<int> adj[MAX];
int d[MAX];
 
 void dfs(int u = 1, int p = -1){
     for(auto v:adj[u]){
         if(v==p)continue;

         dfs(v,u);
         ans = max(ans, d[u]+d[v]+1);
         d[u] = max(d[u],1+d[v]);
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
    dfs();
    cout<<ans;
}
```
{% endtab %}

{% tab title="TreeDistance I" %}
```cpp
vector<int>a[200005];
int vis[200005];
int d[200005];
int par[200005];
 
void dfs(int src, int p, int dis){
    vis[src]=1;
    d[src]=dis;
    
    for(auto i:a[src]){
        if(!vis[i] and i!=p){
            par[i] = src;
            dfs(i, src, dis+1);
        }
    }
}
 
 
int main(){
    cin>>n;
    for(int i=0;i<n-1;i++){
        int x, y;cin>>x>>y;
        a[x].pb(y);
        a[y].pb(x);
    }
    //==================================== DFS#1: to get one diameter end point
    memset(par, 0, sizeof(par));
    memset(vis, 0, sizeof(vis));
    memset(d, 0, sizeof(d));
    par[1]=0;
    dfs(1, par[1], 0);
    int node1 = -1 , node2 = -1 , ma = INT_MIN;
    for(int i=2;i<=n;i++){
        if(ma<d[i]){
            node1 = i;
            ma = d[i];
        }
    }
    
    //==================================== DFS#2: to get 2nd diameter end point
    ma=INT_MIN;
    memset(vis, 0, sizeof(vis));
    memset(d, 0, sizeof(d));
    dfs(node1 , 0 , 0);
    
    for(int i=1;i<=n;i++){
        if(ma<d[i] and i!=node1){
            node2 = i;
            ma = d[i];
        }
    }
    
    //node1 and node2 mil gaye...
    //ab unse dfs call kardo 
    //==================================== DFS#: to get diameter length
    
    memset(vis, 0, sizeof(vis));
    memset(d, 0, sizeof(d));
    dfs(node1, 0 , 0);
    vector<int>d1;d1.pb(0);
    for(int i=1;i<=n;i++){
        d1.pb(d[i]);
    }
    
    
    memset(vis, 0, sizeof(vis));
    memset(d, 0, sizeof(d));
    dfs(node2, 0 , 0);
    
    //cout<<d[node1]<<endl;            //for tree diameter
    for(int i=1;i<=n;i++){              //for max dist from each node
       cout<<max(d[i], d1[i])<<" ";
    }
    return 0;
}
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

{% tab title="Subordinates" %}
```python
adj = defaultdict(list)
dp = [0]*(n+1)

def dfs(x,par):
    res = 0
    for e in adj[x]:
        if e != par:
            dfs(e,x)
            res += 1 + dp[e]
    dp[x] = res

for i in range(2,n+1):
    x = A[i-2]
    adj[x].append(i)

dfs(1,0)
for e in dp[1:]:
    print(e, end = " ")
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

{% tab title="TreeDistance 2" %}
```cpp
vi ar[200001];
lli res[200001];
int subSize[200001];
lli subDist[200001];
int n;
 
// preprocessing - to fill subtree-dist & subtree-size arr ==================
void dfs1(int node , int par)
{
	subSize[node] = 1;
	
	for(int child : ar[node])
        if(child != par)
        {
            dfs1(child , node);
            subSize[node] += subSize[child];
            
            subDist[node] += subSize[child] + subDist[child];
        }
}
 
// rerooting node to get ans ==================================
void dfs(int node , int par)
{
	res[node] = (res[par] - subSize[node] - subDist[node]); //Rerooting1: remove contribution of self from parent's
    res[node] += n - subSize[node] + subDist[node];         //Rerooting2: add contribution of self in ans
	
	for(int child : ar[node])
	    if(child != par)
	        dfs(child , node);
}
 
int main()
{
	int a , b;
	cin>>n;
	REP(i , n-1) cin>>a>>b , ar[a].pb(b) , ar[b].pb(a);
	
	dfs1(1 , -1);
	res[1] = subDist[1];
	
	for(int child : ar[1])
	dfs(child , 1);
	
	REP(i , n) cout<<res[i]<<" ";
}
```
{% endtab %}
{% endtabs %}

* [x] CSES:[ Tree Diameter](https://cses.fi/problemset/task/1131) ✅✅ \| Basic level Tree DP \| AdityaVerma \| [KartikArora- N-ary tree](https://www.youtube.com/watch?v=qNObsKl0GGY&list=PLb3g_Z8nEv1j_BC-fmZWHFe6jmU_zv-8s&index=3&ab_channel=KartikArora)
* [x] CSES: [Subordinates](https://cses.fi/problemset/task/1674) ✅
* [x] CSES: [Tree Matching](https://cses.fi/problemset/task/1130) \| [kartikArora](https://www.youtube.com/watch?v=RuNAYVTn9qM&list=PLb3g_Z8nEv1j_BC-fmZWHFe6jmU_zv-8s&index=2&ab_channel=KartikArora) ✅
* [x] CSES: [Tree Distances I](https://cses.fi/problemset/task/1132) \| Same code as TreeDiameter=&gt; use 2 dfs to get endpoints of dia ==&gt; dfs b/w them \| [underrated amazing video by HiteshTripathi](https://www.youtube.com/watch?v=Rnv4qvoxsTo&ab_channel=HiteshTripathi) 🚀✅✅🚀 \| **must\_do**
* [x] CSES: [Tree Distances II](https://cses.fi/problemset/task/1133) \| **Tree Rerooting ✅🐽\|** [video](https://www.youtube.com/watch?v=lWCZOjUOjRc&t=42s)
* [x] CF: [Distance in Tree](https://codeforces.com/contest/161/problem/D) \| \#nodes at dist K from each other \| video
* [ ] CSES: [Company Queries I](https://cses.fi/problemset/task/1687) \| **LCA + Binary Lifting 🐽🐽**
* [ ] CSES: [Company Queries II](https://cses.fi/problemset/task/1688) \| **LCA + Binary Lifting 🐽🐽**
* [ ] CSES: 
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

## 3. Adv Trees 

### 3.1 Trie

{% tabs %}
{% tab title="208.\(TEMPLATE.py\)🔵🔴" %}
```python
from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)  # Easy to insert new node.
        self.isword = False  # True for the end of the trie.


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.nodes[char]
        curr.isword = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isword

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True
```
{% endtab %}

{% tab title="214.py🚀" %}
```python
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
```
{% endtab %}

{% tab title="14. cpp✅" %}
```python
struct TrieNode{
    TrieNode* children[26];
    int freq;
};

void insert(TrieNode* root, string s){
    TrieNode* node = root;
    for(char c:s){
        if(!node->children[c-'a']){
            TrieNode* child = new TrieNode();
            child->freq=1;
            node->children[c-'a'] = child;
        }else{
            node->children[c-'a']->freq += 1;
        }
        node = node->children[c-'a'];
    }
}

void traverse(TrieNode* root, string& ans, int size){
    for(int i=0;i<26;i++){
        if(root->children[i] && root->children[i]->freq == size){
            ans += (i+'a');
            traverse(root->children[i],ans,size);
        }
    }
}

string longestCommonPrefix(vector<string>& strs) {
    TrieNode* root = new TrieNode();
    root->freq=0;
    for(string s:strs){
        root->freq += 1;
        insert(root,s);
    }
    
    string ans="";
    traverse(root,ans,strs.size());
    return ans;
}
```
{% endtab %}
{% endtabs %}

* [x] LC [208.Implement Trie \(Prefix Tree\)](https://leetcode.com/problems/implement-trie-prefix-tree/) 🔴🔵
* [x] LC [214. Word Search II](https://leetcode.com/problems/word-search-ii/) ✅🚀
* [x] LC [14.Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)✅

### 3.2 Segment Trees \( both: RSQ+RMQ implementations YAAAAAD honi chahiye\)

* **Complexity:** Tree Construction: `O( n )` 
* **Complexity:** Query in Range: `O( Log n )` 
* **Complexity:**Updating an element: `O( Log n )`

{% tabs %}
{% tab title="IMPLEMENTATION: recursive" %}
```cpp
const int N = 100000;
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
    index+=n            # change the index to leaf node first
    tree[index] = value    # update the value at the leaf node at the exact index
    
    # after updating the child node,update parents
    i = index
    while i > 1: 
        tree[i//2] = tree[i] + tree[i+1]  #update parent by adding new left and right child
        i =i//2    # move up one level at a time in the tree

#RSQ for sum in range [l,r) ----> 0-based index
    # Basically the left and right indices will move
    # towards right and left respectively and with
    # every each next higher level and compute the
    # sum at each height. 
    
def queryTree(l, r):
    sum = 0
    l += n    #change the index to leaf node first
    r += n
    while l < r:
        if (l & 1):    #if left index in odd, make it even
            sum += tree[l]
            l += 1
        if (r & 1):
            r -= 1
            sum += tree[r]
        l =l// 2            # move to the next higher level
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
        
    # Basically the left and right indices will move
    # towards right and left respectively and with
    # every each next higher level and compute the
    # min at each height. 
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

{% tab title="RangeXORQueries" %}
```cpp
//1. with prefix arr =================================================
cin >> n >> q;
for (int i=1;i<=n;++i){
	cin >> a[i];
	a[i]^=a[i-1]; //Calculate the xor prefix sum
}
while (q--){
	cin >> u >> v;
	cout << (a[v] xor a[u-1]) << "\n";
}

//2. with Seg Tree ====================================================

const int mxN = 2e5 + 5;
ll t[4*mxN], a[mxN];

void build(int v, int tl, int tr){
    if (tl == tr){
        t[v] = a[tl];
        return;
    }
    int tm = (tl+tr)/2;
    build(2*v, tl, tm);
    build(2*v+1, tm+1, tr);
    t[v] = t[2*v] ^ t[2*v+1];
}
void update(int v, int tl, int tr, int l, int r, int val){
    if (tr < l || tl > r) return;
    if (l <= tl && tr <= r){
        t[v] += val;
        return;
    }
    int tm = (tl+tr)/2;
    upd(2*v, tl, tm, l, r, val);
    upd(2*v+1, tm+1, tr, l, r, val);
}
int query(int v, int tl, int tr, int l, int r){
    if (tr < l || r < tl) return 0;
    int tm = (tl+tr)/2;
    if (l <= tl && tr <= r){
        return t[v];
    }
    return get(2*v, tl, tm, l, r) ^ get(2*v+1, tm+1, tr, l, r);;
}
void solve(){
    int n, q; cin >> n >> q;
    for (int i = 1; i <= n; i++) cin >> a[i];
    build(1, 1, n);
    while (q--){
        int l, r; cin >> l >> r;
        int ans = query(1, 1, n, l, r);
        cout << ans << endl;
    }
}
 
```
{% endtab %}

{% tab title="RSQ:Lazy Propagation" %}
```python
N = 100000  # Upper limit for array size
tree = [0] * (2 * N)
lazy = [0] * (2 * N)
    
def buildTree(a,n):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = a[i]
    # creating parent node by adding left and right child
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]

# (ul,ur) : update ranges & (sl,sr) : Starting and ending indexes of elements for which current nodes stores sum
def updateRange(ul,ur,diff, sl,sr,index=0):    
    if lazy[index] != 0 :
        tree[index] += (sr - sl + 1) * lazy[index]    # Make pending updates using value  stored in lazy nodes 
  
        # checking if it is not leaf node because if it is leaf node then we cannot go further 
        if (sl != sr) :
            # Since we are not yet updating children of index, we need to set lazy flags for the children 
            lazy[index * 2 + 1] += lazy[index] 
            lazy[index * 2 + 2] += lazy[index] 
    
        lazy[index] = 0     # Set the lazy value for current node as 0 as it has been updated 
      
    # out of range :: what is valid :: ul----sl----sr-----ur || sl----ul----ur-----sr
    if (sl > sr or sl > ur or sr < ul) :
        return
  
    if (sl >= ul and sr <= ur) :    # Current segment is fully in range :: ul----sl----sr-----ur
        tree[index] += (sr - sl + 1) * diff    # Add the difference to current node 
  
        # same logic for checking leaf node or not 
        if (sl != sr) :
            lazy[index * 2 + 1] += diff 
            lazy[index * 2 + 2] += diff 
        return
  
    # If not completely in rang, but overlaps, recur for children, 
    mid = (sl + sr) // 2
    updateRange(ul, ur, diff, sl,mid,  index * 2 + 1)
    updateRange(ul, ur, diff,mid + 1,sr, index * 2 + 2)
  
    tree[index] = tree[index * 2 + 1] + tree[index * 2 + 2] # And use the result of children calls to update this node 
    
def queryTreeRSQ(ql, qr,sl,sr,index):
    # out of range 
    if (sl > sr or sl > qr or sr < ql) :
        return
    # do the pending updates first
    if (lazy[index] != 0) :
        # Make pending updates to this node.  
        # Note that this node represents sum of 
        # elements in arr[ss..se] and all these 
        # elements must be increased by lazy[index] 
        tree[index] += (sr - sl + 1) * lazy[index] 
  
        # checking if it is not leaf node because if t is leaf node then we cannot go further 
        if (sl != sr) :
            # Since we are not yet updating children os index, we need to set lazy values for the children 
            lazy[index * 2] += lazy[index] 
            lazy[index * 2 + 1] += lazy[index] 
  
        # unset the lazy value for current node as it has been updated 
        lazy[index] = 0 
  
    # At this point we are sure that  
    # pending lazy updates are done for  
    # current node. So we can return value
    # (same as it was for query in our previous post) 
  
    # If this segment lies in range 
    if (sl >= ql and sr <= qr)  :
        return tree[index] 
  
    # If a part of this segment overlaps with the given range 
    mid = (sl + sr) // 2
    return queryTreeRSQ(ql, qr,sl,mid ,2*index) + queryTreeRSQ(ql, qr,mid+1,sr, 2*index + 1); 

```
{% endtab %}
{% endtabs %}

* [x] CSES: [Range Xor Queries](https://cses.fi/problemset/task/1650/) ✅✅ \| Doable with both: prefix array & seg Tree
* [x] CSES: [Range Update Queries](https://cses.fi/problemset/task/1651) 🚀✅ \| update on range & query on index =&gt; **hence use Lazy Propagation here**
  * **NOTE:** Lazy propagation isnt "just an alternative approach"
  * Normal Seg Tree implementation =&gt; update on **point** & query on **range**
  * Lazy Seg Tree implementation      =&gt; update on **range** & query on **point**
* [ ] CSES: [Josephus Problem II](https://cses.fi/problemset/result/2607517/) 🐽✅

### 3.3 BIT 

* [ ] CSES: [Nested Range Check](https://cses.fi/problemset/task/2168) 🐽
* [ ] CSES: [Nested Range Count](https://cses.fi/problemset/task/2169) 🐽

 

## ProblemSet

* [https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement](https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement)
* [https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem](https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem)

## Resources:

* Youtube playlist by **WilliamFiset**  : [here](https://www.youtube.com/watch?v=0qgaIMqOEVs&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=9&ab_channel=WilliamFiset)



