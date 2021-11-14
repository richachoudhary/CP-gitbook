# Prefix Sum

## 0. Notes

* 1D array:
  * `prefix[i]=prefix[i−1]+arr[i]`
  * `arr[i]=prefix[i]−prefix[i−1]`
* 2D matrix:
  * `prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] − prefix[i-1][j-1] + arr[i][j]`
  * `arr[i][j] = prefix[i][j] − prefix[i-1][j] − prefix[i][j-1] + prefix[i-1][j-1]`

## 1. Questions

* [x] CSES: [Subarray Sums II](https://cses.fi/problemset/task/1661) (negative numbers also allowed)
  * [x] CSES: [Subarray Sums I](https://cses.fi/problemset/task/1660) 🌟✅ | (only +ve numbers allowed)
* [x] CSES: [Subarray Divisibility](https://cses.fi/problemset/task/1662) ✅
* [x] CF: [1398C. Good Subarrays](https://codeforces.com/contest/1398/problem/C)
* [x] CSES: [Forest Queries](https://cses.fi/problemset/task/1652) | 2D matrix | direct implementation 🌟
* [x] LC [1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
  * [x] LC [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

{% tabs %}
{% tab title="SubarrSum2" %}
```python
for _ in range(1):
    n,x = I()
    A = list(I())
    prefix = [0]*n
    ans = 0
    
    D = dict()
    D[0] = 1
    for i in range(n):
        if i == 0:
            prefix[i] = A[i]
        else:
            prefix[i] = prefix[i-1] + A[i]
            
        ans += D.get(prefix[i]-x, 0)
        
        if prefix[i] in D:
            D[prefix[i]] += 1
        else:
            D[prefix[i]] = 1
            
    print(ans)
        
'''
 
5 7
    2 -1 3 5 -2
    2  1 4 9 7  
 
'''
```
{% endtab %}

{% tab title="SubarrSumsI" %}
```python
# =================================== 1: Hashmap
n,x = I()
A = list(I())

s = set()
s.add(0)
cnt = 0
curr = 0

for e in A:
    curr += e
    if curr - x in s:
        cnt += 1
    s.add(curr)
print(cnt)
# =================================== 2: Two Pointer
n,x = I()
A = list(I())

ans = 0
l = 0
curr = 0
for i in range(n):
    curr += A[i]
    while curr > x:
        curr -= A[l]
        l += 1
    if curr == x:
        ans += 1
print(ans)
```
{% endtab %}

{% tab title="SubarrDivisibility" %}
```python
A = list(I())
 
d = dict()
d[0] = 1
cnt = 0
curr = 0

for e in A:
    curr = (curr+e+n)%n # '+n' because of negative numbers
    if curr in d:
        cnt += d[curr]

    if curr in d:
        d[curr] += 1
    else:
        d[curr] = 1
print(cnt)
```
{% endtab %}

{% tab title="1398C" %}
```python
I = lambda : map(int, input().split())
n,q = I()
graph = [[0]*(n+1)]

for _ in range(n):
 s = str(input())
 graph.append([0] + [c for c in s])

DP = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
 for j in range(1,n+1):
     DP[i][j] = 1 if graph[i][j] == '*' else 0
     DP[i][j] = DP[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

 for _ in range(q):
     x1,y1,x2,y2 = I()
     print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])
```
{% endtab %}

{% tab title="1074" %}
```python
def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

    # PREFIX SUM
    '''
    For each row, calculate the prefix sum. 
    For each pair of columns, calculate the sum of rows.

    Time O(mnn)
    Space O(m)
    '''
    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(n - 1):
            matrix[x][y+1] += matrix[x][y]

    res = 0
    for y1 in range(n):
        for y2 in range(y1, n):
            preSums = {0: 1}
            s = 0
            for x in range(m):
                s += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
                res += preSums.get(s - target, 0)
                preSums[s] = preSums.get(s, 0) + 1
    return res
```
{% endtab %}
{% endtabs %}

* [x] LC [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

{% tabs %}
{% tab title="1292" %}
```python
def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
    # GET DIMENSIONS
    nrows, ncols = len(mat), len(mat[0])

    # SETUP THE PREFIX SUM MATRIX
    prefix = [[0 for _ in range(ncols + 1)] for _ in range(nrows + 1)]

    # FILL THE CELLS - TOP RECT + LEFT RECT - TOP LEFT DOUBLE-COUNTED RECT
    for i in range(nrows):
        for j in range(ncols):
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]


    '''
    1. INITIALIZE MAX_SIDE = 0
    2. AT EACH CELL, WE'LL CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J], BOTH INCLUSIVE, IS <= THRESHOLD
    '''

    # INITIALIZE MAX SIDE
    max_side = 0

    # CHECK IF RECTANGLE (OR SQUARE) FROM [I - MAX, J - MAX] TO [I, J] <= THRESHOLD
    for i in range(nrows):
        for j in range(ncols): 

            # CHECK IF WE CAN SUBTRACT MAX_SIDE
            if min(i, j) >= max_side:
                curr = prefix[i + 1][j + 1]
                top = prefix[i - max_side][j + 1]
                left = prefix[i + 1][j - max_side]
                topLeft = prefix[i - max_side][j - max_side]
                total = curr - top - left + topLeft

                # print(f"CURR : {curr} | TOP : {top} | LEFT : {left} | TOP_LEFT : {topLeft}")
                # print(f"TOTAL : {total}\n")

                # UPDATE MAX_SIDE IFF TOTAL <= THRESHOLD
                if total <= threshold:
                    max_side += 1

    # RETURN MAX SIDE
    return max_side
```
{% endtab %}
{% endtabs %}

