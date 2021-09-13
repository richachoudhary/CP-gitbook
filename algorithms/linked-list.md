# Linked List

## 0. Notes:

* Try to do every problem in both: **iterative** & **recursive** ways
* Defining LinkedList

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 1. Common Problems

* [x] [148.Sort List](https://leetcode.com/problems/sort-list/) \| **MergeSort ✅✅**
* [x] [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) 🌟
* [x] [82.Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) 🌟 🏴‍☠️

{% tabs %}
{% tab title="148" %}
```python
def mergeSort(head):
    if not head or not head.next : 
        return head                 # as we branch and move left, left ... when only one node is left, we return it
    
    left = slow = fast = head
    fast = fast.next                # for [1,2,3,4] as mid will be node 3, if this statement not used
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    right = slow.next               # slow is at middle, next elements are considered right
    slow.next = None                # this makes left has only left part
    
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    return merge(left_sorted, right_sorted)

def merge(l1, l2):
    dummy = ListNode(-1)
    prev = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next            
        prev = prev.next
    prev.next = l1 or l2    # one of l1 and l2 can be non-null at this point
    return dummy.next

return mergeSort(head)
```
{% endtab %}

{% tab title="83. remove I" %}
```python
def deleteDuplicates(head):
        #1.============================= Iterative
        curr = head
        while curr and curr.next:
            while curr and curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
        #2.============================= Recursive
        if not head or not head.next:
            return head
        if head.next:
            if head.next.val == head.val:
                head.next = head.next.next
                head = deleteDuplicates(head)
            else:
                head.next = deleteDuplicates(head.next)
        return head
```
{% endtab %}

{% tab title="82. remove II" %}
```python
def deleteDuplicates(head):
    # 1. ======================================== Iterative
    curr = ListNode(None)
    curr.next=head
    res = curr
    
    while curr.next and curr.next.next:
        if curr.next.val == curr.next.next.val:
            tmp = curr.next.next
            value = curr.next.val
            while tmp.next and tmp.next.val == value:
                tmp = tmp.next
            curr.next = tmp.next
        else:
            curr = curr.next
    return res.next    
    # 2. ======================================== Recursive
    if not head : return None
    if not head.next: return head

    value = head.val
    tmp = head.next
    
    if tmp.val != value:
        head.next = self.deleteDuplicates(tmp)
        return head
    else:
        while tmp and tmp.val == value:
            tmp = tmp.next
        return self.deleteDuplicates(tmp)
```
{% endtab %}
{% endtabs %}



* [x] [206.Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [ ] [92.Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

{% tabs %}
{% tab title="reverse I" %}
```python
def helper(curr, prev):
    if not curr:
        return prev
    nxt = curr.next
    curr.next = prev
    return helper(nxt,curr)

return helper(head,None)
```
{% endtab %}

{% tab title="reverse II" %}
```python

```
{% endtab %}

{% tab title="141." %}
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
```
{% endtab %}

{% tab title="2.✅" %}
```python
dummy = cur = ListNode(0)
carry = 0
while l1 or l2 or carry:
    if l1:
        carry += l1.val
        l1 = l1.next
    if l2:
        carry += l2.val
        l2 = l2.next
    cur.next = ListNode(carry%10)
    cur = cur.next
    carry //= 10
return dummy.next
```
{% endtab %}

{% tab title="234.✅" %}
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
        slow = self.reverseList(slow)
        fast = head
        
        while(slow):
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True
      
    def reverseList(self, node):
        current = node
        previous = None
        
        while(current):
            currentNext = current.next
            current.next = previous
            previous = current
            current = currentNext
            
        return previous
```
{% endtab %}

{% tab title="138." %}
```python
def copyRandomList(self, head: 'Node') -> 'Node':    
    oldToCopy = { None:None}    #for last node
    
    #1. first pass: hashmap key: old node, val: new copy node
    curr = head
    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next
    
    #2. second pass: creating .next & .random for copy nodes
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
    
    return oldToCopy[head]
```
{% endtab %}

{% tab title="23.🍪" %}
```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    head = ListNode(None)
    curr = head
    h = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    while h:
        val, i = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    return head.next
```
{% endtab %}

{% tab title="287💪 \| ShareChat" %}
```python
def findDuplicate(self, nums):
        
        # 1. Rabbit-Tortoise method ==========================================================
        # TC:O(N) , SC:(1)
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
           
        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
    
    
        #2. Binary Search ==========================================================================
        '''
        Let us choose middle element m = n//2 and count number of elements in list, 
        which are less or equal than m. 
        If we have m+1 of them it means we need to search for duplicate in [1,m] range, else in [m+1,n] range
        '''
        #TC: O(NlogN) , SC: O(1)
        
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return high
```
{% endtab %}
{% endtabs %}

* [x] [234.Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) ✅
* [ ] [61.Rotate List](https://leetcode.com/problems/rotate-list/)
* [x] [2.Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) ✅🚀
* [x] [141.Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) ✅🚀
* [ ] [142.Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
* [x] [138.Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) \| Deep copy \| chillar
* [x] 23. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) 🍪🍪🍪✅
* [x] LC [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) \| **Rabbit-Tortoise** method on array \| had me failed **@ShareChat** back then 💪 \| also see in `BinarySearch`

## 2. All Problems



* [ ] GfG: [Remove duplicates from Unsorted List](https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/)

