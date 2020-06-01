# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        power = 0
        carry = 0
        ret = ListNode(0)
        current = ret
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            num = carry + v1 + v2
            carry = num // 10
            this_node = ListNode(num % 10)
            if power == 0:
                ret = this_node
            else:
                current.next = this_node
            current = this_node
            power += 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ret

