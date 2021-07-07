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

* [x] [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) 🌟
* [x] [82.Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) 🌟 🏴‍☠️

{% tabs %}
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
{% endtabs %}

* [ ] [234.Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
* [ ] [61.Rotate List](https://leetcode.com/problems/rotate-list/)
* [ ] [2.Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
* [ ] [141.Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
* [ ] [142.Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
* [ ] [138.Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

## 2. All Problems



* [ ] GfG: [Remove duplicates from Unsorted List](https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/)

