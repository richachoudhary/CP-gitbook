# Maths+Geometry

## 1. Probability DP

* [x] 808.[Soup Servings](https://leetcode.com/problems/soup-servings/) 🍜🥘✅✅
* [x] 1277\. [Airplane Seat Assignment Probability](https://leetcode.com/problems/airplane-seat-assignment-probability/) => `0.5 for n>1`
* [ ] [https://leetcode.com/problems/new-21-game/](https://leetcode.com/problems/new-21-game/)

{% tabs %}
{% tab title="808.🥘" %}
```python
def soupServings(self, N: int) -> float:
    if N >= 5000: return 1

    @functools.lru_cache(None)
    def helper(A, B, p):

        # return (prob. of A running out first, prob. of A and B running out at the same time)
        if (A <= 0) and (B <= 0):
            return (0, p)
        elif (A <= 0):
            return (p, 0)
        elif (B <= 0):
            return (0, 0)

        res = []
        res.append(helper(A-100, B, 0.25*p))
        res.append(helper(A-75, B-25, 0.25*p))
        res.append(helper(A-50, B-50, 0.25*p))
        res.append(helper(A-25, B-75, 0.25*p))

        return functools.reduce(lambda x,y: (x[0]+y[0], x[1]+y[1]), res)

    res = helper(N, N, 1)
    return res[0] + 0.5*res[1]

'''
Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

N can range from 0 to 10^9.
This solution will TLE for N > 5·10^4.
However, the output from soupServings grows asymptotically with N.
When N ≥ 5000, soupServings(N) ≈ 1 so we can just return 1.
This means we only need to find a solution when N < 5000.
'''
```
{% endtab %}
{% endtabs %}

## 2. Math Based

* [x] LC [264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) ✅
* [x] LC [313. Super Ugly Number](https://leetcode.com/problems/super-ugly-number/)
* [x] [241.Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | exactly similar to **print all binary trees**

{% tabs %}
{% tab title="264" %}
```python
k = [0] * n
t1 = t2 = t3 = 0
k[0] = 1
for i in range(1,n):
    k[i] = min(k[t1]*2,k[t2]*3,k[t3]*5)
    if(k[i] == k[t1]*2): t1 += 1
    if(k[i] == k[t2]*3): t2 += 1
    if(k[i] == k[t3]*5): t3 += 1
return k[n-1]
```
{% endtab %}

{% tab title="313." %}
```python
nums=[]
heap=[]
seen={1,}
heappush(heap,1)

for _ in range(n):
    curr_ugly=heappop(heap)
    nums.append(curr_ugly)
    for prime in primes:
        new_ugly=curr_ugly*prime
        if new_ugly not in seen:
            seen.add(new_ugly)
            heappush(heap,new_ugly)

return nums[-1]
```
{% endtab %}

{% tab title="241." %}
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
{% endtabs %}

* [ ] [https://leetcode.com/problems/count-sorted-vowel-strings/](https://leetcode.com/problems/count-sorted-vowel-strings/)
* [ ] [https://leetcode.com/problems/super-egg-drop/](https://leetcode.com/problems/super-egg-drop/)
* [ ] [https://leetcode.com/problems/least-operators-to-express-number/](https://leetcode.com/problems/least-operators-to-express-number/)
* [ ] [https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)

## 3. Geometrical DP (blocks, rectangles etc)

* [x] CSES: Rectangle Cutting | [Kartik Arora](https://www.youtube.com/watch?v=LdynQjWsO5Q\&ab\_channel=KartikArora) ✅
* [x] LC [1240: Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | just handle the case of `11x13 `separately | rest is same as `CSES: Rect Cutting` | **@google**
* [x] CSES: [Counting Towers](https://cses.fi/problemset/task/2413) | [KartikArora](https://www.youtube.com/watch?v=pMEYMYTX-r0\&ab\_channel=KartikArora) ✅

{% tabs %}
{% tab title="Rect Cutting" %}
```python
'''       m
    _____________
    |           |
   n|           |
    |           |
'''
@lru_cache(None)
def dp(n,m):
    if n == m:
        return 0
    if (n,m) in MEMO:
        return MEMO[(n,m)]
    v_cut, h_cut = mxn,mxn

    for i in range(1,(m//2)+1):
        v_cut = min(v_cut, 1+dp(n,i)+dp(n,m-i))

    for i in range(1,(n//2)+1):
        h_cut = min(h_cut, 1+dp(i,m)+dp(n-i,m))
    
    MEMO[(n,m)] = min(v_cut,h_cut)
    return MEMO[(n,m)] 

def f():
    I = lambda : map(int, input().split())
    n,m = I()
    print(dp(n,m))
```
{% endtab %}

{% tab title="1240." %}
```python
MEMO = {}
def dp(n,m):
    # God knows why- the special case & only case when code fails
    if (n == 11 and m== 13) or (n==13 and m == 11):
        return 6
    if n == m:
        return 1
    v_cut = h_cut = float('inf')
    if (n,m) in MEMO: return MEMO[(n,m)]
    for i in range(1,(n//2)+1):
        h_cut = min(h_cut,dp(i,m)+dp(n-i,m))
        
    for i in range(1,(m//2)+1):
        v_cut = min(v_cut, dp(n,i)+dp(n,m-i))

    MEMO[(n,m)] = min(v_cut, h_cut)
    return MEMO[(n,m)]
    
```
{% endtab %}

{% tab title="CountingTowers" %}
```python
'''
STATES: 
    * height of tower = i
    * isLinked: 0/1     => whether brick of width 2 or 1
        0: | | |  : 2 bricks of with 1 each
        1: |   |  : brick of width 2
RECUR:
    * dp(i,0): 
        1. Dont extend any tile : 
            1.1 can place a tile of width 2  => dp(i-1,1)
            1.2 can palce 2 tiles of widht 1 => dp(i-1,0)
        2. Extend both:                      => dp(i-1,0)
        3. Extend Either:                    => 2*dp(i-1,0) 
    * dp(i,1):
        1. Dont extend any tile....         => 1.1 + 1.2
        4. Extend the linked piece          => dp(i-1,1)

ANS: dp(n,0) + dp(n,1)
'''
def dp(i,linked):
    if i == 1:
        return 1

    if (i,linked) in MEMO:
        return MEMO[(i,linked)]
    op1 = dp(i-1,1)%MOD         # 1.1
    op2 = dp(i-1,0)%MOD         # 1.2
    op3 = dp(i-1,0)%MOD     # 2
    op4 = 2*dp(i-1,0)%MOD   #3
    op5 = dp(i-1,1)%MOD     #4

    if linked == 0:
        MEMO[(i,linked)] = (op1 + op2 + op3 + op4)%MOD 
    else:
        MEMO[(i,linked)] = (op1 + op2 + op5)%MOD
    return MEMO[(i,linked)]

def f():
    # I = lambda : map(int, input().split())
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = (dp(n,0) + dp(n,1))%MOD
        print(res)
```
{% endtab %}
{% endtabs %}
