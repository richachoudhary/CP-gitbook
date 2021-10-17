# Stack | Queue

### Notes:

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

### 4.1 Standard Questions

#### NGL variants:

* [x] GfG: [Next Greatest Element](https://www.geeksforgeeks.org/next-greater-element/) | **NGL**
* [x] [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O\(1\)) | similar to NGL | | system design heavy🔒
* [x] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | simple implementation of `NSL+NSR` ❤️
  * **NOTE**: dont cram that single stack traversal method. This one is easy to derive on your own
  * `area = abs(nsr[i] - nsl[i] - 1)*h[i]`
* [x] [85.Maximal Rectangle Area In Binary Matrix](https://leetcode.com/problems/maximal-rectangle/) \*\*`NSL+NSR` \*\*add heights for every row\&apply #84's code😎

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

* [x] [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) `res += min(mxl[i],mxr[i]) - h[i]`
* [x] [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
* [x] [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) ✅
* [x] [**772. Basic Calculator III**](https://ttzztt.gitbooks.io/lc/content/quant-dev/basic-calculator-iii.html)** 🐽 | **[**approach**](https://leetcode.com/problems/basic-calculator-ii/discuss/658480/python-basic-calculator-i-ii-iii-easy-solution-detailed-explanation)

{% tabs %}
{% tab title="42" %}
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
{% endtab %}

{% tab title="227" %}
```python
def calculate(self, s: str) -> int:
        
    '''
    IDEA : just keep the numbers (positve/negative) in stack
    in the end; sum up all of them
    
    22+5-17*5
    
    '''
    num = 0
    pre_op = '+'
    stk = []
    
    
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif not c.isspace():
            if pre_op == '+':
                stk.append(num)
            elif pre_op == '-':
                stk.append(-num)
            elif pre_op == '*':
                x = stk.pop()
                stk.append(x*num)
            else:
                x = stk.pop()
                stk.append(int(x/num))
            num = 0
            pre_op = c
    
    # for the last operation -------------
    if pre_op == '+':
        stk.append(num)
    elif pre_op == '-':
        stk.append(-num)
    elif pre_op == '*':
        x = stk.pop()
        stk.append(x*num)
    else:
        x = stk.pop()
        stk.append(int(x/num))
            
    # now just add all numbers in stack
    # print(stk)
    return sum(stk)
                    
    # 2. ==================================================[The amazing hack]
    s += '+0'        # JUGAAD to handle the last operation------------------
    stack, num, preOp = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit(): num = num * 10 + int(s[i])
        elif not s[i].isspace():
            if   preOp == "-":  stack.append(-num)
            elif preOp == "+":  stack.append(num)
            elif preOp == "*":  stack.append(stack.pop() * num)
            else:               stack.append(int(stack.pop() / num))
            preOp, num = s[i], 0
    return sum(stack)                    
```
{% endtab %}

{% tab title="224" %}
```python
def calculate(self, s: str) -> int:
    num=0
    res=0
    sign=1
    stack=[]

    for char in s:
        if char.isdigit():
            num=num*10+int(char)
        elif char in ["-","+"]:
            res=res+num*sign
            num=0
            if char=="-":
                sign=-1
            else:
                sign=1
        elif char=="(":
            stack.append(res)
            stack.append(sign)
            sign=1
            res=0
        elif char==")":
            res+=sign*num
            res*=stack.pop()## process sign
            res+=stack.pop() ##process with old value
            num=0

    return res+num*sign
```
{% endtab %}

{% tab title="" %}
```python
def calc(it):
    def update(op, v):
        if op == "+": stack.append(v)
        if op == "-": stack.append(-v)
        if op == "*": stack.append(stack.pop() * v)
        if op == "/": stack.append(int(stack.pop() / v))

    num, stack, sign = 0, [], "+"
    
    while it < len(s):
        if s[it].isdigit():
            num = num * 10 + int(s[it])
        elif s[it] in "+-*/":
            update(sign, num)
            num, sign = 0, s[it]
        elif s[it] == "(":
            num, j = calc(it + 1)
            it = j - 1
        elif s[it] == ")":
            update(sign, num)
            return sum(stack), it + 1
        it += 1
    update(sign, num)
    return sum(stack)

return calc(0)
```
{% endtab %}
{% endtabs %}

* [ ] [1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O\(N\)-Time-and-Space)
* [ ] [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution)
* [ ] [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-O\(1\)-Space)
* [ ] LC239. Sliding Window Maximum
* [ ] LC739. Daily Temperatures
* [ ] LC862. Shortest Subarray with Sum at Least K
* [ ] LC907. Sum of Subarray Minimums
* [x] [1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

### 4.2 Rest of the problems

* [x] [391. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
* [x] [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | for circular array 🚀
* [ ] [556.Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) 🍪🍪🍪
* [x] [155. Min Stack](https://leetcode.com/problems/min-stack/) : instead of 2 stacks, use single stack & insert pairs in it: `ele,min_ele`
  * Regular approach of `O(1)` => [Aditya Verma](https://www.youtube.com/watch?v=ZvaRHYYI0-4\&list=PL_z\_8CaSLPWdeOezg68SKkeLN4-T_jNHd\&index=11\&ab_channel=AdityaVerma)
* [x] [1441.Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/)
* [x] SPOJ: [STPAR - Street Parade](https://www.spoj.com/problems/STPAR/) | [Approach](http://discuss.spoj.com/t/stpar-street-parade/2022)
* [x] LC 316. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

{% tabs %}
{% tab title="155" %}
#### Approach#1: Standard | single stack + var | O(1)

```python
def __init__(self):
    
    self.min_ = float('inf')
    self.stack = []

def push(self, val: int) -> None:
    self.stack.append(val)
    self.min_ = min(self.min_, val)

def pop(self) -> None:
    pop_ = self.stack[-1]
    self.stack.pop()
    if self.stack:
        if self.min_ == pop_:
            self.min_ = min(self.stack)
    else:
        self.min_ = float('inf')

def top(self) -> int:
    if self.stack:
        return self.stack[-1]
    

def getMin(self) -> int:
    if self.stack:
        return self.min_
```

####

#### Approach#2: Smart | stack of tuple | O(1)

```python
class MinStack:

    def __init__(self):
        self.stk = []    # (ele, min_ele)

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val,val))
            return
        
        if self.stk[-1][1] > val:    # val is the new min
            self.stk.append((val,val))   
        else:
            old_min = self.stk[-1][1]
            self.stk.append((val,old_min))
        

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
```
{% endtab %}

{% tab title="316" %}
```python
def removeDuplicateLetters(self, s: str) -> str:
    last_occ = {}
    for i,c in enumerate(s):
        last_occ[c] = i

    stk = []
    vis = set()

    for i,c in enumerate(s):
        if c in vis:continue

        while stk and stk[-1] > c and last_occ[stk[-1]] > i:
            vis.remove(stk[-1])
            stk.pop()
        stk.append(c)
        vis.add(c)
    return ''.join(stk)

```

soln link: [https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O(n)-greedy-with-stack-explained](https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O\(n\)-greedy-with-stack-explained)
{% endtab %}
{% endtabs %}

### 4.3 Resources

* [Aditya Verma's Playlist](https://www.youtube.com/watch?v=P1bAPZg5uaE\&list=PL_z\_8CaSLPWdeOezg68SKkeLN4-T_jNHd\&ab_channel=AdityaVerma)
