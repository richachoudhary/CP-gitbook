---
description: useful methods found & stolen during CP-ing
---

# methods.py

## `itertools`

* Print **all permutations** of a list/string

```python
from itertools import permutations

# for a list ==================================================
a = [1,2,3]
perms = [p for p in permutations(a)] 
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# for a string ===============================================
perms = [''.join(p) for p in permutations('abc')] 
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

## `map()`

* Takes a function & list as input; applies that function on list & returns the map object for new list.

```python
a = [1, 2, 3, 4, 5]
b = list(map(lambda arg: arg + 1, a)) #[2, 3, 4, 5, 6]
#--- usage in LC by @lee215 : get sum of max elements of each row in matrix-'grid'
hori_sum = sum(map(max, grid))
```

## `zip() `& Unzip

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
>>> zipped           # Holds an iterator object
<zip object at 0x7fa4831153c8>
type(zipped)         # <class 'zip'>
list(zipped)         # [(1, 'a'), (2, 'b'), (3, 'c')]
set(result))         # {(1, 'a'), (2, 'b'), (3, 'c')}
# ================= unzipping (using *) =========================
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
numbers  #(1, 2, 3, 4)
letters  #('a', 'b', 'c', 'd')

#--- usage in LC by @lee215 : take transpose of matix
grid = [[1,2],[3,4]]
transpose = list(zip(*grid)) # [(1, 3), (2, 4)]
```

## `bisect()` :binary search

* `import bisect`
* first element **"greater than or equal to x"** -> `index = bisect.bisect_left(arr, x)`
* first element **"greater than x"** -> `index = bisect.bisect_right(arr, x)`

```python
import bisect
li =  [1, 3, 4, 4, 4, 6, 7]
#index:0  1  2  3  4  5  6    
idx1 = bisect.bisect(li,4)          # => 5
idx2 = bisect.bisect_left(li,4)     # => 2
idx3 = bisect.bisect_right(li,4)    # => 4
```
