# Bitwise

## **Notes:**

```python
>>> n = 19
>>> bin(n)
'0b10011'
>>> n.bit_count()
3
>>> (-n).bit_count()
3
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">What</th>
      <th style="text-align:left">How</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">Left Shift ( &lt;&lt; )</td>
      <td style="text-align:left">
        <p><code>1 &lt;&lt; n = pow(2,n)</code>
        </p>
        <p>is equivalent to <b>multiplying</b> the bit pattern with</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Right Shift ( &gt;&gt; )</td>
      <td style="text-align:left">
        <p><code>n &gt;&gt; 1</code>
        </p>
        <p>16 &gt;&gt; 4 = 1</p>
        <p>is equivalent to <b>dividing</b> the bit pattern with</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: C</b>heck if the i-th bit is set</td>
      <td style="text-align:left"><b><code>return x and (1&lt;&lt;i)</code></b>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>generate all the possible subsets</td>
      <td style="text-align:left">
        <p><code>for i in range(0, 1&lt;&lt;n):<br />         sub = []</code>
        </p>
        <p><code>         for n in range(0,n):</code>
        </p>
        <p><code>              if i and (1&lt;&lt;j):</code>
        </p>
        <p><code>                   sub.append(a[j])</code>
        </p>
        <p><code>         superset += sub</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>(x-1)</code>
      </td>
      <td style="text-align:left">
        <p>flips all the bits to the right of rightmost 1 in x and also including
          the rightmost 1</p>
        <p>x = 4 = (100)
          <br />x - 1 = 3 = (011)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>check if a given number is a power of 2 ?</td>
      <td
      style="text-align:left"><b><code>return (x and !(x and (x-1)))</code></b><code><br />//x will check if x == 0 and !(x and (x-1)) will check if power of two </code>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>Count number of 1&apos;s in binary representation
        of x</td>
      <td style="text-align:left">
        <p><b><code>while(x):</code></b>
        </p>
        <p><b><code>      x = x and (x-1)</code></b>
        </p>
        <p><b><code>      cnt += 1</code></b>
        </p>
        <p><b>Complexity:</b> O(K), where K is the number of ones present in the binary
          form of the given number</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>Get the rightmost 1 in binary representation of
        x</td>
      <td style="text-align:left">
        <p><b><code>x ^ ( x &amp; (x-1))</code></b>
        </p>
        <p><b>How: </b>(x &amp; (x - 1)) will have all the bits equal to the x except
          for the rightmost 1 in x. So if we do bitwise XOR of x and (x &amp; (x-1)),
          it will simply return the rightmost 1.</p>
        <p>x = 10 = (1010)
          <br />x &amp; (x-1) = (1010) &amp; (1001) = (1000)
          <br />x ^ (x &amp; (x-1)) = (1010) ^ (1000) = (0010)</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>Set N-th bit in x</td>
      <td style="text-align:left"><b><code>x | (1 &lt;&lt; n)</code></b>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Implementation: </b>Highest power of 2 less than or equal to given
        N</td>
      <td style="text-align:left">
        <ul>
          <li>using left shift operator to find all powers of 2 starting from 1.</li>
          <li>
            <p>For every power check if it is smaller than or equal to n or not</p>
            <p><code><br />for i in range(8*sys.getsizeof(n)):</code>
            </p>
            <p><code>     curr</code>  <code>=</code>  <code>1</code>  <code>&lt;&lt; i</code>
            </p>
            <p><code>     if</code>  <code>curr &gt;= n: return curr</code>
            </p>
          </li>
          <li>
            <p>Another approach using log:</p>
            <p><code>p = int(math.log(n, 2))    <br />return int(pow(2, p))</code>
            </p>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>XOR Trick: </b>swap w/o extra variable</td>
      <td style="text-align:left">
        <p><code>a,b // integers to be swapped</code>
        </p>
        <p><code>a = a^b   // a now contains a^b</code>
        </p>
        <p><code>b = a^b   // b now contains a</code>
        </p>
        <p><code>a = a^b   // a now contains b     </code><b><code> #SWAPPED</code></b> 
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Other Helpful things</td>
      <td style="text-align:left">
        <ul>
          <li><code>(a|b) = (a+b) - (a&amp;b)</code>
          </li>
          <li><code>(a+b) = (a^b) + 2*(a&amp;b)</code>
          </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

* **Bitmasking**:

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







## Problems: Bitwise

* [ ] Missing Number: [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)​
* [ ] Bitwise ORs of Subarrays: [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] XOR Queries of a Subarray: [https://leetcode.com/problems/xor-queries-of-a-subarray/](https://leetcode.com/problems/xor-queries-of-a-subarray/)
* [ ] Minimum Flips to Make a OR b Equal to c: [https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
* [ ] Count Triplets That Can Form Two Arrays of Equal XOR: [https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
* [ ] Bitwise AND of Numbers Range: [https://leetcode.com/problems/bitwise-and-of-numbers-range/](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
* [ ] Decode XORed Permutation: [https://leetcode.com/problems/decode-xored-permutation/](https://leetcode.com/problems/decode-xored-permutation/)
* [x] CSES: [Apple Division](https://cses.fi/problemset/result/2572485/)



## ProblemSet\(to be picked from here\)

* [ ] CommonProblems:  [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [ ] LC: [https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation](https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation)
* [ ] CF: [https://codeforces.com/problemset?order=BY\_SOLVED\_DESC&tags=bitmasks%2C1200-1500](https://codeforces.com/problemset?order=BY_SOLVED_DESC&tags=bitmasks%2C1200-1500)











## Resources:

* [https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)
* [https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate](https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate)
* [https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)

