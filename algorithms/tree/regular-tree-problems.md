# Regular Tree Problems

## 1. Regular Tree Problems

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

##
