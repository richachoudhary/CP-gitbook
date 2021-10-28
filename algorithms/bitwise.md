# Bitwise

### 🌟**ANY PROBLEM IN THE WORLD CAN BE SOLVED BY BITSET(i.e. checking on all possible solutions)🟢🟢🟢**

### \*\*\*\*

### \*\* \*\*<mark style="color:green;">**1<\<i **</mark>**i>>1**

### <mark style="color:orange;">चोंच</mark> wali taraf <mark style="color:orange;">1</mark> rahega

(because चोंच एक hi hoti hai na)

### <mark style="color:yellow;">मुँह खुला</mark> wali taraf <mark style="color:yellow;">i</mark> rahega

***

## **0.Notes:**

```python
# int to binary
>>> n = 19
>>> bin(n)                # '0b10011'
# binary to int
>>> int('11111111', 2)    # 255

# binary to int (base 32)
>>> bit_str = '{0:032b}'.format(5)    # 00000000000000000000000000000101
# binary to int (base 16)
>>> bit_str = '{0:016b}'.format(5)    # 0000000000000101


>>> n.bit_count()
3
>>> (-n).bit_count()
3
```

| What                                                                      | How                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Left Shift ( << )                                                         | <p><code>1 &#x3C;&#x3C; i = pow(2,i) : </code><strong><code>general_use</code></strong></p><p><strong><code>n&#x3C;&#x3C;k </code></strong>is equivalent to <strong>multiplying</strong> n with <span class="math">2^k</span></p>                                                                                                                                                                                                                                                                             |
| Right Shift ( >> )                                                        | <p><code>i >> 1 : </code><strong><code>general_use</code></strong></p><p>16 >> 4 = 1</p><p><strong><code>n>>k </code></strong>is equivalent to <strong>dividing</strong> n with <span class="math">2^k</span></p>                                                                                                                                                                                                                                                                                             |
| **Implementation: C**heck if the i-th bit is set                          | **`return x and (1<<i)`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **GET** i-th bit of x                                                     | **`return (x>>i)&1`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \*\*CLEAR/TURN OFF \*\* the i-th bit in x                                 | **`x = x^(1<<i) `**# xor turns that bit off                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \*\*SET/TURN ON \*\*the i-th bit in x                                     | **`x = x\|(1<<i)`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **TOGGLE** the i-th bit in x                                              | **x = `x^(1<<i)`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \*\*Implementation: \*\*generate all the possible subsets                 | <p><code>for i in range(0, 1&#x3C;&#x3C;n):</code><br><code>sub = []</code></p><p><code>for j in range(0,n):</code></p><p><code>if i </code><strong><code>&#x26;</code></strong><code>(1&#x3C;&#x3C;j):</code></p><p><code>sub.append(a[j])</code></p><p><code>superset += sub</code></p>                                                                                                                                                                                                                     |
| `(x-1)`                                                                   | <p>flips all the bits to the right of rightmost 1 in x and also including the rightmost 1</p><p>x = 4 = (100)<br>x - 1 = 3 = (011)</p>                                                                                                                                                                                                                                                                                                                                                                        |
| \*\*Implementation: \*\*check if a given number is a power of 2 ?         | <p><strong><code>return (x and !(x and (x-1)))</code></strong><br><code>//x will check if x == 0 and !(x and (x-1)) will check if power of two</code></p>                                                                                                                                                                                                                                                                                                                                                     |
| \*\*Implementation: \*\*Count number of 1's in binary representation of x | <p><strong><code>while(x):</code></strong></p><p><strong><code>x = x &#x26; (x-1)</code></strong></p><p><strong><code>cnt += 1</code></strong></p><p><strong>Complexity:</strong> O(K), where K is the number of ones present in the binary form of the given number</p>                                                                                                                                                                                                                                      |
| \*\*Implementation: \*\*Get the rightmost 1 in binary representation of x | <p><strong><code>return x ^ ( x &#x26; (x-1))</code></strong></p><p><strong>How: </strong>(x &#x26; (x - 1)) will have all the bits equal to the x except for the rightmost 1 in x. So if we do bitwise XOR of x and (x &#x26; (x-1)), it will simply return the rightmost 1.</p><p>x = 10 = (1010)<br>x &#x26; (x-1) = (1010) &#x26; (1001) = (1000)<br>x ^ (x &#x26; (x-1)) = (1010) ^ (1000) = (0010)</p>                                                                                                  |
| \*\*Implementation: \*\*Highest power of 2 less than or equal to given N  | <ul><li>using left shift operator to find all powers of 2 starting from 1.</li><li><p>For every power check if it is smaller than or equal to n or not</p><p><br><code>for i in range( 8 *sys.getsizeof ( n ) ):</code></p><p><code>curr</code> <code>=</code> <code>1</code> <code>&#x3C;&#x3C; i</code></p><p><code>if</code> <code>curr >= n: return curr</code></p></li><li><p>Another approach using log:</p><p><code>p = int(math.log(n, 2))</code><br><code>return int(pow(2, p))</code></p></li></ul> |
| \*\*XOR Trick: \*\*swap w/o extra variable                                | <p><code>a,b // integers to be swapped</code></p><p><code>a = a^b // a now contains a^b</code></p><p><code>b = a^b // b now contains a</code></p><p><code>a = a^b // a now contains b </code><strong><code>#SWAPPED</code></strong></p>                                                                                                                                                                                                                                                                       |
| Other Useful things                                                       | <ul><li></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

***

## \*\*\*\*

## 1. Problems: Bitwise

* [ ] LC : [289.Game of Life](https://leetcode.com/problems/game-of-life/)
* [ ] Missing Number: [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)​
* [ ] Bitwise ORs of Subarrays: [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] XOR Queries of a Subarray: [https://leetcode.com/problems/xor-queries-of-a-subarray/](https://leetcode.com/problems/xor-queries-of-a-subarray/)
* [ ] Minimum Flips to Make a OR b Equal to c: [https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
* [ ] Count Triplets That Can Form Two Arrays of Equal XOR: [https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
* [ ] Bitwise AND of Numbers Range: [https://leetcode.com/problems/bitwise-and-of-numbers-range/](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
* [ ] Decode XORed Permutation: [https://leetcode.com/problems/decode-xored-permutation/](https://leetcode.com/problems/decode-xored-permutation/)
* [x] LC: [29.Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)
* [x] LC 421. [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | <mark style="color:orange;">`standardQ`</mark> | **@google | must\_do✅**
* [ ] LC 318. [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) | **@google**

{% tabs %}
{% tab title="289." %}
**1. Appr#1 : SC: O(N\*M)**

so damn easy

```python
def gameOfLife(self, A: List[List[int]]) -> None:
    n,m = len(A), len(A[0])
    dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

    def count_neighoubrs(x,y):
        count = 0
        for dx,dy in dirs:
            nx, ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and A[nx][ny] == 1:
                count += 1
        return count

    res = [[0 for _ in range(m)] for _ in range(n)]    # extra space

    for i in range(n):
        for j in range(m):
            res[i][j] = A[i][j]
            nei = count_neighoubrs(i,j)
            if A[i][j] == 0:  
                if nei == 3:     # .4 dead
                    res[i][j] = 1
            elif A[i][j] == 1:
                if nei < 2 or nei > 3:
                    res[i][j] = 0
    A[::] = res
```

**2. FOLLOW\_UP: #1: Do in O(1) Space ---> **<mark style="color:red;">**bitwise**</mark>

\*\*IDEA: \*\*

* Traverse top-left to bottom-right & store the prev\_val in `0-th` bit & new val in `1st` bit.
* Iterate once again & assign cell values to `0-th` bit only

```python
def gameOfLife(self, A: List[List[int]]) -> None:
    n,m = len(A), len(A[0])
    dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

    def count_neighoubrs(x,y):
        count = 0
        for dx,dy in dirs:
            nx, ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and get_ith_bit(0,nx,ny) == 1:
                count += 1
        return count

    def set_ith_bit(i,x,y):
        A[x][y] = A[x][y]|(1<<i)

    def get_ith_bit(i,x,y):
        return (A[x][y]>>i)&1

    for i in range(n):
        for j in range(m):
            nei = count_neighoubrs(i,j)
            prev_val = get_ith_bit(0,i,j)
            if prev_val == 1 and nei == 2 or nei == 3:
                set_ith_bit(1,i,j)

    for i in range(n):
        for j in range(m):
            A[i][j] = get_ith_bit(1,i,j)
```

**3. FOLLOW\_UP#2: infinite board**

> In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

* When the board is infinite, we can't present the board using 2d array, because the number of rows and columns maybe too big.
* To mimic the infinite board follow up question, I add a new method <mark style="color:orange;">`gameOfLifeInfinite`</mark>. And in `gameOfLife`, I've just converted the **board(m, n)** into **infinite board** by storing **live cells** into the <mark style="color:orange;">set</mark>, and the row bound **m**, column bound **n** as well in case we want to limit the boundary.
* The output of `gameOfLifeInfinite` is the set of **live cells** after processing.

```python
class Solution:
    def gameOfLifeInfinite(self, live: set, m: int, n: int) -> set:
        # liveNeighborsCnt[(r, c)] is the number of live neighbors around cell (r, c)
        liveNeighborsCnt = defaultdict(int)  
        for r, c in live:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == m or nc < 0 or nc == n: continue  # Trim cells which have position out of the board 
                    liveNeighborsCnt[(nr, nc)] += 1

        ans = set()
        for (r, c), cnt in liveNeighborsCnt.items():
            if cnt == 3 or cnt == 2 and (r, c) in live:
                ans.add((r, c))
        return ans

    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        liveInput = set((r, c) for r in range(m) for c in range(n) if board[r][c] == 1)
        liveOutput = self.gameOfLifeInfinite(liveInput, m, n)
        for r in range(m):
            for c in range(n):
                board[r][c] = 1 if (r, c) in liveOutput else 0
```

Complexity for `gameOfLifeInfinite`:

* Time: `O(K)`, where `K` is number of live cells.
* Space: `O(K)`
{% endtab %}

{% tab title="421✅" %}
**Videos:**

* To understand logic: [this](https://www.youtube.com/watch?v=I7sUjln2Fjw\&ab\_channel=HellgeekArena)
* To understand code: [this](https://www.youtube.com/watch?v=jCu-Pd0IjIA\&ab\_channel=CodingNinjas)

#### Approach:

* O(N\*2) is trivial; so dont bother
* Greedy Approach: **bitwise+Trie**: `O(32*N) `✅
  * 1 Build Bitwise tree with array
  * 2 for each ele in arr: greedily traverse the trie & get max possible xor value with it

```python
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, val):
        curr = self.root
        
        for i in range(31, -1, -1):
            bit = (val>>i)&1
            
            if bit == 0:
                if not curr.left:
                    curr.left = TrieNode()
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TrieNode()
                curr = curr.right

    def max_xor(self, A):
        max_xor_val = 0
        
        for i in range(len(A)):
            curr = self.root
            val = A[i]
            curr_xor = 0
            
            for j in range(31, -1, -1):
                bit = (val>>j)&1
                
                if bit == 0:
                    if curr.right:
                        curr_xor += 2**j
                        curr = curr.right
                    else:
                        curr = curr.left
                else:
                    if curr.left:
                        curr_xor += 2**j
                        curr = curr.left
                    else:
                        curr = curr.right
                        
            max_xor_val = max(max_xor_val, curr_xor)
            
        return max_xor_val
        
class Solution:
    def findMaximumXOR(self, A):
        t = Trie()
        for x in A:
            t.insert(x)
        return t.max_xor(A)
    

# TC: O(32*N) ================================================== 
    
    
```
{% endtab %}
{% endtabs %}

## **2. Bitmasking**:

```python
def display(SUBSET):        #prints the actual numbers in given SUBSET
    for bit_no in range(0,10):
       if SUBSET and (1<<bit_no):
           print(bit_no + 1)

def add(SUBSET,x):
   SUBSET = SUBSET ^ (1<<(x-1))   # alters the (x-1)th bit
def remove(SUBSET,x):
   SUBSET = SUBSET ^ (1<<(x-1))   # alters the (x-1)th bit : same thing works here too

SUBSET = 15        # 15 is the BITMASK a subset {1,2,3,4} from a set of {1,10}
display(SUBSET)
add(SUBSET,2)
remove(SUBSET,5)
```

## 3. DP with Bitmasking:

* check #DP section

## ProblemSet

* [ ] CommonProblems: [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [ ] LC: [https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation](https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation)
* [ ] CF: [https://codeforces.com/problemset?order=BY\_SOLVED\_DESC\&tags=bitmasks%2C1200-1500](https://codeforces.com/problemset?order=BY\_SOLVED\_DESC\&tags=bitmasks%2C1200-1500)

## Resources:

* [https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)
* [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)
