# Regular Tree Problems

## 0. Notes



_Q. <mark style="color:orange;">**DFS vs BFS ?**</mark>. Which would be more efficient ? When would you prefer one over the other ?_

* <mark style="color:orange;">**Ans :**</mark> If you were to get such a problem in interview, it's very likely that the interviewer would proceed to ask a follow-up question such as this one.&#x20;
* The DFS vs BFS is a **vast topic of discussion**. But one thing that's for sure (and helpful to know) is <mark style="color:orange;">none is always better than the other</mark>. You would need to have an idea of probable structure of Tree/Graph that would be given as input (and ofcourse what you need to find depending on the question ) to make a better decision about which approach to prefer.
* A <mark style="color:orange;"></mark> <mark style="color:orange;"></mark><mark style="color:orange;">**DFS:**</mark> is <mark style="color:yellow;">easy to implement</mark> and <mark style="color:yellow;">generally has advantage of being space-efficient</mark>, <mark style="color:yellow;">especially in a balanced / almost balanced Tree</mark> and the space required would be `O(h)` (where `h` is the height of the tree) while we would require `O(2^h)` space complexity for **BFS** traversal which could consume huge amount of memory <mark style="color:yellow;">when tree is balanced & for</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`h`</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">is larger.</mark>
* **A **<mark style="color:orange;">**BFS:**</mark> On the other hand, **BFS** would <mark style="color:yellow;">perform well if you don't need to search the entire depth of the tree or if the tree is skewed and there are only few branches going very deep.</mark> In worst case, the height of a tree `h` could be equal to `n` and if there are huge number of nodes, <mark style="color:orange;">DFS would consume huge amounts of memory</mark> & may lead to <mark style="color:orange;">stackoverflow</mark>.
* In this question, the DFS performed marginally better giving better space efficiency than BFS. Again, this <mark style="color:yellow;">**depends on the structure of trees used**</mark> in the test cases.

## 1. Ancestor \[LCA]

