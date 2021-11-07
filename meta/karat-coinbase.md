# Karat@Coinbase

## DSA

* LC 588. [Design In-Memory File System](https://leetfree.com/problems/design-in-memory-file-system)
* [339. Evaluate Division](https://leetcode.com/problems/evaluate-division/)
* **Textbook Buy Sell**
* [**CurrencyConversion**](https://leetcode.com/discuss/interview-question/483660/google-phone-currency-conversion)
* **Currency Arbitrage**: Now given any two currencies x and y. Find the best conversion rate. Basically a graph problem you will have to traverse all paths from x to y because you want the best conversion rate.
  * **follow up** - Rather than hardcoding the data use two apis - 1.) [https://api.pro.coinbase.com/products](https://api.pro.coinbase.com/products) to get the id like USD-EUR aka currency pair and 2.) [https://api.pro.coinbase.com/products/](https://api.pro.coinbase.com/products/)" + id + "/book to fetch the ask and bid price for each one of them. response = request.get(url) is enough to handle the GET calls + response.json() is enough to parse the response.

faf

{% tabs %}
{% tab title="588.MyFileSys" %}
```python
# l is the path length, 
# k is the number of entries in the last level directory(max_possible_path_len)
# =====================================
# Time:  ls: O(l + klogk), 
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.


class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""


class FileSystem:
    def __init__(self):
        self.__root = TrieNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.__root
        subdirs = path.split("/")[1:]
        if path == '/':
            subdirs = []
        for s in subdirs:
            curr = curr.children[s]

        #if its a file_path; return a list which only has this file's name
        # => lexicographical order
        if curr.is_file:
             return [subdirs[-1]]

        #if its a directory path: return lsit of file+directory names
        # in this directory 
        # => lexicographical order
        return sorted(curr.children.keys())

    # mkdir: O(l) ; l = path length
    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.__root
        subdirs = path.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_file = False
        return curr

    def readContentFromFile(self, filePath):
        """ 
        :type filePath: str
        :rtype: str
        """
        curr = self.__root
        subdirs = filePath.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr.content
    
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.__root
        subdirs = filePath.split('/')[1:]  # because every path starts with extra '/
        for s in subdirs:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_file = True
        curr.content += content

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir('/a/b/c')
    fs.addContentToFile('/a/b/c/d', 'hello')
    print(fs.ls("/"))
    print(fs.readContentFromFile('/a/b/c/d'))
    print(fs.ls("/a/b/c/d"))
```
{% endtab %}

{% tab title="(posh)588.FileSys" %}
```python
# l is the path length, 
# k is the number of entries in the last level directory
# =====================================
# Time:  ls: O(l + klogk), 
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.


class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""


class FileSystem:
    def __init__(self):
        self.__root = TrieNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.__getNode(path)

        if curr.is_file:
            return [self.__split(path, "/")[-1]]

        return sorted(curr.children.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.__putNode(path)
        curr.is_file = False

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.__putNode(filePath)
        curr.is_file = True
        curr.content += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.__getNode(filePath).content

    def __getNode(self, path):
        curr = self.__root
        for s in self.__split(path, "/"):
            curr = curr.children[s]
        return curr

    def __putNode(self, path):
        curr = self.__root
        for s in self.__split(path, "/"):
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr

    def __split(self, path, delim):
        if path == "/":
            return []
        return path.split("/")[1:]


if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir('/a/b/c')
    fs.addContentToFile('/a/b/c/d', 'hello')
    print(fs.ls("/"))
    print(fs.readContentFromFile('/a/b/c/d'))
    print(fs.ls("/a/b/c/d"))
```
{% endtab %}

{% tab title="TextbookBuySell" %}
```python
"""
You operate a market place for buying & selling used textbooks For a giventext book eg“TheoryofCryptography”
there are people who want to buy this textbook and people who want to sell

Offers to BUY: $100 $100 $99 $99 $97 $90
Offers to SELL: $109 $110 $110 $114 $115 $119

A match occurs when two people agree on a price 
Some new offers do not  match. These offers should be added to the active set of offers.

For example : Tim offers to SELL at $150 This will not match No one is willing to buy at that price so we save the offer

Offers to SELL::$109 $110 $110 $114 $115 $119 $150

When matching we want to give the customer the “best price”

Example matches : If Jane offers to BUY at $120

she will match and buy a book for $109 (the lowest offer)



====================== [APPROACH] ==================
Use two heaps. 
1. Max Heap : buy orders
2. Min Heap : sell orders

>>> Processing:
1. Buy Order Req comes(p):
    * we want to lowest sell price in list i.e. top of sell minH
    Case#1: (p > max_sell) there's a match => process order
    Case#2: (p <= max_sell)  not a match => add this in buy's heap for future

2. Sell Order req comes(p):
    * get top_val_from_buy_max_heap
    Case#1: (p < max_buy) match => process
    Case#2: (p >= max_buy): store in sell order's list

TC: O(n logn) --> because we put everything in the heaps which are O(log n) per offer/poll operations.
SC: O(n) --> we're putting the entire input lists in the heaps

"""
from heapq import heappush, heappop


class TextBookMarket():
    def __init__(self,buy_requests, sell_requests):
        self.__buy_requests = buy_requests
        self.__sell_requests = sell_requests
        self.__sell_min_heap = []
        self.__buy_max_heap = []
        self.__initialize_marketplace()
    
    def __initialize_marketplace(self):
        for sell in self.__sell_requests:
            heappush(self.__sell_min_heap, sell)
            
        # implement max heap
        for buy in self.__buy_requests:
            heappush(self.__buy_max_heap, -buy)

        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
    
    def process_buy(self, buy):
        max_sell = heappop(self.__sell_min_heap)
        if buy > max_sell:
            profit =  buy - max_sell
            print(f'\tPROFIT = {profit}')
            return profit
        print('your order has been stored.Please wait for better opportunity')
        heappush(self.__buy_max_heap,-buy)
        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
        return None
    
    def process_sell(self,sell):
        max_buy = (-1)*heappop(self.__buy_max_heap)
        
        if sell > max_buy:
            profit = sell - max_buy
            print(f'\tPROFIT = {profit}')
            return profit
        print('your order has been stored.Please wait for better opportunity')
        heappush(self.__sell_min_heap,sell)
        print(self.__sell_min_heap)
        print(self.__buy_max_heap)
        return None

buys = [100, 100, 99, 99, 97, 90]
sells = [109, 110, 110, 114, 115, 119]

market = TextBookMarket(buys,sells)
market.process_buy(120)
market.process_buy(113)
market.process_buy(90)
```
{% endtab %}

{% tab title="339" %}
```python
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    G = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v
        
    def bfs(src, dst):
        if not (src in G and dst in G): return -1.0
        q, seen = [(src, 1.0)], set()
        for x, v in q:
            if x == dst: 
                return v
            seen.add(x)
            for y in G[x]:
                if y not in seen: 
                    q.append((y, v*G[x][y]))
        return -1.0
    return [bfs(s, d) for s, d in queries]
```
{% endtab %}

{% tab title="CurrencyConversion" %}
```python
from collections import defaultdict
from collections import deque

def getRatio(start, end, data):
    adj = defaultdict(list)
    vis = dict()
    for node in data:
        adj[node[0]].append([node[1], node[2]])
        adj[node[1]].append([node[0], 1.0 / node[2]])
        vis[node[0]] = False
        vis[node[1]] = False
    
    # start BFS
    queue = deque()
    queue.append((start, 1.0))
    
    while queue:
        curr, num = queue.popleft()
        if vis[curr]:
            continue
        vis[curr] = True
         
        if curr in adj:
            values = adj[curr]
            neighbors = {}
            for val in values:
                neighbors[val[0]] = val[1]
            for key in neighbors:
                if not vis[key]:
                    if key == end:
                        res = num * neighbors[key]
                        return round(res,2)
                    queue.append((key, num * neighbors[key]))
    return -1


data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("GBP", "AUD", data))

''' ================= APIs =================='''
import requests, json
resp =  requests.get('http://api.pro.coinbase.com/products').json()
print(resp[0]['id'])
```
{% endtab %}

{% tab title="Currency Arbitrage" %}
```python
from math import log

def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float("inf")] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    print(min_dist)
    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]
print(arbitrage(rates))

'''

TC: O(N^3)
SC: O(N^2)

For example, say we have a weighted edge path a -> b -> c -> d. 
Since we want to see if a * b * c * d > 1, we’ll take the negative log of each edge:

-log(a) -> -log(b) -> -log(c) -> -log(d).

The total cost of this path will then be

-(log(a) + log(b) + log(c) + log(d)) = -log(a * b * c * d).

-log(x) < 0 if x is greater than 1, so that’s why if we have a negative cost cycle, if means that the product of the weighted edges is bigger than 1.

The Bellman-Ford algorithm can detect negative cycles. So if we run Bellman-Ford on our graph and discover one, then that means its corresponding edge weights multiply out to more than 1, and thus we can perform an arbitrage.

'''
```
{% endtab %}
{% endtabs %}

fafa

## HLD:

* **Slack**
  * how will you mark the message read.
  * API + storage layer (main focus),
  * how will you push notifications.
  * How will you show "someone is typing.." kinda feature
    * \=> Mostly like whoever is typing send updates to cache with the timestamp and then UI can fetch cache data. Not a very efficient approach because later the interviewer told me that Spotify actually open Websockets for each client. It doesn't depend on long polling method. I didn't verify the interviewer's claim. Actually, in all the notification services based interviews, I have seen the crux is how do you send the data from server to the client. Usually, the interviewers are happy with long polling strategy or fixed interval-based check.
* **Stock Exchange**
  * Design a ordering system for stocks. Users will place orders and cancel orders. Think about race conditions when trying to cancel an order before executed. Users can also schedule orders in the future.

1st technical screen was an LC medium, nothing too crazy, I think most people could do it here if they know about arrays. It is very important to display 'clear communication' during these rounds as it is one of Coinbase's core values.

Onsite: 2 pair programming and 1 system design.

First pair programming was an OOP related question with some minor algorithms. The focus here is on getting a working solution and communicating clearly.

Second pair programming was actually pretty heavily algorithm involved although you also needed some OOP principles. (I signed an NDA so I can't disclose Coinbase questions)

The system design was very generic and I think watching enough Youtube videos would be enough help here.I can't disclose exactly but on a high-level it was essentially like designing a system that periodically fetches data from an API and uses it in the system.

I received an offer only 2 days after!

_3rd round (1 hour):_\
This was a coding interview. The question was given a list of buy and sell orders, try to find the maximum profit a trader can make?\
After solving the question, I was given few practical real world problems a cryptocurrency exchange faces and was asked how I would solve it.\
After a week I got a reject.

On-site Round 1: System Design. Design Slack. Question regarding how will you mark the message read. API + storage layer (main focus), how will you push notifications. How will you show "someone is typing.." kinda feature.

**Phone Screen**

* a way for users to buy and sell stocks
* match buyers with the lowest seler (<= buyer's price)
* match sellers with the highest buyer (>= seller's price)

**Onsite**\
Currency Exchange

* a list of currency relationships with exchange values. (BTC - USD)
* find the best exchange rate from currency1 to currency2

Game

* connect 4
* OOP design

System Design

* design slack and slack related features (show "some one is typing" etc)

Behavioral

* cross team collaboration
* career aspiration etc.

## Pair Programing#2

###

## Question Bank:

* [Chinese doc1](https://juejin.cn/post/6844904085913600008)
* [Cinenes doc2](https://www.jianshu.com/p/fdbcba5fe5bc)

## 0. Dependency Injec**ti**on

Dependency injection is a principle that helps to decrease coupling and increase cohesion.![../\_images/coupling-cohesion.png](https://python-dependency-injector.ets-labs.org/\_images/coupling-cohesion.png)

What is coupling and cohesion?

Coupling and cohesion are about how tough the components are tied.

* **High coupling**. If the coupling is high it’s like using a superglue or welding. No easy way to disassemble.
* **High cohesion**. High cohesion is like using the screws. Very easy to disassemble and assemble back or assemble a different way. It is an opposite to high coupling.

**Without Dependency Injection (DI):**

```java
class Car{
  private Wheel wh = new NepaliRubberWheel();
  private Battery bt = new ExcideBattery();

  //The rest
}
```

**After using dependency injection:**

Here, we are **injecting** the **dependencies** (Wheel and Battery) at runtime. Hence the term : _Dependency Injection._ We normally rely on DI frameworks such as Spring, Guice, Weld to create the dependencies and inject where needed.

```java
class Car{
  private Wheel wh; // Inject an Instance of Wheel (dependency of car) at runtime
  private Battery bt; // Inject an Instance of Battery (dependency of car) at runtime
  Car(Wheel wh,Battery bt) {
      this.wh = wh;
      this.bt = bt;
  }
  //Or we can have setters
  void setWheel(Wheel wh) {
      this.wh = wh;
  }
}
```

## 1. Find Rectangles

{% tabs %}
{% tab title="problem.txt" %}
```
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

There are N shapes made up of 0s in the image. They are not necessarily rectangles -- they are odd shapes ("islands"). Find them.

image1 = [
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1, 1],
  [1, 0, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [0, 1, 0, 1, 1, 1, 0],
]

Every single pixel in each shape. For reference, these are (in [row,column] format):

findShapes(image1) =>
  [
    [[0,1],[1,1],[1,2]],
    [[1,4],[2,3],[2,4],[2,5],[3,4]],
    [[3,1],[4,1],[4,3],[5,1],[5,2],[5,3],[5,4],[6,3],[6,4]],
    [[7,6]],
  ]


Other test cases:

image2 = [
  [0],
]

findShapes(image2) =>
  [
    [[0,0]],
  ]

image3 = [
  [1],
]

findShapes(image3) => []

n: number of rows in the input image
m: number of columns in the input image

作者：Esc1pe
链接：https://juejin.cn/post/6844904085913600008
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
{% endtab %}

{% tab title="solution.py" %}
```python
def solve(image):
    n,m = len(image), len(image[0])
    nei = [(1,0),(0,1),(-1,0),(0,-1)]
    
    def dfs(x,y,island,image):
        image[x][y] = 1
        island.append([x,y])
        
        for dx,dy in nei:
            nx, ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and image[nx][ny] == 0:
                dfs(nx,ny,island,image)
    
    res = []
    for i in range(n):
        for j in range(m):
            if image[i][j] == 0:
                island = []
                dfs(i,j,island,image)
                #calculate its island
                if len(island) > 1:
                    res.append(island)

    for r in res:
        print(r)


def test1():
    image = [
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 0],
    ]
    solve(image)


def test2():
    image = [
        [0],
    ]
    solve(image)


def run_tests():
    test1()
    test2()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}
{% endtabs %}

## 2. Task By Level | cook sleep

* (Similar: FindLeaves, [LeetCode 366](https://leetfree.com/problems/find-leaves-of-binary-tree))

{% tabs %}
{% tab title="problem.txt" %}
```
input = {
{"cook", "eat"},   // do "cook" before "eat"
{"study", "eat"},
{"sleep", "study"}}

output (steps of a workflow):
{{"sleep", "cook"},.
{"study"},
{"eat"}}
```
{% endtab %}

{% tab title="solution.py" %}
```python
from collections import defaultdict, deque


def solve(tree):
    par = dict()
    nodes = set()
    
    # build indeg=======================
    for x, y in tree:
        nodes.add(x)
        nodes.add(y)

    indeg = dict()
    for node in nodes:
        indeg[node] = 0

    for x, y in tree:
        par[y] = x
        indeg[x] += 1
    # print(par)
    # print(indeg)
    # topological sort =====================
    res = []
    Q = []
    for k,v in indeg.items():
        if v == 0:
            Q.append(k)
            
    while Q:
        n = len(Q)
        leaves = []
        for _ in range(n):
            x = Q.pop(0)
            leaves.append(x)
            
            # if supe_parent is reached
            if x not in par.keys():
                break
            
            indeg[par[x]] -= 1
            if indeg[par[x]] == 0:
                Q.append(par[x])
        res.append(leaves)
    print(res)
            

def test1():
    tree = [[1, 2], [1,3], [2,4], [2,5]]  # do y before x
    solve(tree)

def test2():
    tree = [
        ["eat","cook"],
        ["eat","study"],
        ["study","sleep"]
    ]  # do y before 1x
    solve(tree)



def run_tests():
    test1()
    test2()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}
{% endtabs %}

## 3. Badge Access

{% tabs %}
{% tab title="problem.txt" %}
```
# Pt1: ===============================================================
We are working on a security system for a badged-access room in our company's building. 
Given an ordered list of employees who used their badge to enter or exit the room, 
write a function that returns two collection

All employees who didn't use their badge while exiting the room 
  – they recorded an enter without a matching exix
All employees who didn't use their badge while entering the room  
  – they recorded an exit without a matching enter

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],. 1point3acres.com/bbs
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],. more info on 1point3acres.com
  ["Paul",     "enter"],. From 1point 3acres bbs
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]
find_mismatched_entries(badge_records)
Expected output: ["Paul", "Curtis"], ["Martha"]

# Pt2: ===============================================================

We want to find employees who badged into our secured room unusually often. 
We have an unordered list of names and access times over a single day. 
Access times are given as three or four-digit numbers using 24-hour time, 
such as "800" or "2250"

Write a function that finds anyone who badged into the room 3 or more times 
in a 1-hour period, and returns each time that they badged in during that period.
 (If there are multiple 1-hour periods where this was true, 
 just return the first one.)

badge_records =[
     ["Paul", 1355],
     ["Jennifer", 1910],
     ["John", 830],
     ["Paul", 1315],
     ["John", 835],
     ["Paul", 1405],
     ["Paul", 1630],
     ["John", 855],
     ["John", 915],
     ["John", 930],
     ["Jennifer", 1335],
     ["Jennifer", 730],
     ["John", 1630],
    ]

Expected output:
John: 830 835 855 915 930
Paul: 1315 1355 1405
```
{% endtab %}

{% tab title="solution_p1 .py" %}
```python
def solve(records):

    emps = dict()   # emp -> [ext_cnt, ent_cnt]
    
    for e, action in records:
        if action == "exit":
            if e not in emps.keys():
                emps[e] = [1,0]
            else:
                emps[e][0] += 1
        else:
            if e not in emps.keys():
                emps[e] = [0,1]
            else:
                emps[e][1] += 1
            
    exit_defaulters, enter_defaulters = [], []
    
    for emp, cnts in emps.items():
        exit_cnt, ent_cnt = cnts
        if exit_cnt < ent_cnt:
            exit_defaulters.append(emp)
        elif ent_cnt < exit_cnt:
            enter_defaulters.append(emp)
    
    print(exit_defaulters)
    print(enter_defaulters)


def test1():
    badge_records = [
        ["Martha", "exit"],
        ["Paul", "enter"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "enter"],
        ["Paul", "enter"],
        ["Curtis", "enter"],
        ["Paul", "exit"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "exit"],
    ]

    solve(badge_records)


def run_tests():
    test1()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}

{% tab title="solution_pt2.py" %}
```python
from collections import defaultdict
def solve(records):
    emps = defaultdict(list)
    res = defaultdict(list)
    
    for e,t in records:
        emps[e].append(t)
        
    for e,ts in emps.items():
        emps[e] = sorted(ts)
        
    # print(emps)
    for e, ts in emps.items():
        #check if emp defaulter at all:
        for i in range(len(ts)-1):
            if ts[i+1]-ts[i] <= 100:
                # defaulter found!
                start_time = ts[i]
                end_time = ts[i]+100
                
                default_times = [start_time]
                j = i+1
                while j<len(ts) and ts[j]<=end_time:
                    default_times.append(ts[j])
                    j += 1
                res[e] = default_times
                break
    
    for e, ts in res.items():
        print(e, end = ': ')  
        for t in ts:
            print(t, end = ' ')
        print('')
    
def test1():
    badge_records =[
     ["Paul", 1355],
     ["Jennifer", 1910],
     ["John", 830],
     ["Paul", 1315],
     ["John", 835],
     ["Paul", 1405],
     ["Paul", 1630],
     ["John", 855],
     ["John", 915],
     ["John", 930],
     ["Jennifer", 1335],
     ["Jennifer", 730],
     ["John", 1630],
    ]
    solve(badge_records)


def run_tests():
    test1()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}
{% endtabs %}

## 4. Merge Intervals | LC-252,253 & LC.56

{% tabs %}
{% tab title="problem.txt" %}
```
# Pt1: ===============================================================

Similar to Meeting Rooms(LeetCode 252, *try 253!)

# Pt2: ===============================================================

Similar to Merge Intervals(LeetCode 56), but the output is different, 
now you are required to output idle time after time intervals merged, 
notice also output 0 - first start time.
```
{% endtab %}

{% tab title="solution_p1 .py" %}
```python
function canSchedule(meetings, start, end) {
  for (const meeting of meetings) {
    if (
      (start >= meeting[0] && start < meeting[1]) ||
      (end > meeting[0] && end <= meeting[1]) ||
      (start < meeting[0] && end > meeting[1])
    ) {
      return false;
    }
  }
  return true;
}
```
{% endtab %}

{% tab title="solution_pt2.py" %}
```python
function spareTime(meetings) {
  if (!meetings || meetings.length === 0) {
    return [];
  }
  meetings = mergeMeetings(meetings);
  const result = [];
  let start = 0;
  for (let i = 0; i < meetings.length; i++) {
    result.push([start, meetings[i][0]]);
    start = meetings[i][1];
  }
  return result;
}
function mergeMeetings(meetings) {
  const result = [];
  meetings.sort((a, b) => a[0] - b[0]);
  let [start, end] = meetings[0];
  for (const meeting of meetings) {
    if (start < meeting[1]) {
      end = Math.max(end, meeting[1]);
    } else {
      result.push(start, end);
      start = meeting[0];
      end = meeting[0];
    }
  }
  return result;
}
```
{% endtab %}
{% endtabs %}

## 5. Course Schedule

{% tabs %}
{% tab title="problem.txt" %}
```
# Pt1: ===============================================================

You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
Sample Input:

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
复制代码Sample Output (pseudocode, in any order):
find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]-baidu 1point3acres
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]-baidu 1point3acres
  [17, 94]: []
  [17, 25]: []
}
Additional test cases:

Sample Input:

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

Sample output:

find_pairs(student_course_pairs_2) =>
{
  [0, 42]: []
  [0, 9]: []
  [9, 42]: []
}


# Pt2: ===============================================================

Students may decide to take different "tracks" or sequences of courses 
in the Computer Science curriculum. 
There may be more than one track that includes the same course, 
but each student follows a single linear track from a "root" node to a "leaf" node. 

In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs, 
and returns the name of all of the courses that the students could be taking 
when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
 ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]



# Pt3: ===============================================================
```
{% endtab %}

{% tab title="solution_p1 .py" %}
```python
from collections import defaultdict


def solve(courses):
    adj = defaultdict(set)

    for sid, c in courses:
        adj[sid].add(c)

    pairs = defaultdict(list)

    for id1, courses1 in adj.items():
        for id2, courses2 in adj.items():
            if id1 != id2 and id1 < id2:
                if id1 > id2:
                    # swap to keep the smaller first
                    id1, courses1, id2, courses2 = id2, courses2, id1, courses1
                intersection_courses = list(set(courses1 & courses2))
                # if len(intersection_courses) > 0:
                # print(f' {id1} - {id2} :: {intersection_courses}')
                pairs[(id1, id2)].append(intersection_courses)

    for k, v in pairs.items():
        print(f"[{k[0]} {k[1]}]: ", end="")
        print(*v, sep=", ")


def test1():
    courses = [
        ["58", "Software Design"],
        ["58", "Linear Algebra"],
        ["94", "Art History"],
        ["94", "Operating Systems"],
        ["17", "Software Design"],
        ["58", "Mechanics"],
        ["58", "Economics"],
        ["17", "Linear Algebra"],
        ["17", "Political Science"],
        ["94", "Economics"],
        ["25", "Economics"],
    ]
    solve(courses)


def test2():
    courses = [
        ["42", "Software Design"],
        ["0", "Advanced Mechanics"],
        ["9", "Art History"],
    ]
    solve(courses)


def run_tests():
    test1()
    test2()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}

