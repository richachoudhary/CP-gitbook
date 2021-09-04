# Design

## 1. LRU Cache

* LC [146.LRU Cache](https://leetcode.com/problems/lru-cache/)

{% tabs %}
{% tab title="OrderdDict\(FAST\)" %}
```python
from collections import OrderedDict

class LRUCache:

   def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict
        self.cache[key] = value
        
'''
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''
```
{% endtab %}

{% tab title="deque\(SLOW\)" %}
```python
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.deque = deque()
    
    def _find(self, key: int) -> int:
		""" Linearly scans the deque for a specified key. Returns -1 if it does not exist, returns the index of the deque if it exists"""
        for i in range(len(self.deque)):
            n = self.deque[i]
            if n[0] == key:
                return i 
        return -1
    
    def get(self, key: int) -> int:
        idx = self._find(key)
        if idx == -1:
            return -1
        else:
            k, v = self.deque[idx]
            del self.deque[idx] # We have to put this pair at the end of the queue so, we have to delete it first
            self.deque.append((k, v)) # And now, we put it at the end of the queue. So, the most viewed ones will be always at the end and be saved from popping when new capacity got hit.
            return v
                

    def put(self, key: int, value: int) -> None:
        idx = self._find(key)
        if idx == -1:
            if len(self.deque) >= self.size:
                self.deque.popleft()
            self.deque.append((key,value))
        else:
            del self.deque[idx]
            self.deque.append((key, value))
```
{% endtab %}
{% endtabs %}

## 2. LFU Cache 🐽

* LC [460.LFU Cache](https://leetcode.com/problems/lfu-cache/)

## 2. Movie Rental System

* LC [1912. Design Movie Rental System](https://leetcode.com/problems/design-movie-rental-system/)
* Sol: [https://leetcode.com/problems/design-movie-rental-system/discuss/1298440/Python-SortedList-solution-explained](https://leetcode.com/problems/design-movie-rental-system/discuss/1298440/Python-SortedList-solution-explained)

## From LC:

* [x] LC [1600. Throne Inheritance](https://leetcode.com/problems/throne-inheritance/)

{% tabs %}
{% tab title="1600" %}
```python
from collections import defaultdict
class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.dead = set()
        self.kingdom = defaultdict(list)
        self.root = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(root):
            if root not in self.dead:
                res.append(root)
            for nxt in self.kingdom[root]:
                dfs(nxt)
        dfs(self.root)
        return res
    
# TC:
# birth() -> O(1) || death -> O(1) || getInheritance -> O(N)
```
{% endtab %}
{% endtabs %}

