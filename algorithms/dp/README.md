---
description: All the problems from LC, categorised
---

# ---> DP

### #There are two uses for dynamic programming:🟢🟢🟢

1. **Finding an optimal solution**: We want to find a solution that is as large as possible or as small as possible.
2. **Counting the number of solutions**: We want to calculate the total number of possible solutions.

## # Notes 

*  **Approach for DP problem: ** find Recursion **===>** Memoize it **===>** (optional) Top-Down OR matrix
* Using **MEMO** in python: (using **dict**-  constant lookup time)

```python
MEMO = {}
# ... use memo inside recur fn
if (a,b,c) in MEMO: return MEMO[(a,b,c)]
# find res & set in MEMO
MEMO[(a,b,c)] = res
#------------------------------------------
# Using python's built-in MEMO:
@lru_cache(None)
def solve().....
```

* Memoization vs Top-Down: (_both have same space & time complexities_)
  * **Recursion+Memoization **is easy to think & code.**should be your goto **approach for all DP ques.
    * in Rarest of rare cases; it might lead to _recursive stack overflow err_
  * **Top-Down: **nobody can write it w/o recursive. Avoid for new/unseen problems
    * If recursion+memo gives stack-overflow err, use Top-Down!

## Resources

* DP Patterns for Beginners: [https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions](https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions)
* **Solved all DP problems in 7 months: **[**https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months**](https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months)** **
* DP pattens list: [https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491](https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491)
* @youtube:
  * WilliamFiset Playlist: [https://www.youtube.com/watch?v=gQszF5qdZ-0\&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u\&ab_channel=WilliamFiset](https://www.youtube.com/watch?v=gQszF5qdZ-0\&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u\&ab_channel=WilliamFiset)
  * **✅Aditya Verma Playlist**: [https://www.youtube.com/watch?v=nqowUJzG-iM\&list=PL_z\_8CaSLPWekqhdCPmFohncHwz8TY2Go\&ab_channel=AdityaVerma](https://www.youtube.com/watch?v=nqowUJzG-iM\&list=PL_z\_8CaSLPWekqhdCPmFohncHwz8TY2Go\&ab_channel=AdityaVerma)
    * Good for problem classification & variety, but poor for intuition building
  * **✅Kartik Arora's Playlist: **[https://www.youtube.com/watch?v=24hk2qW_BCU\&list=PLb3g_Z8nEv1h1w6MI8vNMuL_wrI0FtqE7\&ab_channel=KartikArora](https://www.youtube.com/watch?v=24hk2qW_BCU\&list=PLb3g_Z8nEv1h1w6MI8vNMuL_wrI0FtqE7\&ab_channel=KartikArora)
* CF: list of all DP resource & questions:  [**DP Tutorial and Problem List**](https://codeforces.com/blog/entry/67679)\


