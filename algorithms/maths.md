# Maths & Geometry

## 1. Geometry

### 1.1 Notes

* Heron's formula for area of triangle![\text{ Area }=\sqrt{s\(s-a\)\(s-b\)\(s-c\)}](https://www.gstatic.com/education/formulas2/355397047/en/heron_s_formula.svg)

### 1.2 Problems: Geometry

#### 1.2.1 Easy 🧠

* [x] [1266.Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/) 
* [x] [883. Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/)
* [x] [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/) ✴️
* [x] [892. Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) ✴️

{% hint style="info" %}
For problems like \(\#892\) :in geometry of 3-D blocks: think in terms of subtracting the overlap, not adding each block one-by-one.
{% endhint %}

* [x] Check collinearity : [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
  * [x] Similar: [1037.Valid Boomerang](https://leetcode.com/problems/valid-boomerang/)

```python
(x0, y0), (x1, y1) = coordinates[: 2]
for x, y in coordinates:
    if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
        return False
return True
```

* [x] [836.Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) 💡
* [ ] 
### 2.3 Problemsets

* **`[E]`** Leetcode tag = **geometry:** [https://leetcode.com/problemset/all/?topicSlugs=geometry](https://leetcode.com/problemset/all/?topicSlugs=geometry)
* Codeforces Tag = **geometry** : [https://codeforces.com/problemset?tags=geometry](https://codeforces.com/problemset?tags=geometry)

### 1.3 Resources: Geometry

* [Geometric Algorithms](https://www.cs.princeton.edu/~rs/AlgsDS07/16Geometric.pdf)
* Topcoder:
  * [GEOMETRY CONCEPTS PART 1: BASIC CONCEPTS](https://www.topcoder.com/thrive/articles/Geometry%20Concepts%20part%201:%20Basic%20Concepts)
  * [GEOMETRY CONCEPTS PART 2: LINE INTERSECTION AND ITS APPLICATIONS](https://www.topcoder.com/thrive/articles/Geometry%20Concepts%20part%202:%20%20Line%20Intersection%20and%20its%20Applications)
  * [LINE SWEEP ALGORITHMS](https://www.topcoder.com/thrive/articles/Line%20Sweep%20Algorithms)
* [Al.Cash's blog](https://codeforces.com/blog/entry/48122)
* [Handbook of geometry for competitive programmers](https://vlecomte.github.io/cp-geo.pdf)



## 2. Maths

### 2.1 Notes

* Modular Exponentiation :

```cpp
int modularExponentiation(int x,int n,int M){    //get (x^n % M)
    if(n==0) return 1;
    else if(n%2 == 0) return modularExponentiation((x*x)%M,n/2,M);
    else return (x*modularExponentiation((x*x)%M,(n-1)/2,M))%M;
}
// or in python: 
math.pow(x,n,M)
```

 

### 2.2 Problems: Maths

* [x] CSES: [Two Sets](https://cses.fi/problemset/task/1092) \| four consecutive numbers can be divided into 2 sets of equal sums \| [link to solution approach](https://www.reddit.com/r/learnprogramming/comments/n9ql5a/cses_problem_two_sets/) ⭐️
* [x] CSES: [Coin Piles](https://cses.fi/problemset/task/1754) \| [Solution Approach](https://discuss.codechef.com/t/coin-piles-problem-from-cses/28647/3)
* [x] CSES: [Gray Code](https://cses.fi/problemset/task/2205) \| [Solution](https://www.geeksforgeeks.org/generate-n-bit-gray-codes/)
* [x] CSES: [Missing Coin Sum](https://cses.fi/problemset/result/2583670/) \| [Approach](https://discuss.codechef.com/t/cses-missing-coin-sum/84039/2) ✅
  * **KYA SEEKHA:** At any index **i** in a sorted array **a**, currSum represents `sum(a[ 0...i ])`.We can form every possible sum from `1...currSum`, when we are at index i

### 2.3 Combinatorics

* [ ] AtCoder: [Cumulative Sum](https://atcoder.jp/contests/abc208/tasks/abc208_f) \| [Editorial](https://atcoder.jp/contests/abc208/editorial/2219)

### 2.4 Chess Problems:

* [x] CSES: [Two Knights](https://cses.fi/problemset/task/1072) \| approach: [here](https://discuss.codechef.com/t/cses-two-knights-problem-help-needed/69448/5) & [here](https://math.stackexchange.com/questions/3266257/number-of-ways-two-knights-can-be-placed-such-that-they-dont-attack)
* [https://codeforces.com/blog/entry/78943](https://codeforces.com/blog/entry/78943)

{% hint style="info" %}
If two knight attack each other then they will be in 2\*_3 rectangle or 3\*_2 rectangle. 

* number of 2\*3 rects = \#rows\*\#cols = \(n-1\)\*\(n-2\)

So the number of ways of placing them is \(n-1\)_\(n-2\)+\(n-2\)_\(n-1\). Also in each rectangle no ways of placing the knight is 2. So total ways of placing knight so that they attack each other will be 2_2_\(n-1\)_\(n-2\). So the number of ways such that knight do not attack each other will be n_n_\(n_n-1\)/2 — 4_\(n-1\)_\(n-2\)
{% endhint %}



### 2.3 Problemsets

* Leetcode tag=**Maths :** [https://leetcode.com/problemset/all/?topicSlugs=math](https://leetcode.com/problemset/all/?topicSlugs=math)
* Hackerrank: [https://www.hackerrank.com/domains/mathematics?filters%5Bsubdomains%5D%5B%5D=geometry](https://www.hackerrank.com/domains/mathematics?filters%5Bsubdomains%5D%5B%5D=geometry)
* Codeforces Tag = **combinatorics/probability**: [https://codeforces.com/problemset?tags=probabilities](https://codeforces.com/problemset?tags=probabilities)
* Codeforces tag = **number-theory:**  [https://codeforces.com/problemset?tags=number+theory](https://codeforces.com/problemset?tags=number+theory)

### 2.4 Resources: Maths

* Kartik Arora's Playlist :[ Number Theory](https://www.youtube.com/watch?v=2NN5j1iF2ko&list=PLb3g_Z8nEv1i6NHntG5l2fPKuVu853EYy&ab_channel=KartikArora)
* **Topcoder** :
  * \*\*\*\*[**MATHEMATICS FOR TOPCODERS**](https://www.topcoder.com/thrive/articles/Mathematics%20for%20Topcoders)\*\*\*\*
  * \*\*\*\*[**BASICS OF COMBINATORICS**](https://www.topcoder.com/thrive/articles/Basics%20of%20Combinatorics)\*\*\*\*

