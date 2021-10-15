# Bitwise

### **ANY PROBLEM IN THE WORLD CAN BE SOLVED BY BITSET(i.e. checking on all possible solutions)🟢🟢🟢**

## **Notes:**

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

| What                                                                  | How                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Left Shift ( << )                                                     | <p><code>1 &#x3C;&#x3C; i = pow(2,i) : </code><strong><code>general_use</code></strong></p><p><strong><code>n&#x3C;&#x3C;k </code></strong>is equivalent to <strong>multiplying</strong> n with <span class="math">2^k </span> </p>                                                                                                                                                                                                                                                                                                |
| Right Shift ( >> )                                                    | <p><code>i >> 1 : </code><strong><code>general_use</code></strong></p><p>16 >> 4 = 1</p><p><strong><code>n>>k </code></strong>is equivalent to <strong>dividing</strong> n with <span class="math">2^k </span> </p>                                                                                                                                                                                                                                                                                                                |
| **Implementation: C**heck if the i-th bit is set                      | **`return x and (1<<i)`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **TURN OFF ** the i-th bit in x                                       | **`x = x^(1<<i) `**  # xor turns that bit off                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **TURN ON **the i-th bit in x                                         | **`x = x\|(1<<i)`**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Implementation: **generate all the possible subsets                 | <p><code>for i in range(0, 1&#x3C;&#x3C;n):</code><br><code>         sub = []</code></p><p><code>         for j in range(0,n):</code></p><p><code>              if i </code><strong><code>&#x26;</code></strong><code>(1&#x3C;&#x3C;j):</code></p><p><code>                   sub.append(a[j])</code></p><p><code>         superset += sub</code></p>                                                                                                                                                                              |
| `(x-1)`                                                               | <p>flips all the bits to the right of rightmost 1 in x and also including the rightmost 1</p><p>x = 4      = (100)<br>x - 1 = 3 = (011)</p>                                                                                                                                                                                                                                                                                                                                                                                        |
| **Implementation: **check if a given number is a power of 2 ?         | <p><strong><code>return (x and !(x and (x-1)))</code></strong><br><code>//x will check if x == 0 and !(x and (x-1)) will check if power of two </code></p>                                                                                                                                                                                                                                                                                                                                                                         |
| **Implementation: **Count number of 1's in binary representation of x | <p><strong><code>while(x):</code></strong></p><p><strong><code>      x = x &#x26; (x-1)</code></strong></p><p><strong><code>      cnt += 1</code></strong></p><p><strong>Complexity:</strong> O(K), where K is the number of ones present in the binary form of the given number</p>                                                                                                                                                                                                                                               |
| **Implementation: **Get the rightmost 1 in binary representation of x | <p><strong><code>x ^ ( x &#x26; (x-1))</code></strong></p><p><strong>How: </strong>(x &#x26; (x - 1)) will have all the bits equal to the x except for the rightmost 1 in x. So if we do bitwise XOR of x and (x &#x26; (x-1)), it will simply return the rightmost 1.</p><p>x = 10                                               = (1010)<br>x &#x26; (x-1) = (1010) &#x26; (1001)          = (1000)<br>x ^ (x &#x26; (x-1)) = (1010) ^ (1000)   = (0010)</p>                                                                     |
| **Implementation: **Highest power of 2 less than or equal to given N  | <ul><li>using left shift operator to find all powers of 2 starting from 1.</li><li><p>For every power check if it is smaller than or equal to n or not</p><p><code></code><br><code>for i in range(8*sys.getsizeof(n)):</code></p><p><code>     curr</code> <code>=</code> <code>1</code> <code>&#x3C;&#x3C; i</code></p><p><code>     if</code> <code>curr >= n: return curr</code></p></li><li><p>Another approach using log:</p><p><code>p = int(math.log(n, 2))    </code><br><code>return int(pow(2, p))</code></p></li></ul> |
| **XOR Trick: **swap w/o extra variable                                | <p><code>a,b // integers to be swapped</code></p><p><code>a = a^b   // a now contains a^b</code></p><p><code>b = a^b   // b now contains a</code></p><p><code>a = a^b   // a now contains b     </code><strong><code> #SWAPPED</code></strong> </p>                                                                                                                                                                                                                                                                                |
| Other Helpful things                                                  | <ul><li><code>(a|b) = (a+b) - (a&#x26;b)</code></li><li><code>(a+b) = (a^b) + 2*(a&#x26;b)</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                        |

****

## **Bitmasking**:

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

### DP with Bitmasking:

* check #DP section





## Problems: Bitwise

* [ ] Missing Number: [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)​
* [ ] Bitwise ORs of Subarrays: [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] XOR Queries of a Subarray: [https://leetcode.com/problems/xor-queries-of-a-subarray/](https://leetcode.com/problems/xor-queries-of-a-subarray/)
* [ ] Minimum Flips to Make a OR b Equal to c: [https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
* [ ] Count Triplets That Can Form Two Arrays of Equal XOR: [https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
* [ ] Bitwise AND of Numbers Range: [https://leetcode.com/problems/bitwise-and-of-numbers-range/](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
* [ ] Decode XORed Permutation: [https://leetcode.com/problems/decode-xored-permutation/](https://leetcode.com/problems/decode-xored-permutation/)
* [x] CSES: [Apple Division](https://cses.fi/problemset/result/2572485/)
* [x] LC: [29.Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)



## ProblemSet(to be picked from here)

* [ ] CommonProblems:  [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [ ] LC: [https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation](https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation)
* [ ] CF: [https://codeforces.com/problemset?order=BY_SOLVED_DESC\&tags=bitmasks%2C1200-1500](https://codeforces.com/problemset?order=BY_SOLVED_DESC\&tags=bitmasks%2C1200-1500)











## Resources:

* [https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)
* [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)