{% tab title="solution_pt2.py" %}
```python
n, m = I()
adj = defaultdict(list)

for _ in range(m):
    x, y = I()
    adj[x].append(y)
    adj[y].append(x)

par = [0]*(n+1)
# BFS
Q = deque()
Q.append(1)
par[1] = -1

while Q:
    p = Q.pop()
    
    if p == n:
        break
    
    for x in adj[p]:
        if not par[x]:
            Q.append(x)
            par[x] = p

# Traverse back from n-> 1
if not par[n]:
    print("IMPOSSIBLE")
    return

path = []
curr = n
while curr != -1:
    path.append(curr)
    curr = par[curr]
    
print(len(path))
for p in reversed(path):
    print(p,end = " ")
return 
```
{% endtab %}
{% endtabs %}

## 6. Domain Visit | LC [811](https://leetcode.com/problems/subdomain-visit-count/) , 718

{% tabs %}
{% tab title="problem.txt" %}
```
# Pt1: ===============================================================

cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]

# Pt2: ===============================================================

[LCS]

Longest Continuous Common History: 
Given visiting history of each user, 
find the longest continuous common history between two users. 
(LeetCode 718, dp:LCS)

[
 ["3234.html", "xys.html", "7hsaa.html"], // user1
 ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]
output: ["xys.html", "7hsaa.html"]

# Pt3: ===============================================================

[Ad conversion Rate]


The people who buy ads on our network don't have enough data about how ads are working for
their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page
after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = 
  [
  "3123122444","234111110", "8321125440", "99911063"
  ]

And our ops team provided us with some raw log data from our ad server showing every time a
user clicked on one of our ads:
 ad_clicks = [
  #"IP_Address,Time,Ad_Text",
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]     
The client also sent over the IP addresses of all their users.     
all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]
       
 Write a function to parse this data, determine how many times each ad was clicked,
then return the ad text, that ad's number of clicks, and how many of those ad clicks
were from users who made a purchase.

 Expected output:
 Bought Clicked Ad Text
 1 of 2  2017 Pet Mittens
 0 of 1  The Best Hollywood Coats
 3 of 3  Buy wool coats for your pet
```
{% endtab %}

