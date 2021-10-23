# Maths



## 0. Notes :

### **0.1 Fibonacci:**

* **Zeckendorf’s theorem** states that every positive integer has a **unique representation as a sum of Fibonacci numbers** such that **no two numbers are equal or consecutive Fibonacci numbers**.
  * For example, the number 74 can be represented as the sum 55+13+5+1.
* \*\*Binet’s formula \*\*for calculating **Fibonacci numbers:**

![](../../.gitbook/assets/screenshot-2021-08-13-at-9.32.25-am.png)

### **0.2 Primes & Factors**

![](../../.gitbook/assets/screenshot-2021-09-10-at-2.04.29-pm.png)

![](../../.gitbook/assets/screenshot-2021-09-10-at-2.06.28-pm.png)

![Wilson’s theorem to check whether a number is prime or not](../../.gitbook/assets/screenshot-2021-09-10-at-2.14.35-pm.png)

![Euler’s totient function](../../.gitbook/assets/screenshot-2021-09-10-at-2.10.08-pm.png)

* \*\*Lagrange’s theorem \*\*states that every positive integer can be represented as a sum of four squares, i.e., \*\* $$N = a^2 + b^2 + c^2 + d^2$$ \*\*
  * For example, the number 123 can be represented as the sum $$123 = 8^2 + 5^2 + 5^2 + 3^3$$ 8

### **0.3 Euclidean GCD**

```python
def gcd(a,b):
    if (b == 0):              # Everything divides 0
         return a
    return gcd(b, a%b)
```

* **Sieve of Eratosthenes**
  * **COMPLEXITY**:

![TC of Sieve algo](../../.gitbook/assets/screenshot-2021-09-10-at-2.08.37-pm.png)

{% tabs %}
{% tab title="Sieve_Algo.py" %}
```cpp
if n <= 1:
    return 0

primes = [True for _ in range(n+1)]
primes[0] = False

primes[1] = False
for i in range(2,int(sqrt(n+1))+1):
    if primes[i]:
        for j in range(i*i,n+1,i):
            primes[j] = False

return sum(x for x in primes if x)
```
{% endtab %}
{% endtabs %}

### 0.4 Combinatorics

* \*\*Catalan numbers \*\*
  * C(n) equals the number of\*\* valid parenthesis expressions \*\*that consist of n left parentheses and n right parentheses.
  * Catalan numbers are also related to\*\* trees\*\*:
    * there are **C(n)** **binary trees** of **n nodes**
    * there are **C(n−1)** \*\*rooted trees \*\*of **n nodes**

![](../../.gitbook/assets/screenshot-2021-09-10-at-2.22.05-pm.png)

* **Derangements**
  * \==> permutations where no element remains in its original place
    * number of derangements of elements {1, 2, . . . , n}, i.e., .
    * For example, when n = 3, there are two derangements: (2, 3, 1) and (3, 1, 2)

![formula for Derangements](../../.gitbook/assets/screenshot-2021-09-10-at-2.25.10-pm.png)

### 0.5 Modular Exponentiation :

```cpp
int my_pow(int x,int n,int M){    //get (x^n % M)
    if(n==0) return 1;
    else if(n%2 == 0) return my_pow((x*x)%M,n/2,M);
    else return (x*my_pow((x*x)%M,(n-1)/2,M))%M;
}
// or in python: 
math.pow(x,n,M)
```

###

## 1. Problems: Maths

