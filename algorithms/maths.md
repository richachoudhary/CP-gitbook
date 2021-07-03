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

### 2.2 Problems: Maths



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

