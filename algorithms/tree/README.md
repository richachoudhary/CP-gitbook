# --->Tree

## Notes:

* **DFS vs BFS:: How to Pick One?**
  1. Extra Space can be one factor (Explained below)
  2. **Depth First Traversals** are typically recursive and recursive code requires **function call overheads**.
  3. The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. So if our problem is to search something that is more likely to\*\* closer to root,\*\* we would prefer **BFS**. And if the target node is **close to a leaf**, we would prefer **DFS**.
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
