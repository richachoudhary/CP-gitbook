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
     * III. Write **base condition** i.e. smallest valid input & include it in the beginning 
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
* [x] GfG: [Reverse A Stack w/o Extra Space](https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/) [Video](https://www.youtube.com/watch?v=8YXQ68oHjAs&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=9&ab_channel=AdityaVerma) `O(1) ; not counting function stack`

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
* [x] Tower of Hanoi \| [video](https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11&ab_channel=AdityaVerma)

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

* [x] Print all subsets/powerset of a string \| [video](https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12&ab_channel=AdityaVerma) \| Decision Tree method

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
* [x] [22.Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) 🚀



## 2. D&C

## 3. Backtrack









## \# Resources

* Aditya Verma's playlist on Recursion: [https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL\_z\_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&ab\_channel=AdityaVerma](https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&ab_channel=AdityaVerma)

