class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def addTwoNumbers(l1, l2):
        head = tail = ListNode()
        carry = 0
        while carry or l1 or l2:
            temp = carry
            if l1:
                temp = temp + l1.val
                l1 = l1.next
            if l2:
                temp = temp + l2.val
                l2 = l2.next
            node = ListNode(temp % 10, None)
            tail.next = node
            tail = node
            carry = temp // 10

        return head.next


l1 = ListNode(0)
l2 = ListNode(0)
numbers = Solution.addTwoNumbers(l1, l2)
print(numbers.val)
