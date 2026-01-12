class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next=list1)
        ptrA = list1
        for _ in range(a-1):
            ptrA = ptrA.next
        ptrB = list1
        for _ in range(b+1):
            ptrB = ptrB.next
        list2Tail = list2
        while list2Tail.next:
            list2Tail = list2Tail.next
        ptrA.next = list2
        list2Tail.next = ptrB

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0

        while i < a - 1:
            curr = curr.next
            i += 1
        head = curr

        while i <= b:
            curr = curr.next
            i += 1

        head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr

        return list1