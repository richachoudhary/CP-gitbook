---
description: 'All the problems from LC, categorised'
---

# DP

## \# Notes 

*  **Approach for DP problem:**  find Recursion **===&gt;** Memoize it **===&gt;** \(optional\) Top-Down OR matrix
* Using **MEMO** in python: \(using **dict**-  constant lookup time\)

```python
MEMO = {}
# ... use memo inside recur fn
if (a,b,c) in MEMO: return MEMO[(a,b,c)]
# find res & set in MEMO
MEMO[(a,b,c)] = res
```

* Memoization vs Top-Down: \(_both have same space & time complexities_\)
  * **Recursion+Memoization** is easy to think & code.**should be your goto** approach for all DP ques.
    * in Rarest of rare cases; it might lead to _recursive stack overflow err_
  * **Top-Down:** nobody can write it w/o recursive. Avoid for new/unseen problems
    * If recursion+memo gives stack-overflow err, use Top-Down!

## 1. Linear DP

* [ ] [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [ ] [https://leetcode.com/problems/min-cost-climbing-stairs/](https://leetcode.com/problems/min-cost-climbing-stairs/)
* [ ] [https://leetcode.com/problems/divisor-game/](https://leetcode.com/problems/divisor-game/)
* [ ] [https://leetcode.com/problems/decode-ways/](https://leetcode.com/problems/decode-ways/)
* [ ] [https://leetcode.com/problems/unique-binary-search-trees/](https://leetcode.com/problems/unique-binary-search-trees/)
* [ ] [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
* [ ] [https://leetcode.com/problems/counting-bits/](https://leetcode.com/problems/counting-bits/)
* [ ] [https://leetcode.com/problems/integer-break/](https://leetcode.com/problems/integer-break/)
* [ ] [https://leetcode.com/problems/count-numbers-with-unique-digits/](https://leetcode.com/problems/count-numbers-with-unique-digits/)
* [ ] [https://leetcode.com/problems/wiggle-subsequence/](https://leetcode.com/problems/wiggle-subsequence/)
* [ ] [https://leetcode.com/problems/maximum-length-of-pair-chain/](https://leetcode.com/problems/maximum-length-of-pair-chain/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
* [ ] [https://leetcode.com/problems/delete-and-earn/](https://leetcode.com/problems/delete-and-earn/)
* [ ] [https://leetcode.com/problems/domino-and-tromino-tiling/](https://leetcode.com/problems/domino-and-tromino-tiling/)
* [ ] [https://leetcode.com/problems/knight-dialer/](https://leetcode.com/problems/knight-dialer/)
* [ ] [https://leetcode.com/problems/minimum-cost-for-tickets/](https://leetcode.com/problems/minimum-cost-for-tickets/)
* [ ] [https://leetcode.com/problems/partition-array-for-maximum-sum/](https://leetcode.com/problems/partition-array-for-maximum-sum/)
* [ ] [https://leetcode.com/problems/filling-bookcase-shelves/](https://leetcode.com/problems/filling-bookcase-shelves/)
* [ ] [https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)
* [ ] [https://leetcode.com/problems/greatest-sum-divisible-by-three/](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
* [ ] [https://leetcode.com/problems/student-attendance-record-ii/](https://leetcode.com/problems/student-attendance-record-ii/)
* [ ] [https://leetcode.com/problems/decode-ways-ii/](https://leetcode.com/problems/decode-ways-ii/)
* [ ] [https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)
* [ ] [https://leetcode.com/problems/maximum-profit-in-job-scheduling/](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
* [ ] [https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)
* [ ] [https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)
* [ ] [https://leetcode.com/problems/stone-game-iii/](https://leetcode.com/problems/stone-game-iii/)
* [ ] [https://leetcode.com/problems/restore-the-array/](https://leetcode.com/problems/restore-the-array/)
* [ ] [https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/)
* [ ] [https://leetcode.com/problems/stone-game-iv/](https://leetcode.com/problems/stone-game-iv/)

## 2.1 0/1 Knapsack

```python
def knapsack(wt, val, W):    #NOTE: wt is sorted here; if not->first sort
    MEMO = {}
    def recur(wt,val,W,n):
        if n == 0 or W == 0:        # base case
            return 0
        if (W,n) in MEMO: return MEMO[(W,n)]
        if wt[n-1] <= W:
            opt1 = val[n-1] + recur(wt,val,W-wt[n-1],n-1)    # inclue
            opt2 = recur(wt,val,W,n-1)                       # dont inclue
            MEMO[(W,n)] = max(opt1,opt2)
         else:
            MEMO[(W,n)] = recur(wt,val,W,n-1)      # too heavy, cant inclue
        return MEMO[(W,n)]
                
    n = len(wt)
    return recur(wt,val,W,n)
```

#### 2.1.1 0/1 Knapsack Standard Variations \| source : [AdityaVerma](https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10&ab_channel=AdityaVerma)

* [x] GfG: [Subset Sum Problem](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
* [x] [416.Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
* [x] [GfG:: Count of subsets sum with a Given sum](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)
  * Replace `or` with `+` in Subset Sum Problem
* [x] [GfG: Sum of subset differences](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/)
  * [x] **Similar:**  [1049.Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/submissions/)
* [x] [494.Target Sum](https://leetcode.com/problems/target-sum/)  🎖

#### 2.1.2  Problems: 0/1 Knapsack 

* [ ] [https://leetcode.com/problems/house-robber-ii/](https://leetcode.com/problems/house-robber-ii/)
* [ ] [https://leetcode.com/problems/ones-and-zeroes/](https://leetcode.com/problems/ones-and-zeroes/)
* [ ] [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)
* [ ] [https://leetcode.com/problems/shopping-offers/](https://leetcode.com/problems/shopping-offers/)
* [ ] [https://leetcode.com/problems/2-keys-keyboard/](https://leetcode.com/problems/2-keys-keyboard/)
* [ ] [https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)
* [ ] [https://leetcode.com/problems/best-team-with-no-conflicts/](https://leetcode.com/problems/best-team-with-no-conflicts/)
* [ ] [https://leetcode.com/problems/profitable-schemes/](https://leetcode.com/problems/profitable-schemes/)
* [ ] [https://leetcode.com/problems/tallest-billboard/](https://leetcode.com/problems/tallest-billboard/)
* [ ] [https://leetcode.com/problems/pizza-with-3n-slices/](https://leetcode.com/problems/pizza-with-3n-slices/)
* [ ] [https://leetcode.com/problems/reducing-dishes/](https://leetcode.com/problems/reducing-dishes/)

## 2.2 Unbounded Knapsack 

```python
def knapsack(wt, val, W):    #NOTE: wt is sorted here; if not->first sort
    MEMO = {}
    def recur(wt,val,W,n):
        if n == 0 or W == 0:  
            return 0
        if (W,n) in MEMO: return MEMO[(W,n)]
        if wt[n-1] <= W:
            # we can again take all n elements
            opt1 = val[n-1] + recur(wt,val,W-wt[n-1],n)  # just this much change
            opt2 = recur(wt,val,W,n-1)             
            MEMO[(W,n)] = max(opt1,opt2)
         else:
            MEMO[(W,n)] = recur(wt,val,W,n-1)    
        return MEMO[(W,n)]
                
    n = len(wt)
    return recur(wt,val,W,n)
```

#### 2.2.1 Standard Problems: Unbounded Knapsack 

* [x] CSES: [Coin Combinations 1](https://cses.fi/problemset/task/1635/)
  * [ ] CSES: [Coin Combinations 2](https://cses.fi/problemset/task/1636)
* [x] [322.Coin Change](https://leetcode.com/problems/coin-change/) 🌟
* [x] [518.Coin Change 2](https://leetcode.com/problems/coin-change-2/)
* [x] GfG: [Rod Cutting Problem](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)         
  * [ ] Similar\(but Hard\)[1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

#### 2.2.2  Problems: Unbounded Knapsack 

* [ ] ..

## 3. Multi Dimension DP

* [ ] [https://leetcode.com/problems/triangle/](https://leetcode.com/problems/triangle/)
* [ ] [https://leetcode.com/problems/combination-sum-iv/](https://leetcode.com/problems/combination-sum-iv/)
* [ ] [https://leetcode.com/problems/out-of-boundary-paths/](https://leetcode.com/problems/out-of-boundary-paths/)
* [ ] [https://leetcode.com/problems/knight-probability-in-chessboard/](https://leetcode.com/problems/knight-probability-in-chessboard/)
* [ ] [https://leetcode.com/problems/champagne-tower/](https://leetcode.com/problems/champagne-tower/)
* [ ] [https://leetcode.com/problems/largest-sum-of-averages/](https://leetcode.com/problems/largest-sum-of-averages/)
* [ ] [https://leetcode.com/problems/minimum-falling-path-sum/](https://leetcode.com/problems/minimum-falling-path-sum/)
* [ ] [https://leetcode.com/problems/video-stitching/](https://leetcode.com/problems/video-stitching/)
* [ ] [https://leetcode.com/problems/longest-arithmetic-subsequence/](https://leetcode.com/problems/longest-arithmetic-subsequence/)
* [ ] [https://leetcode.com/problems/stone-game-ii/](https://leetcode.com/problems/stone-game-ii/)
* [ ] [https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
* [x] [https://leetcode.com/problems/dice-roll-simulation/](https://leetcode.com/problems/dice-roll-simulation/)
* [ ] [https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)
* [ ] [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
* [ ] [https://leetcode.com/problems/create-maximum-number/](https://leetcode.com/problems/create-maximum-number/)
* [ ] [https://leetcode.com/problems/frog-jump/](https://leetcode.com/problems/frog-jump/)
* [ ] [https://leetcode.com/problems/split-array-largest-sum/](https://leetcode.com/problems/split-array-largest-sum/)
* [ ] [https://leetcode.com/problems/freedom-trail/](https://leetcode.com/problems/freedom-trail/)
* [ ] [https://leetcode.com/problems/minimum-number-of-refueling-stops/](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
* [ ] [https://leetcode.com/problems/number-of-music-playlists/](https://leetcode.com/problems/number-of-music-playlists/)
* [ ] [https://leetcode.com/problems/count-vowels-permutation/](https://leetcode.com/problems/count-vowels-permutation/)
* [ ] [https://leetcode.com/problems/minimum-falling-path-sum-ii/](https://leetcode.com/problems/minimum-falling-path-sum-ii/)
* [ ] [https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)
* [ ] [https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)
* [ ] [https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
* [ ] [https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/)
* [ ] [https://leetcode.com/problems/paint-house-iii/](https://leetcode.com/problems/paint-house-iii/)
* [ ] [https://leetcode.com/problems/count-all-possible-routes/](https://leetcode.com/problems/count-all-possible-routes/)

## 4. Interval DP

* [ ] [https://leetcode.com/problems/guess-number-higher-or-lower-ii/](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)
* [ ] [https://leetcode.com/problems/arithmetic-slices/](https://leetcode.com/problems/arithmetic-slices/)
* [ ] [https://leetcode.com/problems/predict-the-winner/](https://leetcode.com/problems/predict-the-winner/)
* [ ] [https://leetcode.com/problems/palindromic-substrings/](https://leetcode.com/problems/palindromic-substrings/)
* [ ] [https://leetcode.com/problems/stone-game/](https://leetcode.com/problems/stone-game/)
* [ ] [https://leetcode.com/problems/minimum-score-triangulation-of-polygon/](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)
* [ ] [https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)
* [ ] [https://leetcode.com/problems/stone-game-vii/](https://leetcode.com/problems/stone-game-vii/)
* [ ] [https://leetcode.com/problems/burst-balloons/](https://leetcode.com/problems/burst-balloons/)
* [ ] [https://leetcode.com/problems/remove-boxes/](https://leetcode.com/problems/remove-boxes/)
* [ ] [https://leetcode.com/problems/strange-printer/](https://leetcode.com/problems/strange-printer/)
* [ ] [https://leetcode.com/problems/valid-permutations-for-di-sequence/](https://leetcode.com/problems/valid-permutations-for-di-sequence/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-merge-stones/](https://leetcode.com/problems/minimum-cost-to-merge-stones/)
* [ ] [https://leetcode.com/problems/allocate-mailboxes/](https://leetcode.com/problems/allocate-mailboxes/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-cut-a-stick/](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
* [ ] [https://leetcode.com/problems/stone-game-v/](https://leetcode.com/problems/stone-game-v/)

## 5. Bit DP

* [ ] [https://leetcode.com/problems/can-i-win/](https://leetcode.com/problems/can-i-win/)
* [ ] [https://leetcode.com/problems/partition-to-k-equal-sum-subsets/](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
* [ ] [https://leetcode.com/problems/stickers-to-spell-word/](https://leetcode.com/problems/stickers-to-spell-word/)
* [ ] [https://leetcode.com/problems/shortest-path-visiting-all-nodes/](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
* [ ] [https://leetcode.com/problems/smallest-sufficient-team/](https://leetcode.com/problems/smallest-sufficient-team/)
* [ ] [https://leetcode.com/problems/maximum-students-taking-exam/](https://leetcode.com/problems/maximum-students-taking-exam/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)
* [ ] [https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/)
* [ ] [https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)
* [ ] [https://leetcode.com/problems/distribute-repeating-integers/](https://leetcode.com/problems/distribute-repeating-integers/)
* [ ] [https://leetcode.com/problems/maximize-grid-happiness/](https://leetcode.com/problems/maximize-grid-happiness/)
* [ ] [https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)

### 5.1 Resources: Bit DP

* ✅Kartik Arora's Playlist: [Bitwise DP](https://www.youtube.com/watch?v=6sEFap7hIl4&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&ab_channel=KartikArora)

## 6. Digit DP

* [ ] [https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/)
* [ ] [https://leetcode.com/problems/numbers-at-most-n-given-digit-set/](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)
* [ ] [https://leetcode.com/problems/numbers-with-repeated-digits/](https://leetcode.com/problems/numbers-with-repeated-digits/)

### 6.1 Resources: Digit DP

* ✅Kartik Arora's playlist: [Digit DP](https://www.youtube.com/watch?v=heUFId6Qd1A&list=PLb3g_Z8nEv1hB69JL9K7KfEyK8iQNj9nX&ab_channel=KartikArora)

## 7. DP on Trees

* [ ] [https://leetcode.com/problems/unique-binary-search-trees-ii/](https://leetcode.com/problems/unique-binary-search-trees-ii/)
* [ ] [https://leetcode.com/problems/house-robber-iii/](https://leetcode.com/problems/house-robber-iii/)
* [ ] [https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)
* [ ] [https://leetcode.com/problems/linked-list-in-binary-tree/](https://leetcode.com/problems/linked-list-in-binary-tree/)
* [ ] [https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)
* [ ] [https://leetcode.com/problems/binary-tree-cameras/](https://leetcode.com/problems/binary-tree-cameras/)
* [ ] [https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

### 7.1 Resources: Tree DP

* ✅Kartik Arora's Playlist: [Tree DP](https://www.youtube.com/watch?v=fGznXJ-LTbI&list=PLb3g_Z8nEv1j_BC-fmZWHFe6jmU_zv-8s&ab_channel=KartikArora)

## 8. DP on Graph

* [ ] [https://leetcode.com/problems/cheapest-flights-within-k-stops/](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
* [ ] [https://leetcode.com/problems/find-the-shortest-superstring/](https://leetcode.com/problems/find-the-shortest-superstring/)

## 9. String DP

* [ ] [https://leetcode.com/problems/is-subsequence/](https://leetcode.com/problems/is-subsequence/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning/](https://leetcode.com/problems/palindrome-partitioning/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning-ii/](https://leetcode.com/problems/palindrome-partitioning-ii/)
* [ ] [https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)
* [ ] [https://leetcode.com/problems/unique-substrings-in-wraparound-string/](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)
* [ ] [https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
* [ ] [https://leetcode.com/problems/longest-string-chain/](https://leetcode.com/problems/longest-string-chain/)
* [ ] [https://leetcode.com/problems/longest-happy-string/](https://leetcode.com/problems/longest-happy-string/)
* [ ] [https://leetcode.com/problems/longest-valid-parentheses/](https://leetcode.com/problems/longest-valid-parentheses/)
* [ ] [https://leetcode.com/problems/distinct-subsequences/](https://leetcode.com/problems/distinct-subsequences/)
* [ ] [https://leetcode.com/problems/word-break-ii/](https://leetcode.com/problems/word-break-ii/)
* [ ] [https://leetcode.com/problems/count-the-repetitions/](https://leetcode.com/problems/count-the-repetitions/)
* [ ] [https://leetcode.com/problems/concatenated-words/](https://leetcode.com/problems/concatenated-words/)
* [ ] [https://leetcode.com/problems/count-different-palindromic-subsequences/](https://leetcode.com/problems/count-different-palindromic-subsequences/)
* [ ] [https://leetcode.com/problems/distinct-subsequences-ii/](https://leetcode.com/problems/distinct-subsequences-ii/)
* [ ] [https://leetcode.com/problems/longest-chunked-palindrome-decomposition/](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)
* [ ] [https://leetcode.com/problems/palindrome-partitioning-iii/](https://leetcode.com/problems/palindrome-partitioning-iii/)
* [ ] [https://leetcode.com/problems/find-all-good-strings/](https://leetcode.com/problems/find-all-good-strings/)
* [ ] [https://leetcode.com/problems/string-compression-ii/](https://leetcode.com/problems/string-compression-ii/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)

## 9. Probability DP

* [ ] [https://leetcode.com/problems/soup-servings/](https://leetcode.com/problems/soup-servings/)
* [ ] [https://leetcode.com/problems/new-21-game/](https://leetcode.com/problems/new-21-game/)
* [ ] [https://leetcode.com/problems/airplane-seat-assignment-probability/](https://leetcode.com/problems/airplane-seat-assignment-probability/)

## 10. Classic DPs

### 10.1 Cadane's Algorithm

* [ ] [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
* [ ] [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)
* [ ] [https://leetcode.com/problems/bitwise-ors-of-subarrays/](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
* [ ] [https://leetcode.com/problems/longest-turbulent-subarray/](https://leetcode.com/problems/longest-turbulent-subarray/)
* [ ] [https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)
* [ ] [https://leetcode.com/problems/k-concatenation-maximum-sum/](https://leetcode.com/problems/k-concatenation-maximum-sum/)
* [ ] [https://leetcode.com/problems/largest-divisible-subset/](https://leetcode.com/problems/largest-divisible-subset/)
* [ ] [https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)

### 10.2 LCS

* [ ] [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)
* [ ] [https://leetcode.com/problems/longest-palindromic-subsequence/](https://leetcode.com/problems/longest-palindromic-subsequence/)
* [ ] [https://leetcode.com/problems/maximum-length-of-repeated-subarray/](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)[**=**](https://leetcode.com/problems/longest-common-subsequence/)
* [ ] [https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)
* [ ] [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)
* [ ] [https://leetcode.com/problems/wildcard-matching/](https://leetcode.com/problems/wildcard-matching/)
* [ ] [https://leetcode.com/problems/edit-distance/](https://leetcode.com/problems/edit-distance/)
* [ ] [https://leetcode.com/problems/interleaving-string/](https://leetcode.com/problems/interleaving-string/)
* [ ] [https://leetcode.com/problems/shortest-common-supersequence/](https://leetcode.com/problems/shortest-common-supersequence/)
* [ ] [https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
* [ ] [https://leetcode.com/problems/max-dot-product-of-two-subsequences/](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

### 10.3 LIS

* [ ] [https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)
* [ ] [https://leetcode.com/problems/number-of-longest-increasing-subsequence/](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
* [ ] [https://leetcode.com/problems/russian-doll-envelopes/](https://leetcode.com/problems/russian-doll-envelopes/)
* [ ] [https://leetcode.com/problems/delete-columns-to-make-sorted-iii/](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)
* [ ] [https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/)
* [ ] [https://leetcode.com/problems/maximum-height-by-stacking-cuboids/](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/)
* [ ] [https://leetcode.com/problems/make-array-strictly-increasing/](https://leetcode.com/problems/make-array-strictly-increasing/)



### 10.4  2D Grid Traversal

* [ ] [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)
* [ ] [https://leetcode.com/problems/unique-paths-ii/](https://leetcode.com/problems/unique-paths-ii/)
* [ ] [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)
* [ ] [https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/)
* [ ] [https://leetcode.com/problems/where-will-the-ball-fall/](https://leetcode.com/problems/where-will-the-ball-fall/)
* [ ] [https://leetcode.com/problems/dungeon-game/](https://leetcode.com/problems/dungeon-game/)
* [ ] [https://leetcode.com/problems/cherry-pickup/](https://leetcode.com/problems/cherry-pickup/)
* [ ] [https://leetcode.com/problems/number-of-paths-with-max-score/](https://leetcode.com/problems/number-of-paths-with-max-score/)
* [ ] [https://leetcode.com/problems/cherry-pickup-ii/](https://leetcode.com/problems/cherry-pickup-ii/)
* [ ] [https://leetcode.com/problems/kth-smallest-instructions/](https://leetcode.com/problems/kth-smallest-instructions/)

### 10.5 Cumulative Sum

* [ ] [https://leetcode.com/problems/range-sum-query-immutable/](https://leetcode.com/problems/range-sum-query-immutable/)
* [ ] [https://leetcode.com/problems/maximal-square/](https://leetcode.com/problems/maximal-square/)
* [ ] [https://leetcode.com/problems/range-sum-query-2d-immutable/](https://leetcode.com/problems/range-sum-query-2d-immutable/)
* [ ] [https://leetcode.com/problems/largest-plus-sign/](https://leetcode.com/problems/largest-plus-sign/)
* [ ] [https://leetcode.com/problems/push-dominoes/](https://leetcode.com/problems/push-dominoes/)
* [ ] [https://leetcode.com/problems/largest-1-bordered-square/](https://leetcode.com/problems/largest-1-bordered-square/)
* [ ] [https://leetcode.com/problems/count-square-submatrices-with-all-ones/](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
* [ ] [https://leetcode.com/problems/matrix-block-sum/](https://leetcode.com/problems/matrix-block-sum/)
* [ ] [https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
* [ ] [https://leetcode.com/problems/count-submatrices-with-all-ones/](https://leetcode.com/problems/count-submatrices-with-all-ones/)
* [ ] [https://leetcode.com/problems/ways-to-make-a-fair-array/](https://leetcode.com/problems/ways-to-make-a-fair-array/)[=](https://leetcode.com/problems/maximal-rectangle/)
* [ ] [https://leetcode.com/problems/maximal-rectangle/](https://leetcode.com/problems/maximal-rectangle/)
* [ ] [https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)
* [ ] [https://leetcode.com/problems/super-washing-machines/](https://leetcode.com/problems/super-washing-machines/)
* [ ] [https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)
* [ ] [https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
* [ ] [https://leetcode.com/problems/get-the-maximum-score/](https://leetcode.com/problems/get-the-maximum-score/)

### 10.6 Hashmap\(SubArray\)

* [ ] [https://leetcode.com/problems/continuous-subarray-sum/](https://leetcode.com/problems/continuous-subarray-sum/)
* [ ] [https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)
* [ ] [https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

## 11. DP + Alpha \(Tricks/DS\)

* [ ] [https://leetcode.com/problems/arithmetic-slices-ii-subsequence/](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)
* [ ] [https://leetcode.com/problems/odd-even-jump/](https://leetcode.com/problems/odd-even-jump/)
* [ ] [https://leetcode.com/problems/constrained-subsequence-sum/](https://leetcode.com/problems/constrained-subsequence-sum/)
* [ ] [https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)

## 12. Insertion DP

* [ ] [https://leetcode.com/problems/k-inverse-pairs-array/](https://leetcode.com/problems/k-inverse-pairs-array/)

## 13. Memoization

* [ ] [https://leetcode.com/problems/minimum-jumps-to-reach-home/](https://leetcode.com/problems/minimum-jumps-to-reach-home/)
* [ ] [https://leetcode.com/problems/scramble-string/](https://leetcode.com/problems/scramble-string/)
* [ ] [https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)
* [ ] [https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/)
* [ ] [https://leetcode.com/problems/jump-game-v/](https://leetcode.com/problems/jump-game-v/)
* [ ] [https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/)

## 14. Binary Lifting

* [ ] [https://leetcode.com/problems/kth-ancestor-of-a-tree-node/](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)

## 15. Math

* [ ] [https://leetcode.com/problems/ugly-number-ii/](https://leetcode.com/problems/ugly-number-ii/)
* [ ] [https://leetcode.com/problems/count-sorted-vowel-strings/](https://leetcode.com/problems/count-sorted-vowel-strings/)
* [ ] [https://leetcode.com/problems/race-car/](https://leetcode.com/problems/race-car/)
* [ ] [https://leetcode.com/problems/super-egg-drop/](https://leetcode.com/problems/super-egg-drop/)
* [ ] [https://leetcode.com/problems/least-operators-to-express-number/](https://leetcode.com/problems/least-operators-to-express-number/)
* [ ] [https://leetcode.com/problems/largest-multiple-of-three/](https://leetcode.com/problems/largest-multiple-of-three/)
* [ ] [https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)









## Resources

* DP Patterns for Beginners: [https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions](https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions)
* **Solved all DP problems in 7 months:** [**https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months**](https://leetcode.com/discuss/general-discussion/1000929/solved-all-dynamic-programming-dp-problems-in-7-months) ****
* DP pattens list: [https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491](https://leetcode.com/discuss/general-discussion/1050391/Must-do-Dynamic-programming-Problems-Category-wise/845491)
* @youtube:
  * WilliamFiset Playlist: [https://www.youtube.com/watch?v=gQszF5qdZ-0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&ab\_channel=WilliamFiset](https://www.youtube.com/watch?v=gQszF5qdZ-0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&ab_channel=WilliamFiset)
  * **✅Aditya Verma Playlist**: [https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL\_z\_8CaSLPWekqhdCPmFohncHwz8TY2Go&ab\_channel=AdityaVerma](https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&ab_channel=AdityaVerma)
    * Good for problem classification & variety, but poor for intuition building
  * **✅Kartik Arora's Playlist:** [https://www.youtube.com/watch?v=24hk2qW\_BCU&list=PLb3g\_Z8nEv1h1w6MI8vNMuL\_wrI0FtqE7&ab\_channel=KartikArora](https://www.youtube.com/watch?v=24hk2qW_BCU&list=PLb3g_Z8nEv1h1w6MI8vNMuL_wrI0FtqE7&ab_channel=KartikArora)

