# generalInfo.py

* Taking input from user: `num = input ("Enter number :")`
* single line multiple **input**: `a,b=map(int,input().split())`
* take **array** as input: `arr = list(map(int, input().split()))`
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

