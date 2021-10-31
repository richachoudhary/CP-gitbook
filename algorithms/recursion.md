# Recursion 💪

## Notes

* **Approaches** to solve a recursive problem:
  1. If you have to take \*\*decisions \*\*at every step => Make **Decision Tree** (using **I/P O/P method**)
     * You'll get the answer when \*\*i/p is empty i.e. \*\*at the **leaves** of decision tree
     * \*\*Trick: \*\*is to keep reducing input & keep increasing output::
     * **`f(ip,op) => f(smaller_ip, larger_op1) , f(smaller_ip, larger_op2) ,...`**
     * See below: \*\* \*\*`Print all subsets/powerset of a string`
  2. If the problem requires **reducing the input** at every step => use **BHI method**
     * I. **Hypotheses**: what will your function do (_induction_)
     * II. **Induction**: Apply that hypothesis on smaller input :: `main code` goes here
     * III. Write **base condition** i.e. _smallest valid input_ & include it in the beginning
     * e.g.: find height of tree [video](https://www.youtube.com/watch?v=aqLTbtWh40E\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=5\&ab\_channel=AdityaVerma%27)
  3. If you've to take choices at every step: => Make **Choice Diagram** (like **DP**)

## 1. Recursion

* [x] Sort An Array \*\*OR \*\*Sort A Stack (using BHI method) - for concept building : [video](https://www.youtube.com/watch?v=AZ4jEY\_JAVc\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=6\&ab\_channel=AdityaVerma)

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
* [x] GfG: [Reverse A Stack w/o Extra Space](https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/) | [Video](https://www.youtube.com/watch?v=8YXQ68oHjAs\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=9\&ab\_channel=AdityaVerma) `O(1) ; not counting function stack`

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
* [x] CSES: [Tower of Hanoi](https://cses.fi/problemset/task/2165) | [video](https://www.youtube.com/watch?v=l45md3RYX7c\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=11\&ab\_channel=AdityaVerma)
* [x] [22.Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) 🚀

{% tabs %}
{% tab title="779" %}
Pascal Tree \*\*type \*\*structure banega

```python
def kthGrammar(self, n: int, k: int) -> int:

    def recur(n,k):
        if n==0:
            return 0
        else:
            prev = recur(n-1,k//2)
            # print(" n = {} , k = {} , prev = {}".format(n,k,prev))
            if prev == 0:
                return 1 if (k&1) else 0
            else:
                return 0 if (k&1) else 1

    res = recur(n-1,k-1)

    return res


    # Just make the fucking (pascal like) tree!!!!!!
    # f(n,k) = f(n-1, k//2) == 0 ::
    #                             if k&1 : 1
    #                             else   : 0
    #                       == 1 ::
     #                             if k&1 : 0
    #                              else   : 1
    #

    # Aditya Verma : https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10&ab_channel=AdityaVerma
```
{% endtab %}

{% tab title="Tower Of Hanoi" %}
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
{% endtab %}

{% tab title="22" %}
```python
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def f(op,cl,s):
        # print(f'op = {op}, cl = {cl} , s = {s}')
        if cl == 0:
            ans.append(s)
            return

        if op > 0: f(op-1,cl,s+'(')
        if cl > 0 and op < cl:f(op,cl-1,s+')')

    f(n,n,'')
    return ans
```
{% endtab %}
{% endtabs %}

* [x] Print all subsets/powerset of a string | [video](https://www.youtube.com/watch?v=Yg5a2FxU4Fo\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=12\&ab\_channel=AdityaVerma) | **Decision Tree method**

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

* [x] [Permutation with Spaces](https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1) | [Video](https://www.youtube.com/watch?v=1cspuQ6qHW0\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&index=14\&ab\_channel=AdityaVerma) : \*\*NOTE: \*\*Sometimes you've to break-down the problem before making recursion tree
* [x] \----------------------------- \[Medium]---------------------------
* [x] [1823.Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)
* [x] [1545.Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)
* [ ] [394.Decode String](https://leetcode.com/problems/decode-string/) 🔒❌
* [ ] \-------------------------------\[Hard]----------------------------------
* [ ] CSES: [Josephus Problem II](https://cses.fi/problemset/task/2163) 🐽 | KartikVarma-O(N\*N)...need to do better
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

## 2. D\&C

* [x] [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) ✅| **standard\_Q**
* [x] [241.Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) ✅ | similar to #95
* [x] [240.Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | **@Google ✅**
* [x] [280. Wiggle Sort I](https://leetfree.com/problems/wiggle-sort) | **@Google ✅**
* [ ] [342.Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)
* [ ] [23.Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [ ] [315.Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
* [ ] [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
* [ ] [4.Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* [ ] [493.Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
* [ ] [https://leetcode.com/problems/number-of-ships-in-a-rectangle/](https://leetcode.com/problems/number-of-ships-in-a-rectangle/)
* [x] CSES: [Apple Division](https://cses.fi/problemset/result/2572485/) ⭐️
* [x] LC: [395. Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) ✅🚀🐽

{% tabs %}
{% tab title="95" %}
```python
def generateTrees(self, n: int) -> List[TreeNode]:

    def solve(arr):
        #Base conditions
        if len(arr) < 1:
            return [None]
        if len(arr) == 1:
            return [TreeNode(arr[0])]

        ret = []
        for i,item in enumerate(arr):
            leftTrees = f(arr[0:i])
            rightTrees = f(arr[i+1:])

            for lt in leftTrees:
                for rt in rightTrees:
                    r = TreeNode(arr[i])
                    r.left = lt
                    r.right = rt
                    ret.append(r)
        return ret

    return solve(list(range(1,n+1)))
```
{% endtab %}

{% tab title="241" %}
```python
def diffWaysToCompute(self, s: str) -> List[int]:
    MEMO = {}

    def f(s):
        if s in MEMO:
            return MEMO[s]
        if s.isdigit():
            MEMO[s] = [int(s)]
            return MEMO[s]
        res = []
        for i,c in enumerate(s):
            if c in '+-*':
                l = f(s[:i])
                r = f(s[i+1:])
                for _l in l:
                    for _r in r:
                        if c == '+':
                            res.append(_l + _r)
                        elif c == '-':
                            res.append(_l - _r)
                        else:
                            res.append(_l * _r)
        MEMO[s] = res
        return res
    return f(s)
    '''
    Complexity: w/o MEMO: O(2^n)
    '''
```
{% endtab %}

{% tab title="240" %}
```python
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1. TC: O(NlogM) -----------------------------------------------------
        
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if 0<= idx < len(row) and row[idx] == target:
                return True
        return False
        
        
        
        #2. TC: O(N+M) -----------------------------------------------------
        n,m = len(matrix), len(matrix[0])
        x, y = 0, m-1   # start from top-right(TR)
        
        while True:
            if matrix[x][y] == target:
                return True
            
            # move down
            if matrix[x][y] < target:
                x += 1
                
            # move left
            elif matrix[x][y] > target:
                y -= 1
            
            if x >= n or y < 0:     # out of bound
                break
            
        return False
```

**Approach#2: O(N+M) | most optimised:**

* start from TOP-RIGHT(**TR**) corner
* in each step; either move down or left ; until found OR out-of-bound
* video on approach#2: [link](https://www.youtube.com/watch?v=dcTJRw1704w\&ab\_channel=AlgorithmsMadeEasy) | understand why you can solve this only by starting from **TOP-RIGHT**(\*\*TR) \*\*corner
{% endtab %}

{% tab title="395" %}
```python
from collections import Counter
def longestSubstring(self, s: str, k: int) -> int:
    
    cnt = Counter(s)
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

{% tab title="AppleDivi" %}
```python
x,y = 0,0
# MEMO = {}
def f(x,y,i):
    # print('i: {} , x:{} ,y:{} '.format(i,x,y))
    if i >= len(a) :
        return abs(x-y)
    opt1 = f(x+a[i],y,i+1)
    opt2 = f(x,y+a[i],i+1)
    return min(opt1,opt2)
    
ans = f(0,0,0)
print(ans)
```
{% endtab %}

{% tab title="WiggleSort280+342" %}
[**LC 280. Wiggle Sort I**](https://leetfree.com/problems/wiggle-sort)

```
nums[i-1] <= nums[i] >= nums[i + 1] where i is an odd number
```

* App#1(naive): sort🙅‍♂️ TC:O(nlogn) , SC: O(N)
* App#2: in-place swap: TC:O(N), SC: O(1)

```python
def wiggleSort(self, nums: List[int]) -> None:

    #1. NAIVE: Sorting: TC : O(NlogN), SC: O(N) ================================
    nums.sort()
    n = len(nums)

    first_half, second_half = nums[:n//2] , nums[n//2:]
    second_half.reverse()

    print(first_half)
    print(second_half)

    i,j = 0,0
    res = []
    while i<len(first_half) and j <len(second_half):
        res.append(first_half[i])
        res.append(second_half[j])
        i += 1
        j += 1

    while i<len(first_half):
        res.append(first_half[i])
        i += 1

    while j<len(second_half):
        res.append(second_half[j])
        j += 1
    nums[::] = res

    """
    Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 

    Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
    Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
    --------------------------      --------------------------
    Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
    """

    # 2. In Place Sort:: TC: O(N), SC: O(1) ========================================

    n = len(nums)
    i = 0

    while i < n:
        if i> 0 and nums[i] <= nums[i-1]:
            nums[i],nums[i-1] = nums[i-1], nums[i]
        if i<n-1 and nums[i] <= nums[i+1]:
            nums[i],nums[i+1] = nums[i+1], nums[i]

        i += 2


    '''
    IDEA: move to odd indices & try to create local maxima(by swapping)
    video: https://www.youtube.com/watch?v=di7gNqxfU1g&ab_channel=CodingBlocks

    '''
```

**LC 324. **[**Wiggle Sort II**](https://leetcode.com/problems/wiggle-sort-ii/)

**How is it different from Wiggle Sort I?**

* Wiggle sort 1 is `nums[i-1] <= nums[i] >= nums[i + 1]` where i is an odd number
* This question is `nums[i-1] < nums[i] > nums[i + 1]` where i is an odd number.
* The **difference** is that, in this question, when two elements are equal, you have to move one of the two elements somewhere else, and the difficulty is how to achieve moving all the duplicate elements to their correct positions in O(N) time such that the final array has a wiggle pattern.

```python








??????????????????????????????????? 
TODO:




```
{% endtab %}
{% endtabs %}

## 3. Backtrack

* [x] [52.N-Queens II](https://leetcode.com/problems/n-queens-ii/) | CSES: [Chessboard and Queens](https://cses.fi/problemset/task/1624) ✅🚀

{% tabs %}
{% tab title="52. n Queens" %}
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

## # Resources

* Aditya Verma's playlist on Recursion: [https://www.youtube.com/watch?v=kHi1DUhp9kM\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&ab\_channel=AdityaVerma](https://www.youtube.com/watch?v=kHi1DUhp9kM\&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY\&ab\_channel=AdityaVerma)
