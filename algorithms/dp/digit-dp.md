# Digit DP

## 1. Standard problems:

* [ ] find all X in range \[L,R] which follow some f(x)    . L,R could be very huge here \~ `10^18`
* [x] Q1: [Count numbers in range \[L,R\] s.t. sum of its digits == X.](https://www.youtube.com/watch?v=heUFId6Qd1A\&list=PLb3g_Z8nEv1hB69JL9K7KfEyK8iQNj9nX\&ab_channel=KartikArora)   (1<=L<=R\<pow(10,18) , 1<=X<=180)
* [ ] CSES: [Counting Numbers](https://cses.fi/problemset/task/2220/) | [Kartik Arora](https://www.youtube.com/watch?v=lD_irvBkeOk\&ab_channel=KartikArora) 🐽✅

{% tabs %}
{% tab title="#1." %}
```python
'''
dp(N,X) = dp(N-1,X)   # put '0' at 1st postition
          + dp(N-1,X-1) # put '0' at 1st postition, sum needed now is X-1
          + .... dp(N-1,X-9)
        = SUM ( dp(N-1,X-i) ) for i:[0,9]
COMPLEXITY = O(X*logR) ..... very very loww for such big R           
'''
MEMO = {}
def solve(str,n,x,tight):
          if (n,x,tight) in MEMO: return MEMO[(n,x,tight)]
          if x<0:return 0
          if n == 1:
               if 0<=x<=9: return 1
               return 0
           res = 0
           ub = str[(len(str)-n)] if tight else 9
           for dig in range(ub+1):
                     res += solve(strs,n-1,x-dig, (tight and dig == ub))
           MEMO[(n,x,tight)] = res
           return res
          
l, r = '', '1234'
return solve(r,len(r),5,1) - solve(l,len(l),5,1)
```
{% endtab %}
{% endtabs %}

* [ ] [902.Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) 🔒
* [ ] [1012. Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/discuss/560346/python-digit-dp)
* [ ] [788. Rotated Digits](https://leetcode.com/problems/rotated-digits/discuss/560601/python-digit-dp)
* [ ] [1397. Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/discuss/560841/Python-Digit-DP)
* [ ] [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/discuss/560876/Python-Digit-DP)
* [ ] [357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/560898/Python-Digit-DP)
* [ ] [600. Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/584350/Python-Digit-DP-\(Pattern-For-Similar-Questions\))

## 2. CF Problems:

* [ ] [Investigation](https://vjudge.net/problem/LightOJ-1068)
* [ ] [LIDS](https://toph.co/p/lids)
* [ ] [Magic Numbers](https://codeforces.com/contest/628/problem/D)
* [ ] [Palindromic Numbers](https://vjudge.net/problem/LightOJ-1205)
* [ ] [Chef and Digits](https://www.codechef.com/problems/DGTCNT)
* [ ] [Maximum Product](https://codeforces.com/gym/100886/problem/G)
* [ ] [Cantor](http://www.spoj.com/problems/TAP2012C/en/)
* [ ] [Digit Count](https://vjudge.net/problem/LightOJ-1122)
* [ ] [Logan and DIGIT IMMUNE numbers](https://www.codechef.com/problems/DIGIMU)
* [ ] [Sanvi and Magical Numbers](https://devskill.com/CodingProblems/ViewProblem/392)
* [ ] [Sum of Digits](http://www.spoj.com/problems/CPCRC1C/)
* [ ] [Digit Sum](http://www.spoj.com/problems/PR003004/)
* [ ] [Ra-One Numbers](http://www.spoj.com/problems/RAONE/)
* [ ] [LUCIFER Number](http://www.spoj.com/problems/LUCIFER/)
* [ ] [369 Numbers](http://www.spoj.com/problems/NUMTSN/)
* [ ] [Chef and special numbers](https://www.codechef.com/problems/WORKCHEF)
* [ ] [Perfect Number](https://codeforces.com/contest/919/problem/B)
* [ ] [The Great Ninja War](https://www.hackerearth.com/problem/algorithm/sallu-bhai-and-ias-8838ac8d/)
* [ ] AtCoder:[ Digit Product](https://atcoder.jp/contests/abc208/editorial/2216)

## 3. Resources: Digit DP

* CF: [Blog](https://codeforces.com/blog/entry/84928)
* ✅Kartik Arora's playlist: [Digit DP](https://www.youtube.com/watch?v=heUFId6Qd1A\&list=PLb3g_Z8nEv1hB69JL9K7KfEyK8iQNj9nX\&ab_channel=KartikArora)
