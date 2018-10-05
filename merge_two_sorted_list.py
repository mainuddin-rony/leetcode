# Problem link: https://leetcode.com/problems/merge-two-sorted-lists/description/

## TODO later

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while (l1 and l2):
            print(l1.val, l2.val)
            if (l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if (l1):
            p.next = l1
        elif (l2):
            p.next = l2
        return dummy.next


l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])
sol = Solution()
sol_list = sol.mergeTwoLists(l1, l2)

