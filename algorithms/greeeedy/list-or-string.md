# List | String

## 5. List & String

* [x] [18. 4Sum](https://leetcode.com/problems/4sum/) - generalized for **Ksum 📌**
* [x] [1021.Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
* [x] [443.String Compression](https://leetcode.com/problems/string-compression/)
* [ ] [1520.Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) 🍪🍪🍪
* [x] LC: [8.String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
* [x] CSES: [Palindrome Reorder](https://cses.fi/problemset/task/1755)
* [x] TYPE: Count # Inversions✅
  * [x] CSES: [Collecting Numbers](https://cses.fi/problemset/task/2216) | [Approach](https://discuss.codechef.com/t/cses-collecting-numbers/83775)
  * [x] CSES: [Collecting Numbers II](https://cses.fi/problemset/task/2217) | [Video](https://www.youtube.com/watch?v=LEL3HW4dQew\&ab\_channel=ARSLONGAVITABREVIS) 🐽
* [x] CSES: [Subarray Sum 1](https://cses.fi/problemset/task/1660/) | only "prefix sum"
* [x] CSES: [Subarray Sum 2](https://cses.fi/problemset/task/1661) | neg numbers | prefix sum **+** map
* [x] CSES: [Subarray Divisibility](https://cses.fi/problemset/result/2648945/) | ✅
* [x] LC 44: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
* [x] LC [163. Missing Ranges](https://leetfree.com/problems/missing-ranges)
* [x] LC [179.Largest Number](https://leetcode.com/problems/largest-number/) 🐽
* [x] LC [41.First Missing Positive](https://leetcode.com/problems/first-missing-positive/) ✅🍪🍪🍪
* [x] LC [14.Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) ✅| kaafi clever | longest common prefix
* [x] LC [334.Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | **O(N)**
* [x] LC [68. Text Justification](https://leetcode.com/problems/text-justification/) 💪🔴
  * Asked in Coinbase \*\*Karat Test \*\*| multiple times
  * so many corner cases; impossible to solve in interview
  * Built upon \[EASY] [1592.Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) ✅💪

{% tabs %}
{% tab title="18.Ksum" %}
**IDEA/STEPS:**&#x20;

* recursively call kSum function from every j:\[i+1,N] & new\_k = k-1
* when k == 2: apply two\_sum algo
* pay attention how you maintain & append prev call's values to final result

```python
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

    def k_sum(nums, k, target, arr, start_idx):
        if k == 2:
            two_sum(nums, arr, k, start_idx, target)
            return
        for i in range(start_idx, len(nums) - k + 1):
            if i > start_idx and nums[i] == nums[i - 1]:
                continue
            k_sum(nums, k - 1, target - nums[i], arr + [nums[i]], i + 1)

    def two_sum(nums, arr, k, start_idx, target):
        left = start_idx
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                res.append(arr + [nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # skip same element to avoid duplicate quadruplets
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # skip same element to avoid duplicate quadruplets
            elif total < target:
                left += 1
            else:
                right -= 1

    nums.sort()
    res = []
    k_sum(nums, 4, target, [], 0)
    return res

'''
Time: O(NlogN + N^(k-1)), where k >= 2, N is number of elements in the array nums.
Extra space (Without count output as space): O(N)
Video: https://www.youtube.com/watch?v=-vu9GpZfqLY&ab_channel=CodeAndCoffee
'''    
```
{% endtab %}

{% tab title="Collecting Numbers✅" %}
```python
# 1. ==================== LIS doesnt work here: WA
tails = []
LIS = [1]*n

for i,x in enumerate(A):
    idx = bisect.bisect_left(tails,x)
    if idx == len(tails):
        tails.append(x)
        if len(tails) > 1:
            LIS[i] = LIS[idx-1]+1
    else:
        tails[idx] = x
        if idx > 0 and LIS[idx -1] == LIS[i]:
            LIS[i] = LIS[idx-1]+1
        else:
            LIS[i] = LIS[idx]
print(sum(x for x in LIS if x==1))

# 2. ============== Count inversions (as numbers are in 1...n)

s = set()
cnt = 0
for x in A:
    if x-1 not in s:
        cnt += 1
    s.add(x)

print(cnt)

'''
VIDEO: https://www.youtube.com/watch?v=lhhHCZYoJvs&ab_channel=ARSLONGAVITABREVIS
'''
```
{% endtab %}

{% tab title="Subarray Sum 2" %}
```python
I = lambda : map(int, input().split())
n,x = I()

A = list(I())

d = dict()
d[0] = 1
cnt = 0
curr = 0

for e in A:
    curr += e
    if curr - x in d:
        cnt += d[curr-x]

    if curr in d:
        d[curr] += 1
    else:
        d[curr] = 1
print(cnt)
```
{% endtab %}

{% tab title="Subarray Divisibility" %}
```python
d = dict()
d[0] = 1
cnt = 0
curr = 0

for e in A:
    curr = (curr+e+n)%n # '+n' because of negative numbers
    if curr in d:
        cnt += d[curr]

    if curr in d:
        d[curr] += 1
    else:
        d[curr] = 1
print(cnt)
```
{% endtab %}

{% tab title="atoi" %}
```python
ls = list(s.strip())
if len(ls) == 0 : return 0

sign = -1 if ls[0] == '-' else 1
if ls[0] in ['-','+'] : del ls[0]
ret, i = 0, 0
while i < len(ls) and ls[i].isdigit() :
    ret = ret*10 + ord(ls[i]) - ord('0')
    i += 1
return max(-2**31, min(sign * ret,2**31-1))
```
{% endtab %}

{% tab title="41.✅" %}
```python
# 1. O(NlogN) ===========================
        
nums.sort()
res = 1
for e in nums:
    if res == e:
        res += 1
return res

# 2. O(N) ===================================
# missing number will be in range [1,n]

n = len(nums)

# ignore all out of bound numbers
for i in range(n):
    if nums[i] <= 0 or nums[i] > n:
        nums[i] = n + 1
        
 # mark all the numbers                
for i in range(n):
    if abs(nums[i]) > n:
        continue
    nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

# return first unmarked number
for i in range(n):
    if nums[i] > 0:
        return i + 1
return n + 1
```
{% endtab %}

{% tab title="14." %}
```python
if not strs: return ''
        
m, M = min(strs), max(strs)

for i, c in enumerate(m):
    if c != M[i]:  
        return m[:i]
return m
```
{% endtab %}

{% tab title="334." %}
```python
def increasingTriplet(self, nums: List[int]) -> bool:
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False
```
{% endtab %}

{% tab title="1592" %}
```python
def reorderSpaces(self, text: str) -> str:

    spaces = text.count(" ")
    words = text.split()
    if len(words) == 1:
        return words[0] + (" " * spaces)

    sep_count = len(words) - 1
    spaces_between_words = spaces // sep_count
    spaces_in_the_end = spaces % sep_count
    return (" " * spaces_between_words).join(words) + (" " * spaces_in_the_end)
```
{% endtab %}

{% tab title="68" %}
```python
def fullJustify(self, words: List[str], maxWidth: int):
    
    #--------------------------------------
    # Updated version of EASY: [1592. Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/)
    def reorderSpaces(text):
        spaces = text.count(" ")
        s = text.split(" ")

        while "" in s :
            s.remove("")

        if len(s) == 1:
            return s[0] + " "*spaces

        #min no of spaces between each word
        nsw = spaces//(len(s)-1)
        #no. of spaces left 
        nsl = spaces%(len(s)-1)
        result = ""
        for i in range(len(s)) :
            if i != len(s)-1 :
                result += s[i] + (" ")*nsw
                if nsl > 0:
                    result += " "
                    nsl -= 1
            else:
                result += s[i]  
        return result
    #--------------------------------------
    result = []
    last = words.pop(0)
    while words:
        if len(last) + len(words[0])  >= maxWidth :
            t = last + (" ")*(maxWidth-len(last))
            last = words.pop(0)
            result.append(t)
        elif len(last) + len(words[0]) < maxWidth :
            last = last + " " + words.pop(0)             
    result.append(last + (" ")*(maxWidth-len(last)))

    #reorder every row
    for i in range(len(result)-1):
        result[i] = reorderSpaces(result[i])
    return result 
        
```
{% endtab %}
{% endtabs %}

* [x] CF: [C.Unstable String](https://codeforces.com/problemset/problem/1535/C)
* [x] LC [**Minimum Swaps to Group All 1's Together**](https://leetcode.com/discuss/interview-question/344778/find-the-minimum-number-of-swaps-required-such-that-all-the-0s-and-all-the-1s-are-together)\*\* | [**gfg**](https://www.geeksforgeeks.org/minimum-swaps-required-sort-binary-array/)| @CareemHackerrank\*\*
* [x] \*\*LC \*\*[\*\*926. \*\*Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/)

{% tabs %}
{% tab title="UnstableStr" %}
```python
def solve(s):
    res = 0
    pos0, pos1 = 0,0
    for c in s:
        if c == '0':
            pos0 += 1
            pos1 = 0
            res += pos0
        elif c == '1':
            pos1 += 1
            pos0 = 0
            res += pos1
        else:
            pos1 += 1
            pos0 += 1
            res += max(pos1,pos0)
        pos1, pos0 = pos0,pos1
    return res

t = int(input())
while t:
    t -= 1
    s = str(input())
    print(solve(s))
```
{% endtab %}

{% tab title="Group1" %}
Firstly, count how many 0's in the entire array (suppose the number of 0's is p), then count how many 1's before index p, which is the answer(since those 1's has to be moved to place where index is larger than p-1).

```python
int minSwap(int[] array){
    int p = 0;
    for(int i=0;i<array.length;i++){
        if(array[i]==0){
            p++;
        }
    }
    
    int count = 0;
    for(int i=0;i<p;i++){
        if(array[i]==1){
            count++;
        }
    }

    return count;
}
```

A modified version is below, which also considers the case to move all zeros to the right.

```java
int minSwapBinaryArray(int[] arr)
{
	int countZero = 0;
	int countOne = 0;
	for (int num : arr)
	{
		num == 0 ? countZero++ : countOne++;
	}
	if (countZero * countOne == 0)
	{
		return 0;
	}
	int swapZeroToLeft = 0;
	int swapZeroToRight = 0;
	for (int i = 0; i < countZero; i++)
	{
		if (arr[i] == 1)
		{
			swapZeroToLeft++;
		}
		if (arr[arr.length - 1 - i] == 1)
		{
			swapZeroToRight++;
		}
	}
	return Math.min(swapZeroToLeft, swapZeroToRight);
}
```
{% endtab %}

{% tab title="926" %}
```python
def minFlipsMonoIncr(self, s: str) -> int:
    min_flips = flips = s.count('0')
    for c in s:
        if c == '0':
            flips -= 1
        else:
            flips += 1
        min_flips = min(min_flips, flips)
    return min_flips

'''
IDEA: 
we assume the string after flip is s = '0'*i + '1'*j, the index of first '1' is i

we just need to find the i in the initial string. We make all 1 before index i flip to 0, and make all 0 after index i flip to 1. Then, we get the right answer.



for instance, s = 010110.
if we choose the first 1(index=1) as i, we need to make all 1 before i flip to 0(all 0), make all 0 after i flip to 1(all 2),so the answer is 2.
if we choose the second 1(index=3) as i, the answer is 1 + 1 = 2
if we choose the third 1(index=4) as i, the answer is 2 + 1 = 3
and so on.
```
{% endtab %}
{% endtabs %}

### 1.2 String Matching Algo

* [x] [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/) 🐽

{% tabs %}
{% tab title="Naive Search" %}
```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1

# ============================ One Line code =============================
def strStr(self, haystack: str, needle: str) -> int:
         return haystack.find(needle)
```
{% endtab %}

{% tab title="KMP" %}
```python
# TC: O(N) =========================================================
def strStr(self, haystack: str, needle: str) -> int:
    lps = [0] * len(needle)
    i, j = 1, 0
    if not needle:
        return 0
    # preprocess needle
    while i < len(needle):
        if needle[i] == needle[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j - 1]
    i, j = 0, 0
    # find using lps
    while i < len(haystack) and j < len(needle):
        if needle[j] == haystack[i]:
            if j == len(needle) - 1:
                return i - j
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                continue
            j = lps[j - 1]
    return -1
```
{% endtab %}

{% tab title="Z Algorithm" %}
```python
# TC: O(N) =========================================================
def strStr(self, haystack: str, needle: str) -> int:
    s = needle + "$" + haystack
    left, right = 0, 0
    z = [0] * len(s)
    if not len(needle):
        return 0
    for k in range(1, len(s)):
        if k > right:
            right = left = k
            while right < len(s) and s[right] == s[right - left]:
                right += 1
            z[k] = right - left
            right -= 1
            if z[k] == len(needle):
                return k - 1 - len(needle)
        else:
            if z[k - left] < right - k + 1:
                z[k] = z[k - left]
            else:
                left = k
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                z[k] = right - left
                right -= 1
                if z[k] == len(needle):
                    return k - 1 - len(needle)
    return -1
```
{% endtab %}

{% tab title="Rabin Karp" %}
```python
def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        hck,nle=0,0
        if n<m: return -1
        for i in range(m):
                hck=10*hck+ord(haystack[i])
                nle=10*nle+ord(needle[i])
        for i in range(n-m+1):
                if hck==nle:
                        return i
                if i==n-m: break
                hck=10*(hck-ord(haystack[i])*10**(m-1))+(ord(haystack[i+m]))    
        return -1
```
{% endtab %}
{% endtabs %}

## 2. Hashing

### 2.1 Rolling Hash

* [x] [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) ⚡️ - learn [**Rabin-Karp**](https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/python-binary-search-with-rabin-karp-o\(n-log-n\)-explained)\*\*\*\*
* [ ] [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath)

{% tabs %}
{% tab title="1044" %}
```python
def RabinKarp(self,text, M, q):
    if M == 0: return True
    h, t, d = (1<<(8*M-8))%q, 0, 256

    dic = defaultdict(list)

    for i in range(M): 
        t = (d * t + ord(text[i]))% q

    dic[t].append(i-M+1)

    for i in range(len(text) - M):
        t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
        for j in dic[t]:
            if text[i+1:i+M+1] == text[j:j+M]:
                return (True, text[j:j+M])
        dic[t].append(i+1)
    return (False, "")

def longestDupSubstring(self, S):
    beg, end = 0, len(S)
    q = (1<<31) - 1 
    Found = ""
    while beg + 1 < end:
        mid = (beg + end)//2
        isFound, candidate = self.RabinKarp(S, mid, q)
        if isFound:
            beg, Found = mid, candidate
        else:
            end = mid

    return Found
```
{% endtab %}
{% endtabs %}

ffafa
