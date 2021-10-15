# Prefix Sum

## 0. Notes

* 1D array:
  * `prefix[k]=prefix[k−1]+arr[k]`
  * `arr[i]=prefix[R]−prefix[L−1]` 
* 2D matrix:
  * `prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] − prefix[i-1][j-1] + arr[i][j]`
  * `arr[i][j] = prefix[A][B] − prefix[a-1][B] − prefix[A][b-1] + prefix[a-1][b-1]`

## 1.  Questions

* [x] CSES: [Subarray Sums II](https://cses.fi/problemset/task/1661)
* [x] CSES: [Subarray Divisibility](https://cses.fi/problemset/task/1662) ✅
* [ ] CF: [1398C. Good Subarrays](https://codeforces.com/contest/1398/problem/C) 
* [x] CSES: [Forest Queries](https://cses.fi/problemset/task/1652) | 2D matrix | direct implementation 🌟
*

{% tabs %}
{% tab title="SubarraySums2" %}
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

{% tab title="SubarrDivisibility✅" %}
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
{% endtabs %}