{% tab title="solution_p1 .py" %}
```python
count = collections.Counter()
for cd in cpdomains:
    n, s = cd.split()
    count[s] += int(n)
    for i in range(len(s)):
        if s[i] == '.':
            count[s[i + 1:]] += int(n)
return ["%d %s" % (count[k], k) for k in count]
```
{% endtab %}

{% tab title="solution_pt2.py" %}
```python
from collections import defaultdict


def solve(history):
    h1, h2 = history
    n,m = len(h1), len(h2)
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    max_cnt = 0
    res = []
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if h1[i-1] == h2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            if max_cnt < dp[i][j]:
                max_cnt = dp[i][j]
                res = h1[i-max_cnt:i]   #WOAHHHHHH
    print(res)

def test1():
    history = [
        ["3234.html", "xys.html", "7hsaa.html"], 
        ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"], 
    ]
    solve(history)
    

def test2():
    courses = [
        [1,2,3,2,1],  # user1
        [3,2,1,4,7]  # user2
    ]
    solve(courses)



def run_tests():
    test1()
    test2()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}

{% tab title="ad_conversion.py" %}
```python
from collections import defaultdict

def solve(completed_purchase_user_ids,ad_clicks,all_user_ips):
    user_ids = set(completed_purchase_user_ids)
    conversion = dict() # txt -> [bought, total_clicks]
    ip_to_user = defaultdict()
    
    for user_ip in all_user_ips:
        uid, ip = user_ip.split(',')
        ip_to_user[ip] = uid
    
    for click in ad_clicks:
        ip, time, txt = click.split(',')
        # print(f'{ip}, {time}, {txt}')
        if txt in conversion:
            conversion[txt][1] += 1
            if ip in ip_to_user.keys() and ip_to_user[ip] in user_ids:
                conversion[txt][0] += 1
        else:
            bought = 0
            if ip in ip_to_user.keys() and ip_to_user[ip] in user_ids:
                bought = 1
            conversion[txt] = [bought,1]
            
    for k,v in conversion.items():
        print(f'{v[0]} of {v[1]}  {k}')
    

