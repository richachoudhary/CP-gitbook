# Recursion 💪

## Notes

* **Approaches** to solve a recursive problem:
  1. If you have to take **decisions** at every step =&gt; Make **Decision Tree** \(using **I/P O/P method**\)
     * You'll get the answer when **i/p is empty i.e.** at the **leaves** of decision tree
     * **Trick:** is to keep reducing input & keep increasing output::
     * **`f(ip,op) => f(smaller_ip, larger_op1) , f(smaller_ip, larger_op2) ,...`** 
     * See below:  ****`Print all subsets/powerset of a string`
  2. If the problem requires **reducing the input** at every step =&gt; use **BHI method**
     * I. **Hypotheses**: what will your function do \(_induction_\)
     * II. **Induction**: Apply that hypothesis on smaller input :: `main code` goes here
     * III. Write **base condition** i.e. _smallest valid input_ & include it in the beginning 
     * e.g.: find height of tree [video](https://www.youtube.com/watch?v=aqLTbtWh40E&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=5&ab_channel=AdityaVerma')
  3. If you've to take choices at every step: =&gt; Make **Choice Diagram** \(like **DP**\)

## 1. Recursion

* [x] Sort An Array **OR** Sort A Stack \(using BHI method\) - for concept building : [video](https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6&ab_channel=AdityaVerma)

{% tabs %}
{% tab title="Sort" %}
```python
def sortArr(arr):    # Hypothesis: fn sorts the arr
    # BC:    - empty arr is already sorted
    if len(arr) == 0: return 
    # INDUCTION
    last = arr[-1]
    arr.pop()
    sortArr(arr)
    insertMe(arr,last)    # flip page to see its implementation
    arr.append(last)
```
{% endtab %}

{% tab title="Insert" %}
```python
def insertMe(arr,x):  # HYPOTHESIS: fn inserts 'x' correctly inserted at its position in 'arr'
    # BC : if no ele or last ele < x, just insert 'x' at the end
    if len(arr) == 0 or arr[-1] < x:
        arr.append(x)
        return
    # INDUCTION - as n-th ele > x;remove last element & insert 'x' into arr[0:n-1] 
    last = arr[-1]
    arr.pop()
    insertMe(arr,x)
    arr.append(last)
```
{% endtab %}
{% endtabs %}

* [x] GfG: [Delete Middle Element of Stack](https://www.geeksforgeeks.org/delete-middle-element-stack/)
* [x] GfG: [Reverse A Stack w/o Extra Space](https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/)  \| [Video](https://www.youtube.com/watch?v=8YXQ68oHjAs&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=9&ab_channel=AdityaVerma) `O(1) ; not counting function stack`

{% tabs %}
{% tab title="reverseStack" %}
```python
def rerveseStack(stk):    #HYPOTHESIS: fn reverses my stack
    # BC:
    if len(stack) == 0: return
    # INDUCTION
    top = stk.pop()
    reverseStack(stk)
    insertMeAtBottom(stk,top)    # flip page to see its implementation
```
{% endtab %}

{% tab title="insertMeAtBottom" %}
```python
def insertMeAtBottom(stk,x): # HYPO: inserts 'x' at the bottom of stk
    # BC
    if len(stk) == 0:
        stk.append(x)
        return
    # INDUCTION
    top = stk.pop()
    insertMeAtBottom(stk,x)
    stk.append(top)
```
{% endtab %}
{% endtabs %}

* [x] [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)
* [x] CSES: [Tower of Hanoi](https://cses.fi/problemset/task/2165) \| [video](https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11&ab_channel=AdityaVerma) 

```python
def solve(n,s,d,h):    # no of plats, poles: source, destination, helper
    # BC
    if n == 1:
        print('moving plate {} from {} to {}'.format(n,s,d))
        moves += 1
        return
    solve(n-1,s,h,d)    # move (n-1) plates s->h
    print('moving plate {} from {} to {}'.format(n,s,d)) # move n-th plate s->d
    moves += 1
    solve(n-1,h,d,s)    # move those (n-1) plates h->d    
```

* [x] Print all subsets/powerset of a string \| [video](https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12&ab_channel=AdityaVerma) \| **Decision Tree method**

```python
def printSubsets(ip, op):
    if len(ip) == 0:
        print(op)
        return
    # choices: (1) print 1st ele of ip OR (2) dont print
    op1, op2 = op,op
    op1.append(ip[0])
    printSubsets(ip[1:],op1)     # choice 1
    printSubsets(ip[1:],op2)     # choice 2
    
printSubsets(str,'') # init with I/P & O/P
```

* [x] [Permutation with Spaces](https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1) \| [Video](https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14&ab_channel=AdityaVerma) : **NOTE:** Sometimes you've to break-down the problem before making recursion tree
* [x] ----------------------------- \[Medium\]---------------------------
* [x] [22.Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) 🚀
* [x] [1823.Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)
* [x] [241.Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)
* [x] [1545.Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)
* [ ] [394.Decode String](https://leetcode.com/problems/decode-string/) 🔒❌
* [ ] -------------------------------\[Hard\]----------------------------------
* [ ] CSES: [Josephus Problem II](https://cses.fi/problemset/task/2163) 🐽 \| KartikVarma-O\(N\*N\)...need to do better
* [ ] [10.Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
* [ ] [44.Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
* [ ] [1106.Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)
* [ ] [761.Special Binary String](https://leetcode.com/problems/special-binary-string/)
* [ ] [224.Basic Calculator](https://leetcode.com/problems/basic-calculator/)
* [ ] [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) 💲
* [ ] [770.Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/)
* [ ] [736.Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/)
* [ ] [strobogrammatic-number-iii](https://leetcode.com/problems/strobogrammatic-number-iii/) 💲
* [ ] [233.Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)
* [ ] [273.Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)



## 2. D&C

{% tabs %}
{% tab title="395." %}
```python
from collections import Counter
def longestSubstring(self, s: str, k: int) -> int:
    
    cnt = collections.Counter(s)
    st = 0
    maxst = 0
    for i, c in enumerate(s):
        if cnt[c] < k:
            maxst = max(maxst, self.longestSubstring(s[st:i], k))
            st = i + 1
    return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))


'''
The idea is that any characters in the string that do not satisfy the requirement
break the string in multiple parts that do not contain these characters, 
and for each part we should check the requirement again
'''
        
```
{% endtab %}
{% endtabs %}

* [x] [241.Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) ✅
* [ ] [240.Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
* [ ] [342.Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)
* [ ] [23.Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [ ] [315.Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
* [ ] [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
* [ ] [4.Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* [ ] [493.Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
* [ ] [https://leetcode.com/problems/number-of-ships-in-a-rectangle/](https://leetcode.com/problems/number-of-ships-in-a-rectangle/)
* [x] CSES: [Apple Division](https://cses.fi/problemset/result/2572485/) ⭐️
* [x] LC: [395. Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) ✅🚀🐽

## 3. Backtrack

* [x] [52.N-Queens II](https://leetcode.com/problems/n-queens-ii/) \| CSES: [Chessboard and Queens](https://cses.fi/problemset/task/1624) ✅🚀

{% tabs %}
{% tab title="52. nQ" %}
```python
board = [[0 for _ in range(n)]for _ in range(n)]
def canPlace(row,col):
    if board[row][col] != 0:
        return False
    for i in range(row+1):
        #check in the same col
        if board[i][col] == 1: return False
        #check if all diagonals are safe
        #(Only need to check the upper rows)- as neeche toh abhi kuch rkha hi nhi
        if 0<=row-i and 0<=col-i and (board[row-i][col-i] == 1):
            return False
        if 0<=row-i and col+i<n and (board[row-i][col+i] == 1):
            return False
    return True

def nQueen(row):
    if row == n:
        return 1
    res = 0
    for col in range(n):
        if canPlace(row, col):
            # print('placed in row: {} '.format(row))
            board[row][col] = 1
            res += nQueen(row+1)
            board[row][col] = 0
    return res

return nQueen(0)    # place from row 0 ---> row N-1

'''
TC: O(N!)
SC: O(N*N)
'''

```
{% endtab %}
{% endtabs %}

[https://leetcode.com/discuss/interview-question/1098081/famous-backtracking-problems](https://leetcode.com/discuss/interview-question/1098081/famous-backtracking-problems)







## \# Resources

* Aditya Verma's playlist on Recursion: [https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&ab\_channel=AdityaVerma](https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&ab_channel=AdityaVerma)

