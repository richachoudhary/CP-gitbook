# Greeeedy

## 1. Map



## 2. Hashing

### 2.1 Rolling Hash

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained)
* [ ] [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath) 



## 3. Heap

## 4. Queue/Stack/Monotonic

### 4.0 Notes:

* How to identify **stack** problem: there'll be an dependent second nested loop. EG:

```python
for i in range(0,N):
    # case1:
    for j in range(0,i): ...
    # case2:
    for j in range(i,0,-1): ...
    # case3:
    for j in range(i+1,N)): ..
    # etc etc
```

## 4.1 Standard Questions

#### NGL variants:

* [x] GfG: [Next Greatest Element](https://www.geeksforgeeks.org/next-greater-element/) \| **NGL**
* [x] [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O%281%29) \| similar to NGL \|  \| system design heavy🔒
* [x] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) \| simple implementation of `NSL+NSR` ❤️
  * **NOTE**: dont cram that single stack traversal method. This one is easy to derive on your own
* [x] [85.Maximal Rectangle Area In Binary Matrix](https://leetcode.com/problems/maximal-rectangle/) **`NSL+NSR`** add heights for every row&apply \#84's code😎

{% tabs %}
{% tab title="NGL" %}
```python
def ngl(arr):
    stk = []
    n = len(arr)
    res = []*n
    for i in range(n-1,-1,-1):
        while len(stk) and stk[-1] < arr[i]:
            stk.pop()
        if len(stk) == 0:
            res[i] = -1
        else:
            res[i] = stk[-1]
        stk.append(arr[i])
    return res
```
{% endtab %}

{% tab title="901" %}
```python
def lel(self, arr: int) -> int:
    arr = self.price
    n = len(arr)
    res = [1]*n
    stk = []    # stores indices
    
    for i in range(n):
        while len(stk) and arr[i] > arr[stk[-1]]:
            stk.pop()
        if len(stk) == 0:
            res[i] = 1
        else:
            res [i] = i-stk[-1]
        stk.append(i)
    return res 
```
{% endtab %}

{% tab title="84❤️" %}
```python
def largestRectangleArea(self, h: List[int]) -> int:
    n = len(h)
    # 1. get nsl - indices
    '''
  i:[0,1,2,3,4,5]
  h:[2,1,5,6,2,3]
nsl:[-1,-1,1,2,1,4]
    '''
    nsl = [0]*n
    stk = []
    
    for i in range(n):
        while stk and h[stk[-1]] >= h[i]:
            stk.pop()
        if len(stk) == 0:
            nsl[i] = -1
        else:
            nsl[i] = stk[-1]
        stk.append(i)
    print(nsl)
    
    # 2. get nsr - indices
    '''
  i:[0,1,2,3,4,5]
  h:[2,1,5,6,2,3]
nsr:[1,6,4,4,6,6]
    '''
    
    nsr = [0]*n
    stk = []
    for i in range(n-1,-1,-1):
        while stk and h[stk[-1]] >= h[i]:
            stk.pop()
        if len(stk) == 0:
            nsr[i] = n
        else:
            nsr[i] = stk[-1]
        stk.append(i)
    print(nsr)
    
    # 3. compute areas
    # (nsr[i] - nsl[i] - 1)*h[i]
    res = 0
    for i in range(n):
        area = abs(nsr[i] - nsl[i] - 1)*h[i]
        res = max(res,area)
    return res
```
{% endtab %}

{% tab title="85" %}
```python
def maximalRectangle(self, matrix: List[List[str]]):
    n= len(matrix)
    if n == 0:return 0
    m = len(matrix[0])
    
    grid = [[0 for i in range(m)]for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                grid[i][j] = int(matrix[i][j])
            elif i>0 and matrix[i][j]=="1":
                grid[i][j] = grid[i-1][j] + 1
    
    res = 0
    for row in grid:
         res = max(res,largestRectangleArea(row))      
    return res
```
{% endtab %}
{% endtabs %}

* [x] [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

```python
def trap(h: List[int]) -> int:
    n = len(h)
    if n == 0: return 0
    mxl = [h[0]]*n
    mxr = [h[-1]]*n
    
    max_yet = mxl[0]
    for i in range(1,n):
        max_yet = max(h[i],max_yet)
        mxl[i] = max_yet
    
    max_yet = mxr[-1]
    for i in range(n-1,-1,-1):
        max_yet = max(h[i],max_yet)
        mxr[i] = max_yet

    res = 0
    for i in range(n):
        res += min(mxl[i],mxr[i]) - h[i]
    return res
```



* [ ] [1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O%28N%29-Time-and-Space)
* [ ] [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution)
* [ ] [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-O%281%29-Space)
* [ ] **LC239. Sliding Window Maximum**
* [ ] **LC739. Daily Temperatures**
* [ ] **LC862. Shortest Subarray with Sum at Least K**
* [ ] **LC907. Sum of Subarray Minimums**

### 4.2 Rest of the problems

* [x] [391. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
* [x] [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) \|  for circular array 🚀
* [ ] [556.Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) 🍪🍪🍪
* [x] [155. Min Stack](https://leetcode.com/problems/min-stack/) : instead of 2 stacks, use single stack & insert pairs in it: `ele,min_ele`
  * Regular approach of `O(1)` =&gt; [Aditya Verma](https://www.youtube.com/watch?v=ZvaRHYYI0-4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=11&ab_channel=AdityaVerma)

### 4.3 Resources

* [Aditya Verma's Playlist](https://www.youtube.com/watch?v=P1bAPZg5uaE&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&ab_channel=AdityaVerma)



## 5.Sort



## 6.Binary Search

* [ ] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [this approach](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o%28n-log-n%29-explained) =&gt; **Rolling Hash/Rabin Karp**

## Two Pointers



## 7.Sliding Window





## 8.Intervals Question

