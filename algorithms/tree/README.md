# --->Tree

## Notes:

* **DFS vs BFS:: How to Pick One?**
  1. Extra Space can be one factor (Explained below)
  2. **Depth First Traversals** are typically recursive and recursive code requires **function call overheads**.
  3. The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search something that is more likely to\*\* closer to root,\*\* we would prefer **BFS**. And if the target node is **close to a leaf**, we would prefer **DFS**.
* _Q. <mark style="color:orange;">**DFS vs BFS ?**</mark>. Which would be more efficient ? When would you prefer one over the other ?_
  * <mark style="color:orange;">**Ans :**</mark> If you were to get such a problem in interview, it's very likely that the interviewer would proceed to ask a follow-up question such as this one.&#x20;
  * The DFS vs BFS is a **vast topic of discussion**. But one thing that's for sure (and helpful to know) is <mark style="color:orange;">none is always better than the other</mark>. You would need to have an idea of probable structure of Tree/Graph that would be given as input (and ofcourse what you need to find depending on the question ) to make a better decision about which approach to prefer.
  * A <mark style="color:orange;"></mark> <mark style="color:orange;"></mark><mark style="color:orange;">**DFS:**</mark> is <mark style="color:yellow;">easy to implement</mark> and <mark style="color:yellow;">generally has advantage of being space-efficient</mark>, <mark style="color:yellow;">especially in a balanced / almost balanced Tree</mark> and the space required would be `O(h)` (where `h` is the height of the tree) while we would require `O(2^h)` space complexity for **BFS** traversal which could consume huge amount of memory <mark style="color:yellow;">when tree is balanced & for</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`h`</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">is larger.</mark>
  * **A **<mark style="color:orange;">**BFS:**</mark> On the other hand, **BFS** would <mark style="color:yellow;">perform well if you don't need to search the entire depth of the tree or if the tree is skewed and there are only few branches going very deep.</mark> In worst case, the height of a tree `h` could be equal to `n` and if there are huge number of nodes, <mark style="color:orange;">DFS would consume huge amounts of memory</mark> & may lead to <mark style="color:orange;">stackoverflow</mark>.
  * In this question, the DFS performed marginally better giving better space efficiency than BFS. Again, this <mark style="color:yellow;">**depends on the structure of trees used**</mark> in the test cases.
* **Rooting A Tree**: is like picking up the tree by a specific node and having all the edges point downwards
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

## ProblemSet

* [https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement](https://leetcode.com/discuss/interview-question/1337373/Tree-question-pattern-oror2021-placement)
* [https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem](https://leetcode.com/problems/path-sum/discuss/548853/recursive-solution-with-takeaway-to-solve-any-binary-tree-problem)

## Resources:

* Youtube playlist by \*\*WilliamFiset \*\* : [here](https://www.youtube.com/watch?v=0qgaIMqOEVs\&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P\&index=9\&ab\_channel=WilliamFiset)
* **Resources: Tree DP**
  * ✅Kartik Arora's Playlist: [Tree DP](https://www.youtube.com/watch?v=fGznXJ-LTbI\&list=PLb3g\_Z8nEv1j\_BC-fmZWHFe6jmU\_zv-8s\&ab\_channel=KartikArora)
  * Aditya Verma's Playlist: [TreeDP](https://www.youtube.com/watch?v=qZ5zayHSH2g\&list=PL\_z\_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn\&ab\_channel=AdityaVerma)