def test1():
    completed_purchase_user_ids = ["3123122444", "234111110", "8321125440", "99911063"]
    ad_clicks = [
        # "IP_Address,Time,Ad_Text",
        "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
        "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
        "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
        "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
        "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
        "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
    ]
    all_user_ips = [
        # "User_ID,IP_Address",
        "2339985511,122.121.0.155",
        "234111110,122.121.0.1",
        "3123122444,92.130.6.145",
        "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
        "8321125440,82.1.106.8",
        "99911063,92.130.6.144",
    ]
    solve(completed_purchase_user_ids,ad_clicks,all_user_ips)


def run_tests():
    test1()


if __name__ == "__main__":
    run_tests()
```
{% endtab %}
{% endtabs %}

## 7. Basic Calculator | [LC 224](https://leetcode.com/problems/basic-calculator/)

{% tabs %}
{% tab title="problem.txt" %}
```
# Pt1: ===============================================================

 Calculator without parenthesis, only +, -, non-negative ints

# Pt2: ===============================================================
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```
{% endtab %}

{% tab title="solution_p1 .py" %}
```python
public static int basicCalculator1(String expression){
    int num = 0, sum = 0, sign = 1; // 1 for +, -1 for -
    char[] chars = expression.toCharArray();
    for(int i = 0; i < chars.length; i++){
        char cur = chars[i];
        if(Character.isDigit(cur)) num = num * 10 + Character.getNumericValue(cur);
        else if(cur == '+' || cur == '-'){
            sum += sign * num;
            num = 0;
            sign = (cur == '+') ? 1 : -1;
        }
    }
    if(num != 0) sum += sign * num;
    return sum;
}
```
{% endtab %}

{% tab title="solution_pt2.py" %}
```python
def calculate(self, s: str) -> int:
    num=0
    res=0
    sign=1
    stack=[]
    
    for char in s:
        if char.isdigit():
            num=num*10+int(char)
        elif char in ["-","+"]:
            res=res+num*sign
            num=0
            if char=="-":
                sign=-1
            else:
                sign=1
        elif char=="(":
            stack.append(res)
            stack.append(sign)
            sign=1
            res=0
        elif char==")":
            res+=sign*num
            res*=stack.pop()## process sign
            res+=stack.pop() ##process with old value
            num=0
    
    return res+num*sign
```
{% endtab %}
{% endtabs %}
