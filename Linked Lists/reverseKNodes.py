# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            curr = head
            next = head.next
            done = None
            while next != tail.next:
                curr.next = done
                done = curr
                curr = next
                next = next.next
            curr.next = done
            return curr, head
        
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # step 5: walk k steps to find the k-th node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:       # step 6: fewer than k nodes left
                    return dummy.next

            after = kth.next                      # step 7
            new_front, new_back = reverse(group_prev.next, kth)  # step 8
            group_prev.next = new_front           # step 9: reconnect front
            new_back.next = after                 # step 10: reconnect back
            group_prev = new_back                 # step 11: advance
