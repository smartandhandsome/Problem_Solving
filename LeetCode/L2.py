# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False

        node = l1
        i = 1
        num1 = 0
        while node:
            num1 += node.val * i
            i *= 10
            node = node.next

        node = l2
        i = 1
        num2 = 0
        while node:
            num2 += node.val * i
            i *= 10
            node = node.next
        num = num1 + num2
        print(num)

        answer = ListNode()
        n = answer
        while True:
            n.val = num % 10
            num //= 10
            if num == 0:
                break
            n.next = ListNode()
            n = n.next
        return answer
