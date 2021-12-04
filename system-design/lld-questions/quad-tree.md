# Quad Tree

## 16.1 The WHY?

### 1. 1-D Spacial Data Representation

* To represent 1-D spacial data: => **use **<mark style="color:orange;">**Binary Search Tree**</mark>

![](<../../.gitbook/assets/Screenshot 2021-11-12 at 3.47.14 PM (1).png>)

### 2. 2-D & 3-D Spacial Data Representation

* 2-D -> <mark style="color:orange;">**Quadtrees**</mark>&#x20;
  * each node has 4 children, corresponding to quadrants of sub-plane: <mark style="color:yellow;">**\[NE, SE, SW, NW]**</mark>
* 3-D -> <mark style="color:orange;">**Octrees**</mark>&#x20;
  * each node has 8 children, corresponding to 3D octant of a sub-volume
*   **Kab tak children banate jaana hota hai in trees mei?** (for both Quadtree & Octree)

    * **=> jab tak har node ek property satisfy na kar de.**
    * <mark style="color:yellow;">**Examples plis =>**</mark>&#x20;
      * E.g#1: until every node has (1) either all 0's OR (2) all 1's



![Eg #1](<../../.gitbook/assets/Screenshot 2021-11-12 at 3.57.38 PM.png>)

* E.g#2: decompose this image until every node have same color fill

![E.g #2](<../../.gitbook/assets/Screenshot 2021-11-12 at 3.56.19 PM.png>)

* Eg #3: untill every node either (1) has grass OR (2) doesnt have grass

![](<../../.gitbook/assets/Screenshot 2021-11-12 at 3.43.39 PM.png>)

## 16.2 Implementation&#x20;

{% tabs %}
{% tab title="LC 427." %}
```python
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node(True, True, None, None, None, None)
        if len(set([item for row in grid for item in row])) == 1:   #is leaf
            root.val = bool(grid[0][0])
        else:
            root.isLeaf = False
            size = len(grid)
            root.topLeft = self.construct([row[:size//2] for row in grid[:size//2]])
            root.topRight = self.construct([row[size//2:] for row in grid[:size//2]])
            root.bottomLeft = self.construct([row[:size//2] for row in grid[size//2:]])
            root.bottomRight = self.construct([row[size//2:] for row in grid[size//2:]])
        return root
```
{% endtab %}

{% tab title="code" %}
```python
import numpy as np
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanceToCenter(self, center):
        return math.sqrt((center.x-self.x)**2 + (center.y-self.y)**2)

class Rectangle:
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
        self.west = center.x - width
        self.east = center.x + width
        self.north = center.y - height
        self.south = center.y + height

    def containsPoint(self, point):
        return (self.west <= point.x < self.east and 
                self.north <= point.y < self.south)
    
    def intersects(self, range):
        return not (range.west > self.east or
                    range.east < self.west or
                    range.north > self.south or
                    range.south < self.north)
    
    # lite:
    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1,x2,x2,x1,x1], [y1,y1,y2,y2,y1], c=c, lw=lw, **kwargs)

class QuadTree:
    def __init__(self, boundary, capacity = 4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        # if the point is in the range of current quadTree
        if not self.boundary.containsPoint(point):
            return False
        
        # if has not reached capcaity
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        
        if not self.divided:
            self.divide()

        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True

        return False
    
    def queryRange(self, range):
        found_points = []

        if not self.boundary.intersects(range):
            return []
        
        for point in self.points:
            if range.containsPoint(point):
                found_points.append(point)
        
        if self.divided:
            found_points.extend(self.nw.queryRange(range))
            found_points.extend(self.ne.queryRange(range))
            found_points.extend(self.sw.queryRange(range))
            found_points.extend(self.se.queryRange(range))
        
        return found_points
    
    def queryRadius(self, range, center):
        found_points = []

        if not self.boundary.intersects(range):
            return []
        
        for point in self.points:
            if range.containsPoint(point) and point.distanceToCenter(center) <= range.width:
                found_points.append(point)
        
        if self.divided:
            found_points.extend(self.nw.queryRadius(range, center))
            found_points.extend(self.ne.queryRadius(range, center))
            found_points.extend(self.sw.queryRadius(range, center))
            found_points.extend(self.se.queryRadius(range, center))
        
        return found_points

    def divide(self):
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.nw = QuadTree(nw)

        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.ne = QuadTree(ne)

        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.sw = QuadTree(sw)

        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.se = QuadTree(se)

        self.divided = True

    def __len__(self):
        count = len(self.points)
        if self.divided:
            count += len(self.nw) + len(self.ne) + len(self.sw) + len(self.se) 
        
        return count
    
    def draw(self, ax):
        self.boundary.draw(ax)

        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)
```
{% endtab %}

{% tab title="run_code" %}
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from quadtree import Point, Rectangle, QuadTree

DPI = 72

width, height = 600, 400

N = 1000
xs = np.random.rand(N) * width
ys = np.random.rand(N) * height
points = [Point(xs[i], ys[i]) for i in range(N)]

domain = Rectangle(Point(width/2, height/2), width/2, height/2)
qtree = QuadTree(domain)

for point in points:
    qtree.insert(point)

print('Total points: ', len(qtree))

# draw rectangles
fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

# draw points
ax.scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])

# generate the range
#center_x = np.random.rand() * width
#center_y = np.random.rand() * height
center_x = 300
center_y = 200

range_width = np.random.rand() * min(center_x, width - center_x)
range_height = np.random.rand() * min(center_y, height - center_y)

found_points = []
#range = Rectangle(Point(center_x, center_y), range_width, range_height)
#found_points = qtree.queryRange(range)
#radius = min(range_width, range_height)
radius = 150
range = Rectangle(Point(center_x, center_y), radius, radius)
found_points = qtree.queryRadius(range, Point(center_x, center_y))

print('points in range:', len(found_points))

ax.scatter([p.x for p in found_points], [p.y for p in found_points],
            facecolors='none', edgecolors='r', s=32)

range.draw(ax, c='r', lw=2)

ax.invert_yaxis()
plt.tight_layout()
plt.savefig('search-quadtree.png', DPI=72)
plt.show()
```
{% endtab %}

{% tab title="output.png" %}
![](<../../.gitbook/assets/Screenshot 2021-11-02 at 1.40.41 PM.png>)
{% endtab %}
{% endtabs %}

## 16.4 \[Util] Trigonometry: to determine direction

```python
import math

p1, p2 = (1,1), (0,0)    # touple
dx, dy = p1[0] - p2[0], p1[1] - p2[1]

angle_in_radian = math.atan2(dy,dy)              # 0.7853981633974483
angle_in_degree = angle_in_radian*180/math.pi    # 45

# ===========>  hence p1 lies in North-East of p2
```



## 16.5 Resources

* video: [Quadtrees and Octrees for Representing Spatial Information](https://www.youtube.com/watch?v=xFcQaig5Z2A\&t=443s\&ab\_channel=TylerScott)
