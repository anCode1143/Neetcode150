class MyCircularQueue:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self, k: int):
        self.maxLength = k
        self.len = 0
        self.front = self.back = None

    def enQueue(self, value: int) -> bool:
        if self.len == self.maxLength:
            return False
        if self.len == 0:
            self.front = self.back = self.ListNode(val=value)
        else:
            self.back.next = self.ListNode(val=value)
            self.back = self.back.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        self.front = self.front.next
        self.len -= 1
        if self.len == 0:
            self.front = self.back = None
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.len == self.maxLength:
            return True
        return False
    
        class ListNode:
            def __init__(self, val, nxt=None):
                self.val = val
                self.next = nxt

        class MyCircularQueue:
            def __init__(self, k: int):
                self.space = k
                self.left = ListNode(0)
                self.right = self.left

            def enQueue(self, value: int) -> bool:
                if self.isFull(): return False

                cur = ListNode(value)
                if self.isEmpty():
                    self.left.next = cur
                    self.right = cur
                else:
                    self.right.next = cur
                    self.right = cur

                self.space -= 1
                return True

            def deQueue(self) -> bool:
                if self.isEmpty(): return False

                self.left.next = self.left.next.next
                if self.left.next is None:
                    self.right = self.left

                self.space += 1
                return True

            def Front(self) -> int:
                if self.isEmpty(): return -1
                return self.left.next.val

            def Rear(self) -> int:
                if self.isEmpty(): return -1
                return self.right.val

            def isEmpty(self) -> bool:
                return self.left.next is None

            def isFull(self) -> bool:
                return self.space == 0
            
"""
cue for diagnosing pattern - links, adding and removing elements dynamically with pointers

how to implement the solution - be careful of exceptions

struggled parts - flow control and conditional states

complexity details
    speed - all operations are constant
    memory - constant overheaad
"""