* [x] [235. LCA of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) 📌
* [x] [236. LCA of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) 📌
  * [x] [1644. LCA of Binary Tree II](https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1644-lowest-common-ancestor-of-a-binary-tree-ii) - target node/s MAY NOT exist in tree | <mark style="color:yellow;">LCA + DFS</mark>
  * [x] [1650. LCA of Binary Tree III](https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1650-lowest-common-ancestor-of-a-binary-tree-iii) - parent to a node is given in Node definition | <mark style="color:yellow;">LCA + 2P</mark>
  * [x] [1483.Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) 📌 | template for binary lifting
    * [x] \=> [Errichto Video](https://www.youtube.com/watch?v=oib-XsjFa-M\&ab\_channel=Errichto)
* [x] [1026.Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)

{% tabs %}
{% tab title="235" %}
4 cases possible for rooted tree @x:

1. x is LCA
2. LCA lies on x.left
3. LCA lies on x.right
4. LCA doesnt exits in tree

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    def lca_bst(x,a,b):
        if not x:
            return None
        #1. if LCA lies on left
        if x.val > a.val and x.val > b.val:
            return lca_bst(x.left,a,b)

        #3. if LCA lies on right
        if x.val < a.val and x.val < b.val:
            return lca_bst(x.right,a,b)
        #3. x is lca
        return x

    return lca_bst(root, p,q)
    
'''
TC: O(H}
SC: O(1) - w/o function stack
'''        
```
{% endtab %}

{% tab title="236" %}
dda

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    def lca(x,a,b):
        if not x:
            return None
        # 1. if x's immediate children are a & b
        if (x.left == a and x.right == b) or (x.right == a and x.left == b):
            return x

        # 2. if x is same as a or b
        if x == a or x == b:
            return x

        left_lca = lca(x.left, a,b)
        right_lca = lca(x.right, a,b)

        if left_lca and right_lca:
            return x
        if left_lca:
            return left_lca
        return right_lca

    return lca(root, p,q)

'''
TC: O(H)
SC: O(1), w/o function stack

'''      
```
{% endtab %}

{% tab title="1644" %}
![](broken-reference) ![](<../../.gitbook/assets/Screenshot 2021-12-18 at 2.45.20 AM (1).png>)

```python
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not q or not p:
            return None
        self.count = 0
        res = self.dfs(root, p, q)
        if self.count == 2:
            return res
        return None

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root == p or root == q:
            self.count += 1    # one of the target node exists in tree
            return root

        if left and right:
            return root
        else:
            return left or right
```
{% endtab %}

{% tab title="1650" %}
![](broken-reference) ![](<../../.gitbook/assets/Screenshot 2021-12-18 at 2.45.20 AM.png>)

```python
    """
    # Definition for a Node.
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q    # switch to the other node's start
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p    # switch to the other node's start
        return p1
```
{% endtab %}

{% tab title="1483📌" %}
![](<../../.gitbook/assets/Screenshot 2021-12-04 at 4.34.59 PM.png>)

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

{% tab title="1026" %}
We pass the minimum and maximum values to the children,\
At the leaf node, we return `max - min` through the path from the root to the leaf.

```python
def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

    def solve(x, minn, maxx):
        if not x:
            return maxx - minn

        minn = min(minn, x.val)
        maxx = max(maxx, x.val)
        return max(solve(x.left,minn,maxx), solve(x.right,minn,maxx))
    return solve(root,root.val,root.val)
```
{% endtab %}
{% endtabs %}

## 2. **Root to leaf path problems**

* [x] ****[**257.** Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) - EASY
* [x] [112. Path Sum I](https://leetcode.com/problems/path-sum/)
* [x] [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
* [x] [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) ✅
* [x] [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)
* [ ] [1457.Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) 🐽

{% tabs %}
{% tab title="257" %}
```python
def recur(x,all_paths,this_path):
    # only add when x is leaf
    if x and not x.left and not x.right:
        if this_path:
            all_paths.append(this_path[2:] +'->' + str(x.val))
        else:
            all_paths.append(str(x.val))
        return 
    elif x:
        recur(x.left, all_paths, this_path + '->' + str(x.val))
        recur(x.right, all_paths, this_path + '->' + str(x.val))

all_paths = []
recur(root, all_paths, '')
return all_paths

'''
# Time complexity: O(N) since we visit every node of the tree once.
# Space complexity: O(N) since we are using the stack to fill the output and since we have the output as a list
'''
```
{% endtab %}

{% tab title="112" %}
```python
def recur(x,curr_sum):
    if not x:
        return False
    if x and not x.left and not x.right:    # if leaf
        if curr_sum - x.val == 0:
            return True
        return False

    found_on_left = recur(x.left, curr_sum - x.val)
    found_on_right = recur(x.right, curr_sum - x.val)
    return found_on_left or found_on_right


return recur(root,targetSum)
```
{% endtab %}

{% tab title="113" %}
```python
def recur(x,all_paths, curr_path):
    if not x:
        return

    if not x.left and not x.right and sum(curr_path) == targetSum:
        all_paths.append(curr_path)
        return

    if x.left: recur(x.left,all_paths, curr_path + [x.left.val])
    if x.right: recur(x.right,all_paths, curr_path + [x.right.val])

all_paths = []
if root:
    recur(root,all_paths,[root.val])
return all_paths
```
{% endtab %}

{% tab title="437" %}
```python
def recur(self,root, k):
    if root:
        return int(root.val == k) + self.recur(root.left, k - root.val) +  self.recur(root.right, k - root.val) 
    return 0

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    if root:
        return self.recur(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    return 0



'''
* The simplest solution is to traverse each node (preorder traversal) and then find all paths which sum to the target using this node as root.
* The worst case complexity for this method is N^2.
* If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2). This is the merge sort recurrence and suggests NlgN.
'''
```
{% endtab %}

{% tab title="1022" %}
```python
def bin_to_int(s):
    val = 0
    for i,c in enumerate(reversed(s)):
        val += pow(2,i)*int(c)
    return val

def solve(x, paths, curr):
    if not x:
        return
    if x and not x.left and not x.right:
        paths.append(curr + str(x.val))
        return 
    solve(x.left,paths, curr + str(x.val))
    solve(x.right,paths, curr + str(x.val))

paths = []
solve(root,paths, '')
print(paths)
ans = 0
for path in paths:
    ans += bin_to_int(path)
return ans

```
{% endtab %}
{% endtabs %}

## 3. **Serialize and Deserialise**

1.[https://leetcode.com/problems/serialize-and-deserialize-binary-tree/](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) Hard\
2.[https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) Medium\
3.[https://leetcode.com/problems/serialize-and-deserialize-bst/](https://leetcode.com/problems/serialize-and-deserialize-bst/)\
4.[https://leetcode.com/problems/serialize-and-deserialize-bst/](https://leetcode.com/problems/serialize-and-deserialize-bst/)



## 4. **Leaves related problem**

* [x] **📌 Get Height of Binary Tree**
* [x] ****[**404.**Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) 📌
* [x] [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)
* [x] [1325. Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

{% tabs %}
{% tab title="get_height" %}
```python
def get_height(root):
     if not root: return 0
      return 1 + max(get_height(root.left), get_height(root.right))
```
{% endtab %}

{% tab title="404" %}
![](<../../.gitbook/assets/Screenshot 2021-12-05 at 3.42.53 AM (1).png>)

```python
def recur(root):
    if not root:
        return 0
    if root and root.left and not root.left.right and not root.left.left:
        return root.left.val + recur(root.right)
    return recur(root.left)+recur(root.right)
return recur(root)
```
{% endtab %}

{% tab title="872" %}
```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        return self.findleaf(root1) == self.findleaf(root2)

    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)
```
{% endtab %}

{% tab title="1325" %}
```python
def removeLeafNodes(self, root, target):
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root
```
{% endtab %}
{% endtabs %}

## 5. Level Order Traversal

* [x] ****[**1161.** Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | 📌| standard\_bfs
* [x] [**865.** Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) ✅
* [x] [1104.Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) 🐽
* [x] [1377. Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/) ✅

{% tabs %}
{% tab title="1161" %}
Standard BFS - level order traversal

```python
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    Q = deque()
    Q.append((root,1))
    d = defaultdict(int)
    d[1] = root.val

    while Q:
        sz = len(Q)
        for _ in range(sz):
            u,l = Q.popleft()
            d[l] += u.val
            if u.left:
                Q.append((u.left,l+1))
            if u.right:
                Q.append((u.right,l+1))

    maxl, maxs = 0,float('-inf')
    for l,s in d.items():
        if maxs < s:
            maxl = l
            maxs = s
    return maxl
    
'''
Time & space: O(n), n is the number of total nodes.
'''    
```
{% endtab %}

{% tab title="865" %}
Write a sub function deep(TreeNode root).&#x20;

Return a pair(int depth, TreeNode subtreeWithAllDeepest)

In sub function deep(TreeNode root)->&#x20;

&#x20;      **if root == null,**&#x20;

&#x20;      \-> return pair(0, null)

&#x20;      **if left depth == right depth**,&#x20;

&#x20;      \-> deepest nodes both in the left and right subtree,&#x20;

&#x20;      \-> return pair (left.depth + 1, root)

&#x20;       **if left depth > right depth**

&#x20;         **->** deepest nodes only in the left subtree,&#x20;

&#x20;        \-> return pair (left.depth + 1, left subtree)

&#x20;       **if left depth < right depth**

&#x20;         **->** deepest nodes only in the right subtree,&#x20;

&#x20;        \-> return pair (right.depth + 1, right subtree)

<mark style="color:yellow;">**Complexity Time O(N) Space O(height)**</mark>

```python
def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(root):
            if not root: return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]: return l[0] + 1, l[1]
            elif l[0] < r[0]: return r[0] + 1, r[1]
            else: return l[0] + 1, root
        return deep(root)[1]
```
{% endtab %}

{% tab title="1104" %}
### Taken from: [soln](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O\(logn\)-time-and-space-with-readable-code-and-step-by-step-explanation)

![](<../../.gitbook/assets/Screenshot 2021-12-05 at 5.56.47 AM.png>)

```python
def pathInZigZagTree(self, label: int) -> List[int]:
    res = [] # O(log n) space
    node_count = 1
    level = 1
    # Determine level of the label
    while label >= node_count*2: # O(log n) time
        node_count *= 2
        level += 1
    # Iterate from the target label to the root
    while label != 0: # O(log n) time
        res.append(label)
        level_max = 2**(level) - 1
        level_min = 2**(level-1)
        label = int((level_max + level_min - label)/2)
        level -= 1
    return res[::-1] # O(n) time
    
'''
=> https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation

Time Complexity:
O(3 log n). 3 are needed as commented in the code.

Space Complexity:
If including the space required for the return res object counts as space then we need
O(log n) because we need to store the path from the root to the label.
'''
```
{% endtab %}

{% tab title="1377" %}
```python
def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
    if n == 1: return 1.0
    G = [[] for i in range(n + 1)]
    for i, j in edges:
        G[i].append(j)
        G[j].append(i)
    seen = [0] * (n + 1)
    
    def dfs(i, t):
        if i != 1 and len(G[i]) == 1 or t == 0:
            return i == target
        seen[i] = 1
        res = sum(dfs(j, t - 1) for j in G[i] if not seen[j])
        return res * 1.0 / (len(G[i]) - (i != 1))
    return dfs(1, t)
```
{% endtab %}
{% endtabs %}



## 6. **Distance between two Nodes**



## \*. Regular Tree Problems

* [x] \*\*\*\*[**Inorder Successor in Binary Search Tree**](https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/) ✅💪
* [x] 501\. [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | MindTickle!
* [x] 236\. [Find LCA in Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | **DnQ** | Standard ✅✅
* [x] Distance b/w 2 nodes in Tree: **`dist(a,b) = depth(a) + depth(b) - 2*depth(c) ; where c = lca(a,b)`**
* [x] LCA of N-ary tree ([article](https://medium.com/@sahilawasthi9560460170/lowest-common-ancestor-of-n-ary-tree-107fa772a939))
* [x] 1367.[ Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/)

{% tabs %}
{% tab title="InO_Succ✅" %}
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
        self.parent = None

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

{% tab title="236.lca✅" %}
```python
def lca(root,p,q) -> 'TreeNode':
        # found p and q?
        if not root or root == p or root == q:
            return root
    
        left = lca(root.left,p,q)
        right = lca(root.right,p,q)
        
        # p and q appears in left and right respectively, then their ancestor is root
        if left is not None and right is not None:
            return root
        
        # p and q not in left, then it must be in right, otherwise left
        if left is None:
            return right
        
        if right is None:
            return left
```
{% endtab %}

{% tab title="1367." %}
```python
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

    def dfs(head, root):
        if not head: return True
        if not root: return False
        return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
    if not head: return True
    if not root: return False
    return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

'''
Time O(N * min(L,H))
Space O(H)
where N = tree size, H = tree height, L = list length.
'''
```
{% endtab %}
{% endtabs %}

![LCA of N-ary Tree](../../.gitbook/assets/screenshot-2021-09-10-at-1.56.31-pm.png)

## # Resources

* LC:[ **Tree question pattern**](https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement)****