* [x] LC [326.Power of Three](https://leetcode.com/problems/power-of-three/)
* [x] CSES: [Two Sets](https://cses.fi/problemset/task/1092) | four consecutive numbers can be divided into 2 sets of equal sums | [link to solution approach](https://www.reddit.com/r/learnprogramming/comments/n9ql5a/cses\_problem\_two\_sets/) ⭐️
* [x] CSES: [Coin Piles](https://cses.fi/problemset/task/1754) | [Solution Approach](https://discuss.codechef.com/t/coin-piles-problem-from-cses/28647/3)
* [x] CSES: [Gray Code](https://cses.fi/problemset/task/2205) | [Solution](https://www.geeksforgeeks.org/generate-n-bit-gray-codes/)
* [x] CSES: [Missing Coin Sum](https://cses.fi/problemset/result/2583670/) | [Approach](https://discuss.codechef.com/t/cses-missing-coin-sum/84039/2) ✅
  * \*\*KYA SEEKHA: \*\*At any index **i** in a sorted array **a**, currSum represents `sum(a[ 0...i ])`.We can form every possible sum from `1...currSum`, when we are at index i
* [x] LC: [166.Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/submissions/) ✅| recurring decimal => reminder will repeat | [Approach](https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/180004/Python-4-lines-\(32ms-beats-100\)-with-explanation)
* [x] LC [1980.Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) | **Cantor's Diagonalization** | [Video@veritassium](https://www.youtube.com/watch?v=OxGsU8oIWjY)
  * \*\*Some infinities(Uncountable Infinity- **party bus people**) are BIGGER than other infinities(Countable Infinities- \*\*hotel rooms 1...inf)
  * Just watch the video; so fucking mind-blowing
* [x] LC [1363.Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/) ✅| fucking amazing question & elegant solution 🍪🍪🍪
* [x] [**31. Next Permutation**](https://leetcode.com/problems/next-permutation/)\*\* | ✅| A must | \*\*interview mei aayega toh bina algo jaane, nhi kar paoge
* [ ] LC [166. Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | @google

{% tabs %}
{% tab title="326" %}
```python
import math

def isPowerOfThree(self, n: int) -> bool:
    if n <= 0: return False
    return math.log10(n) / math.log10(3) % 1 == 0
```
{% endtab %}

{% tab title="1363" %}
```python
d1 = sorted([i for i in d if i%3 ==1])
d2 = sorted([i for i in d if i%3 ==2])
d3 = [i for i in d if i%3 ==0]
if sum(d) % 3 == 1:
    if len(d1) != 0:
        res = d1[1:] + d2 + d3
    else:
        res = d2[2:]+ d3
elif sum(d) % 3 == 2:
    if len(d2) != 0:
        res = d1 + d2[1:] + d3
    else:
        res = d1[2:] +d3
else:
    res = d
res.sort(reverse = True)
if not res: return ''
return str(int(''.join([str(i) for i in res])))
```
{% endtab %}

{% tab title="31✅" %}
**ALGO:**

* To find next permutations, we'll start from the end
* First we'll find the first non-increasing element starting from the end.
* there will be two cases:
  * **CASE#1: **Our i becomes zero (This will happen if the given array is sorted decreasingly).&#x20;
    * In this case, we'll simply reverse the sequence and will return
  * **CASE#2: **If it's not zero then we'll find the first number grater then nums\[i-1] starting from end
    * And We'll swap these two numbers
    * Then We'll reverse a sequence starting from i to end



```python
def nextPermutation(self, nums: List[int]) -> None:
    # To find next permutations, we'll start from the end
    i = j = len(nums)-1
    # First we'll find the first non-increasing element starting from the end
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    # After completion of the first loop, there will be two cases
    # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). 
    # In this case, we'll simply reverse the sequence and will return 
    if i == 0:
        nums.reverse()
        return 
    # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
    while nums[j] <= nums[i-1]:
        j -= 1
    # Now out pointer is pointing at two different positions
    # i. first non-assending number from end
    # j. first number greater than nums[i-1]

    # We'll swap these two numbers
    nums[i-1], nums[j] = nums[j], nums[i-1]

    # We'll reverse a sequence strating from i to end
    nums[i:]= nums[len(nums)-1:i-1:-1]
    # We don't need to return anything as we've modified nums in-place
```
{% endtab %}
{% endtabs %}

## 2. Problems: Combinatorics

* [ ] AtCoder: [Cumulative Sum](https://atcoder.jp/contests/abc208/tasks/abc208\_f) | [Editorial](https://atcoder.jp/contests/abc208/editorial/2219)

## 3. Problems: Chess

* [x] CSES: [Two Knights](https://cses.fi/problemset/task/1072) | approach: [here](https://discuss.codechef.com/t/cses-two-knights-problem-help-needed/69448/5) & [here](https://math.stackexchange.com/questions/3266257/number-of-ways-two-knights-can-be-placed-such-that-they-dont-attack)
* [ ] [https://codeforces.com/blog/entry/78943](https://codeforces.com/blog/entry/78943)

{% hint style="info" %}
If two knight attack each other then they will be in 2\*\_3 rectangle or 3\*\_2 rectangle.

* number of 2\*3 rects = #rows\*#cols = (n-1)\*(n-2)

So the number of ways of placing them is (n-1)_(n-2)+(n-2)_(n-1). Also in each rectangle no ways of placing the knight is 2. So total ways of placing knight so that they attack each other will be 2\_2\_(n-1)_(n-2). So the number of ways such that knight do not attack each other will be n\_n_(n\_n-1)/2 — 4\_(n-1)\_(n-2)
{% endhint %}



## 4. Problemsets

* Leetcode tag=**Maths :** [https://leetcode.com/problemset/all/?topicSlugs=math](https://leetcode.com/problemset/all/?topicSlugs=math)
* Hackerrank: [https://www.hackerrank.com/domains/mathematics?filters%5Bsubdomains%5D%5B%5D=geometry](https://www.hackerrank.com/domains/mathematics?filters%5Bsubdomains%5D%5B%5D=geometry)
* Codeforces Tag = **combinatorics/probability**: [https://codeforces.com/problemset?tags=probabilities](https://codeforces.com/problemset?tags=probabilities)
* Codeforces tag = \*\*number-theory: \*\* [https://codeforces.com/problemset?tags=number+theory](https://codeforces.com/problemset?tags=number+theory)

## 5. Resources

* Kartik Arora's Playlist :[ Number Theory](https://www.youtube.com/watch?v=2NN5j1iF2ko\&list=PLb3g\_Z8nEv1i6NHntG5l2fPKuVu853EYy\&ab\_channel=KartikArora)
* \*\*Topcoder \*\*:
  * [**MATHEMATICS FOR TOPCODERS**](https://www.topcoder.com/thrive/articles/Mathematics%20for%20Topcoders)
  * [**BASICS OF COMBINATORICS**](https://www.topcoder.com/thrive/articles/Basics%20of%20Combinatorics)
