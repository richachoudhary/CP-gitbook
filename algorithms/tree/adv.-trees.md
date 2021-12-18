# Adv. Trees

## 1. Trie

* [x] LC [208.Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) 📌
* [x] LC [212. Word Search II](https://leetcode.com/problems/word-search-ii/) ✅🚀 | trie+DFS
* [x] LC [14.Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)✅ 📌
* [x] LC [676.Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | trie+DFS
* [x] LC [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | trie+DFS
* [x] LC 421. [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | <mark style="color:orange;">`standardQ`</mark> | **@google | must\_do✅📌**

{% tabs %}
{% tab title="208.(TMPL)📌" %}
```python
from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)  # Easy to insert new node.
        self.isword = False  # True for the end of the trie.


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    '''
        TC: O(len(word))
    '''
    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.nodes[char]
        curr.isword = True

    '''
        TC: O(len(word))
    '''
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return True
        
'''
TC: of all operations is O(n), where n is the size of word. 
SC:                      O(M), where M is total lengths of all words
'''                
```
{% endtab %}

{% tab title="212🚀" %}
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

**Complexity**. This is difficult question, space complexity is needed to keep our `trie`, which is `O(k)`, where `k` is sum of length of all words. Time complexity is <mark style="color:orange;">`O(mn*3^T)`</mark>, where `m` and `n` are sizes of our board and `T` is the length of the longest word in `words`. Why? Because we start our `dfs` from all points of our board and do not stop until we make sure that the longest word is checked: if we are not lucky and this word can not be found on board we need to check potentialy to the length `T`. Why `3^T`? Because each time we can choose one of <mark style="color:orange;">three directions</mark>, except the one we came from.
{% endtab %}

{% tab title="14 ✅" %}
```python
from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_end = True
    
    def search(self,word):
        pass
    

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        
        for s in strs:
            trie.insert(s)
        
        root = trie.root
        res = ''
        while root:
            if len(root.children) > 1 or root.is_end:
                return res
            key = list(root.children)[0]
            res += key
            root = root.children[key]
            
        return res
```
{% endtab %}

{% tab title="676" %}
```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isEnd = True

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, words: List[str]) -> None:
        for w in words:
            self.trie.insert(w)

    def search(self, word: str) -> bool:
        def dfs(node, i, word):
            if i == len(word):
                return node.isEnd and self.modified
            if self.modified:
                if word[i] in node.children:
                    return dfs(node.children[word[i]], i + 1, word)
                else:
                    return False
            else:
                for c in node.children:
                    self.modified = c != word[i]
                    if dfs(node.children[c], i + 1, word):
                            return True
                return False
        
        self.modified = False
        return dfs(self.trie.root, 0, word)
```
{% endtab %}

{% tab title="211" %}
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, i, word):
            if i == len(word):
                return node.isEnd
            if word[i] == '.':
                for c in node.children:
                    if dfs(node.children[c], i + 1, word):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                else:
                    return dfs(node.children[word[i]], i + 1, word)
        
        return dfs(self.root, 0, word)
```
{% endtab %}

{% tab title="421" %}
(repeat from bitwise seciton)

{% tabs %}
{% tab title="421✅" %}
**Videos:**

* To understand logic: [this](https://www.youtube.com/watch?v=I7sUjln2Fjw\&ab\_channel=HellgeekArena)
* To understand code: [this](https://www.youtube.com/watch?v=jCu-Pd0IjIA\&ab\_channel=CodingNinjas)

**Approach:**

* O(N\*2) is trivial; so dont bother
* Greedy Approach: **bitwise+Trie**: `O(32*N)` ✅
  * 1 Build Bitwise tree with array
  * 2 for each ele in arr: greedily traverse the trie & get max possible xor value with it

```python
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, val):
        curr = self.root
        
        for i in range(31, -1, -1):
            bit = (val>>i)&1
            
            if bit == 0:
                if not curr.left:
                    curr.left = TrieNode()
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TrieNode()
                curr = curr.right

    def max_xor(self, A):
        max_xor_val = 0
        
        for i in range(len(A)):
            curr = self.root
            val = A[i]
            curr_xor = 0
            
            for j in range(31, -1, -1):
                bit = (val>>j)&1
                
                if bit == 0:
                    if curr.right:
                        curr_xor += 2**j
                        curr = curr.right
                    else:
                        curr = curr.left
                else:
                    if curr.left:
                        curr_xor += 2**j
                        curr = curr.left
                    else:
                        curr = curr.right
                        
            max_xor_val = max(max_xor_val, curr_xor)
            
        return max_xor_val
        
class Solution:
    def findMaximumXOR(self, A):
        t = Trie()
        for x in A:
            t.insert(x)
        return t.max_xor(A)
    

# TC: O(32*N) ================================================== 
```
{% endtab %}
{% endtabs %}
{% endtab %}
{% endtabs %}



## 2. Segment Trees

#### ( both: RSQ+RMQ implementations YAAAAAD honi chahiye)

* <mark style="color:orange;">**TC:**</mark> Tree Construction: ``` `<mark style="color:orange;">`O( n )`</mark>
* <mark style="color:orange;">**TC:**</mark> Query in Range: <mark style="color:orange;">`O( Log n )`</mark>
* <mark style="color:orange;">**TC:**</mark> Updating an element: <mark style="color:orange;">`O( Log n )`</mark>

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

{% tab title="IMPLEMENTATION(RSQ): efficient✅" %}
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

* [x] CSES: [Range Xor Queries](https://cses.fi/problemset/task/1650/) ✅✅ | Doable with both: prefix array & seg Tree
* [x] CSES: [Range Update Queries](https://cses.fi/problemset/task/1651) 🚀✅ | update on range & query on index => **hence use Lazy Propagation here**
  * \*\*NOTE: \*\*Lazy propagation isnt "just an alternative approach"
  * Normal Seg Tree implementation => update on **point** & query on **range**
  * Lazy Seg Tree implementation => update on **range** & query on **point**
* [ ] CSES: [Josephus Problem II](https://cses.fi/problemset/result/2607517/) 🐽✅
* [ ] SPOJ: [MKTHNUM](https://www.spoj.com/problems/MKTHNUM/)

### 3.3 BIT

* [ ] CSES: [Nested Range Check](https://cses.fi/problemset/task/2168) 🐽
* [ ] CSES: [Nested Range Count](https://cses.fi/problemset/task/2169) 🐽

## 4. Sparse Tables

* see vid of Errichto
