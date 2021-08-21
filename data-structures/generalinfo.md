---
description: Python is about 2-4x slower than C++
---

# generalInfo

* **Constraints during Contests:**
  * If n ≤ 12          ===&gt; O\(n!\).
  * If n ≤ 25          ===&gt; O\(2^n\).
  * If n ≤ 100         ===&gt; O\(n^4\).
  * If n ≤ 500         ===&gt; O\(n^3\).
  * If n ≤ 5000        ===&gt; O\(n^2\).
  * If n ≤ 10^6        ===&gt; O\(n log n\).
  * If n ≤ 10^8        ===&gt; O\(n\).
  * If n &gt; 10^8        ===&gt; O\(log n\) or O\(1\)
* **C++ :: Ranges**
  * **int** :is a 32-bit type. its values range of `−2^31` ...`2^31  - 1` or about `−2*(10^9) ...2·(10^9)`
  * **long long:** :is a 64-bit type.values range `−2^63 ...(2^63 -1)` or `-9*(10^18) ...9·(10^18)`
  * **\_\_int128\_t :** 128-bit. `−2^127 ...(2^127 -1)` or `-(10^38) ...(10^38)`
* **C++ :: Policy Base Data Structure\(pbds\): `indexed_set`**

  * set with index based search\(like array\) i.e. normal `set` doesnt support `s[3],` this one does!
  * All methods\(**`find_by_order`**, **`order_of_key`**\) work in **`O(logN)`** time

```cpp
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,
                tree_order_statistics_node_update> indexed_set;

indexed_set s;
s.insert(2);
s.insert(3);
s.insert(7);
s.insert(9);    

auto x = s.find_by_order(2);
cout << *x << "\n"; // 7    
cout << s.order_of_key(7) << "\n"; // 2

//If the element does not appear in the set,
//we get the position that the element would have in the set  
cout << s.order_of_key(6) << "\n"; // 2
cout << s.order_of_key(8) << "\n"; // 3      
```

{% hint style="info" %}
For any question related to **Ordered Containers\(heap,set,multiset\) ====&gt; DONOT USE PYTHON**
{% endhint %}

* **Taking Input:**

  * Taking input from user: `num = input ("Enter number :")`
  * single line multiple **input**: `a,b=map(int,input().split())`
  * take **array** as input: `arr = list(map(int, input().split()))`
  * **HACK:**

  \*\*\*\*

```python
I = lambda : map(int, input().split())     # one line to rule them all

#=========== USAGE ==================
#1. multiple inputs as integers
n, x = I()
l = list(I())
#2. input a list:
for p in I():
    # do your thing here
```

* using int\_min & int\_max in py:
  * **Way1:** recommended: `float('inf')` & `float('`-`inf')`
  * **Way**2**:** Not-recommended `-sys.maxsize`, `sys.maxsize`
* Python's modular exponentiation method: `pow(base,expo,mod)`
* char to int & vv: \(its `chr` not char\)

  ```text
  >>> chr(97)
  'a'
  >>> ord('a')
  97
  ```

* Quickly generate alphabet list/dict

```python
import string
l = list(string.ascii_lowercase)    # ['a','b',....,'z']
letter_count = dict(zip(string.ascii_lowercase, [0]*26)) # {'a':1, 'b':1, ...'z':1}
```

* **Mutable Data Types in python: 🟢**
  * list
  * set
  * dict
* **Immutable Data Types in python: 🔴**
  * String                     \(fucking @Sanjay saying-"Strings are immutable"\)
  * Tuples

