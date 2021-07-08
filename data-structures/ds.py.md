# dataStructures.py

### NOTEs:

* **List of Data Structures implemented in python:** [https://lei-d.gitbook.io/leetcode/data-structure](https://lei-d.gitbook.io/leetcode/data-structure)
* implement `Stack` ---&gt; with `list`
* implement `Queue` ---&gt; with `deque`

## `list`

* **declare 2D matrix :**  `[[0 for _ in range(1)] for _ in range(5)]`
* **slicing**:
  * NOTATION: `list1[start:stop:step]`
  * e.g.: `num_list[-9:]` -&gt; read it as: "9th from the end, to the end."
  * get "all but last n"  -&gt; `mylist[:-n or None]`
* **get freq** of element in list/string: `list.count(x)`
* **Insert** at given index: `list.insert(i, elem)list.insert(i, elem)`
* **enumerate**: `for i,ar in enumerate(arr): arr[i] = ar + i`
* **Reverse a list:** `a.reverse()`
* reverse traversal:
  * `for i in reversed(a)`
  * retrieve original indices: `for i, e in reversed(list(enumerate(a))):`
  * `for item in my_list[::-1]:`
* **Sort:**
  1. Normal sort\(asc\) : `list.sort()`
  2. custom sort ::  for increasing order; - for decreasing order

```python
l = [(2, 3), (3, 4), (2, 4)]
l.sort(key = lambda x: (-x[0], -x[1]) )     # [(3, 4), (2, 4), (2, 3)]
l.sort(key = lambda x: (x[0], -x[1]) )      # [(2, 4), (2, 3), (3, 4)]
```



## `string`

* **str-&gt;list**  **:** split a string by char: `s = txt.split("#")`
* **list-&gt;str  :** join a list by char into string: `list1 = ['1', '2', '3'] str1 = ','.join(list1)`
* **get freq** of element in list/string: `list.count(x)`
* **Casing**: 
  * Check casing:  `mystr.islower()`
  * Change case: `string.lower()`
* **Substring find/StrStr :** Search: `s.find(t)` -&gt; returns **first** index or -1
* **Reverse: `str[::-1]`**

## `set`

* **declare a set**:
  * `s = set()`
  * `s = {}`
* create set from list: `s = set(list1)`
* **size** of set: `len(set1)`
* check if element **exists** in set: `if x in s`
* insert element in set: `s.add(x)`
* remove element from set: `s.remove(x)`
* **Set Operations:**
  * union: `s = set1 | set2`
  * intersection: `s = set1 & set2`
  * diff: `s = = set1 - set2`
  * take the union and exclude the intersection of a pair of sets: `s = set1 ^ set2`
* **filter** unique elements in arr: `arr = list(set(arr))`
* **Check if subset:** `A.issubset(B)`
* set to list: `list1 = list(set1)`
* sorted order: `for k, v in sorted(d.items())`





## `dict`: 

* Its is a hashmap of key-value pairs
* Creating a dictionary:
  *   `d={}`
  *  `d= dict()`
* **Populating** a key with a value: `d["foo"] = "bar"`
* To **check if** a dictionary **has a key**:  `foo in d`
* **Deleting** a key as well as its value: `del d["foo"]`
* **Iterating**: `[(k,v) for k,v in d.items()]`
* get only **keys**\(as list\): `list1 = list(d)`
* get only **values**\(as list\): `list2 = d.values()`
  * Count of keys with val == k:  `res = sum(x == K for x in d.values())`

### `Counter` as dict

* **BETTER Use Counter :** use `count = collections.Counter()` as dict..._very short & convenient_
  * WHAT: Python Counter is a subclass of the dict or dictionary class. It keeps track of the frequency of each element in the container.
  * WHAT: Counter counts hashable objects in Python
  * Observe that _counts_ are always displayed in _**descending order**_
  * **Basics**:

    ```python
      from collections import Counter   #(generally its auto-imported) 

      # for list
      d = Counter(['a','b','c','a','b','a']) # Counter({‘a’: 3, ‘b’: 2, ‘c’: 1})
      # for string
      d2 = Counter("Hello World") # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
      # for tuple
      d3 = Counter(('a','b','c','a','b','a'))  # Counter({‘a’: 3, ‘b’: 2, ‘c’: 1})
    ```

  * **Counters with set**: since sets only have unique elements, it doesnt make sense to use counters with set
  * **Counters with dict**`my_count = Counter({'a':3, 'b':2, 'c':1})   # Counter({'a':3, 'b':2, 'c':1})`
  * **UPDATING**:

    ```python
      my_count = Counter()        # defining an empty Counter
      my_count.update("a")        # Counter({a:1})
      my_count.update("ab")       # Counter({'a': 2, 'b': 1})
    ```

  * Get top `n` **highest frequency elements**: `my_count.most_common(2)`
  * Get top `n` **lowest frequency elements:** `my_count.most_common()[:-n:-1]`
  * **wow\(@lee215\)** : `return ["%d %s" % (count[k], k) for k in count]`

### `defaultdict` as dict <a id="defaultdict"></a>

* similar to dict\(returns a dictionary-like obj\) 
* advantage: `defualtdict` _never raises a KeyError_
* **Initialization:** i.e. what to show when key not present:
  *  `d = defaultdict(`**`default_value`**`)`
  * **\(Usage\)**e.g: `d = defaultdict(list)` =&gt; gives empty list \(_useful in graphs_\)

\_\_

## `heapq` - min heaps

* returns somewhat sorted list
* Usage:

```python
import heapq
heapq.heapify(list1)
```

* **push** new element: `heapq.heappush(a, 4)`
* **delete** min element: `heapq.heappop(a)`
* get **n-smallest elements**: `heapq.nsmallest(n,list1)`
* get **n-largest elements**: `heapq.nlargest(n,list1)`
* **MIN\_HEAP:** Use it like this\(with plain list + hepq operations while insert & get\) 

```python
import heapq

hp = []   # plain-ol-list
# inserting a new element
heapq.heappush(hp,x)
# pop the smallest element in heap
heapq.heappop(hp)
# get the smallest element in heap
hp[0]
```

* **MAX\_HEAP**, converting list to `(-1)*list` helps:
  * e.g. [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)



## `deque`

* A list-like container with fast appends & pops on either end.Implemented using **doubly-linked list**.
* Usage:

{% tabs %}
{% tab title="deque" %}
```python
from collections import deque
de = deque(list1)

#********************* All Popping & Appending is O(1) ***************
de.append(1)
de.pop() # 1
de.appendleft(0)
de.popleft() # 0
#********************* All Popping & Appending is O(1) ***************
#********************* Reading for list is now O(N) ***************
de[3]  # random-access now takes O(n) time
de[0]
de[-1]

# other(possibly) useful ops
d.clear()
dq.reverse()
```
{% endtab %}
{% endtabs %}

