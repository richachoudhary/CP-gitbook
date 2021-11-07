# Geometry

## 0. Notes

* Heron's formula for area of triangle![\text{ Area }=\sqrt{s(s-a)(s-b)(s-c)}](https://www.gstatic.com/education/formulas2/355397047/en/heron\_s\_formula.svg)
* Set theory conventions **∀ (for all) and ∃ (there is).**
  *   For example, **`∀x(∃y(y<x))`**

      \===> means that **for each** element x in the set, **there is** an element y in the set **such that** y is smaller than x

```python
# Cross Product
'''
         i   j   k
AXB = |  x1  y1  z1 |
      |  x2  y2  z2 |
    = (y1z2 - y2z1) i - (x1z2 - x2z1) j + (x1y2 - x2y1) k
'''
```

## 1. Problems

#### 1.2.1 Easy 🧠

* [x] [1266.Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)
* [x] [883. Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/)
* [x] [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/)
* [x] [892. Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/)

{% hint style="info" %}
For problems like (**#892**) :in geometry of 3-D blocks: think in terms of subtracting the overlap, not adding each block one-by-one.
{% endhint %}

* [x] LC: [149.Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | just count all the slopes b/w all 2 pair points
* [x] Check collinearity : [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
  * [x] Similar: [1037.Valid Boomerang](https://leetcode.com/problems/valid-boomerang/)
* [x] LC [218.The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) ✅🌇| uses \*\*SortedList \*\*

{% tabs %}
{% tab title="892" %}
```python
# Intution: 
# * For each tower, its surface area is 4 * v + 2
# * However, 2 adjacent tower will hide the area of connected part.
# * The hidden part is min(v1, v2) and we need just minus this area * 2 :
#     * This is because each of the two prisms is double counting the face that touches, e.g. the face that represents the minimum of the two heights

n, res = len(grid), 0
for i in range(n):
    for j in range(n):
        if grid[i][j]: res += 2 + grid[i][j] * 4
        if i: res -= min(grid[i][j], grid[i - 1][j]) * 2
        if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
return res
```
{% endtab %}

{% tab title="149" %}
```python
#2. count slopes ==========================

INT_MAX = 10**5
res = 0

if n <= 2:
    return n

for i in range(n-1):
    samePoint = 1
    slopes = dict()
    for j in range(i+1,n):
        p1, p2 = points[i],points[j]
        
        if p1 == p2:
            samePoint += 1
        elif p2[0]-p1[0] == 0:
            if INT_MAX in slopes:
                slopes[INT_MAX] += 1
            else:
                slopes[INT_MAX] = 1
        else:
            x = (p2[1]-p1[1])/(p2[0]-p1[0])
            if x in slopes:
                slopes[x] += 1
            else:
                slopes[x] = 1
                
    localres = 0
    for k,v in slopes.items():
        localres = max(localres,v)
    localres += samePoint
    res =  max(res,localres)
        
return res
```
{% endtab %}

{% tab title="1232" %}
```python
(x0, y0), (x1, y1) = coordinates[: 2]
for x, y in coordinates:
    if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
        return False
return True
```
{% endtab %}

{% tab title="218.🌇" %}
```python
from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        
        for l,r,h in buildings:
            events.append((l,h,-1)) #starting event
            events.append((r,h,1))  #ending event
            
        events.sort()   #sort by X cordinate
        n = len(events)
        
        res = []
        active_heights = SortedList([0]) #min heap of curr all hights in current window
        
        i = 0
        while i<n:
            curr_x = events[i][0]
            
            #process all events with same X together
            while i<n and events[i][0] == curr_x:
                x,h,t = events[i]
                
                if t == -1:                      #starting event
                    active_heights.add(h)
                else:
                    active_heights.remove(h)    #ending event
                i += 1
                
            #check if biggest height has changed in window due to this event
            if len(res) == 0 or (len(res) > 0 and res[-1][1] != active_heights[-1]):
                res.append((curr_x, active_heights[-1]))
        return res
```
{% endtab %}
{% endtabs %}

* [x] [836.Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) 💡
* [x] CSES: [Point Location Test](https://cses.fi/problemset/task/2189) | ✅✅**Cross Product**
* [x] CSES: [Line Segment Intersection](https://cses.fi/problemset/task/2190) ✅✅ | `Boundary Box Technique` |**COVERS SO MANY CONCEPTS!**
* [x] CSES: [Polygon Area](https://cses.fi/problemset/result/2677213/) ✅✅
* [ ] CSES: [Point in Polygon](https://www.youtube.com/watch?v=G9QTjWtK\_TQ) 🐽🐽| [video](https://www.youtube.com/watch?v=G9QTjWtK\_TQ\&t=5265s)
* [ ] CSES: [Convex Hull](https://cses.fi/problemset/task/2195) ✅✅ | [video](https://www.youtube.com/watch?v=G9QTjWtK\_TQ\&t=7801s) | \*\*Graham Scan+Jarvis Algo >> \*\*shape of rubber band on nails boundary
* [x] LC [750. Number Of Corner Rectangles](https://sugarac.gitbooks.io/facebook-interview-handbook/content/number-of-corner-rectangles.html) | **@uber**
* [x] LC [939. Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | **@uber**

{% tabs %}
{% tab title="PointLocationTest" %}
```python
'''
         i   j   k
AXB = |  x1  y1  z1 |
      |  x2  y2  z2 |
    = (y1z2 - y2z1)i - (x1z2 - x2z1)j + (x1y2 - x2y1)k
'''

def solve():
    I = lambda : map(int,input().split())
    t = int(input())

    for _ in range(t):
        x1,y1,x2,y2,x3,y3 = I()
        # shift origin to (x1,y1)
        x2,y2 = x2-x1, y2-y1
        x3,y3 = x3-x1, y3-y1

        cross = x3*y2 - x2*y3
        if cross > 0:
            print("RIGHT")
        elif cross < 0:
            print("LEFT")
        else:
            print("TOUCH")
```
{% endtab %}

{% tab title="LineSeg Intersection" %}
```python
'''
#1. check if both lines are COLINEAR YET PARALLEL:

        -----------      -----------
        p1        p2     p3     p4
                    OR
            ----===============--------
            p1  p2            p3      p4 
#2.We need to check:   #hence for _ in range(2): which swaps points in end.easy implementation 😎
    1. line1's endponits signs w.r.t. line2
    2. line2's endponits signs w.r.t. line2
cuz if just 1 or 2 checked, we'll give wrong o/p for this case:
            |
--------    | opposite signs but still "NO" intersection 
            |
'''
x1,y1,x2,y2,x3,y3,x4,y4 = I()
#1.================================== colinear & parallel
if cross(x2,y2,x1,y2) * cross(x4,y4,x3,y3) == 0:
    # just exclude the case when the're not COLLINEAR
    # 1.    -----------
    #      ----------------     => NO
    #
    # 2. 
    #    --------   ---------     => NO
    # 3.
    #     -------==========-------  => YES
    #
    # 
    # check for case#1 : 
    if cross(x2-x1,y2-y1,x3-x1,y3-y1) != 0:
        print("NO")
        break

    # check for case#2 : collinear with Boundary-Box technique
    isSolved = False
    for _ in range(2):
        if max(x2,x1) < min(x3,x4) or max(y2,y1) < min(y3,y4):
            print("NO")
            isSolved = False
        x1,y1,x2,y2,x3,y3,x4,y4 = x3,y3,x4,y4,x1,y1,x2,y2
    
    if not isSolved:
        print("YES")    #case#3
    break
#2. ================================= skewed
for _ in range(2):
    # shift origin to (x1,y1)
    cross1 = cross(x2-x1,y2-y1,x3-x1,y3-y1)
    cross2 = cross(x2-x1,y2-y1,x4-x1,y4-y1)
    
    if cross1*cross2 > 0 :  #both #3 & #4 lie on same side from line 1-->2
        print("NO")
        return
    x1,y1,x2,y2,x3,y3,x4,y4 = x3,y3,x4,y4,x1,y1,x2,y2
if not isSolved:
    print("YES")
```
{% endtab %}

{% tab title="PolyArea" %}
```python
'''
IDEA: 
    * take one edge of polygon & draw lines to all other edges => dividing the polygon into Triangles.
    * Calculate sum of areas of trianges : AreaTriangle =  cross_product//2
    * NOTE: the trick works for both: CONVEX & CONCAVE ploygon (CROSS Product takes care of + & -ve areas)
'''

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def cross(p1,p2,p3): # (p2 - p1) X (p3 - p1)

    a = (p2.x-p1.x)*(p3.y-p1.y) # 3*2
    b = (p3.x-p1.x)*(p2.y-p1.y) # 2*
    return (p2.x-p1.x)*(p3.y-p1.y) - (p3.x-p1.x)*(p2.y-p1.y)

def solve():
        
    I = lambda : map(int, input().split()) 
    n = int(input())
    points = []
    for _ in range(n):
        x,y = I()
        p = Point(x,y)
        points.append(p)

    # fix P0
    res = 0
    for i in range(1,n-1):
        res += (cross(points[0],points[i],points[i+1]))

    print(abs(res)//2) 
    
```
{% endtab %}

{% tab title="750" %}


**Solution 1:**\
One straight-forward solution is: we can iterate any two rows, say r1 and r2, and for every column, we check if grid\[r1]\[c] == grid\[r2]\[c]. IF yes, we increate the count by 1. Then the number of rentangles formed by these two rows are count \* (count - 1) / 2.\
\
The time complexity of the solution is O(m^2 \* n). \
\
If the number of rows is significantly greater than number of columns, we can iterate the columns and check the rows for each of the two columns. Then the time complexity is&#x20;

O(n^2 \* m).

```java
public int countCornerRectangles(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length - 1; i++) {
            for (int j = i + 1; j < grid.length; j++) {
                int counter = 0;
                for (int k = 0; k < grid[0].length; k++) {
                    if (grid[i][k] == 1 && grid[j][k] == 1) counter++;
                }
                if (counter > 0) ans += counter * (counter - 1) / 2;
            }
        }
        return ans;
    }
```

\
**Solution 2:**\
Solution 2 is similar to solution 1. The main difference is we use a hash map to save the positions of the two rows.

_**Time Complexity:** O(N\*(M^2))_\
_**Auxiliary Space:** O(M^2)_\


```java
public int countCornerRectangles(int[][] grid) {
        if (grid == null || grid.length < 2 || grid[0] == null || grid[0].length < 2) {
            return 0;
        }
         
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
         
        int m = grid.length;
        int n = grid[0].length;
         
        for (int r1 = 0; r1 < m; r1++) {
            for (int r2 = r1 + 1; r2 < m; r2++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r1][c] == 1 && grid[r2][c] == 1) {
                        int pos = r1* n + r2;
                        if (map.containsKey(pos)) {
                            int val = map.get(pos);
                            ans += val;
                            map.put(pos, val + 1);
                        } else {
                            map.put(pos, 1);
                        }
                    }
                }
            }
        }
         
        return ans;
    }
```
{% endtab %}

{% tab title="939" %}
```python
def minAreaRect(self, points: List[List[int]]) -> int:

    seen = set()
    res = float('inf')
    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                area = abs(x1 - x2) * abs(y1 - y2)
                if area and area < res:
                    res = area
        seen.add((x1, y1))
    return res if res < float('inf') else 0

'''
TC: O(N^2)
'''
```
{% endtab %}
{% endtabs %}

## 2. Problemsets

* **`[E]`** Leetcode tag = **geometry:** [https://leetcode.com/problemset/all/?topicSlugs=geometry](https://leetcode.com/problemset/all/?topicSlugs=geometry)
* Codeforces Tag = **geometry** : [https://codeforces.com/problemset?tags=geometry](https://codeforces.com/problemset?tags=geometry)

## 3. Resources

* [CSES Steam by Errichto](https://www.youtube.com/watch?v=G9QTjWtK\_TQ) 🚀⭐️
* [Geometric Algorithms](https://www.cs.princeton.edu/\~rs/AlgsDS07/16Geometric.pdf)
* Topcoder:
  * [GEOMETRY CONCEPTS PART 1: BASIC CONCEPTS](https://www.topcoder.com/thrive/articles/Geometry%20Concepts%20part%201:%20Basic%20Concepts)
  * [GEOMETRY CONCEPTS PART 2: LINE INTERSECTION AND ITS APPLICATIONS](https://www.topcoder.com/thrive/articles/Geometry%20Concepts%20part%202:%20%20Line%20Intersection%20and%20its%20Applications)
  * [LINE SWEEP ALGORITHMS](https://www.topcoder.com/thrive/articles/Line%20Sweep%20Algorithms)
* [Al.Cash's blog](https://codeforces.com/blog/entry/48122)
* [Handbook of geometry for competitive programmers](https://vlecomte.github.io/cp-geo.pdf)
