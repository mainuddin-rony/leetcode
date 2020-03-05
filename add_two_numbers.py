# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_numbers = []
        l2_numbers = []
        while l1 != None:
            l1_numbers.append(l1.val)
            l1 = l1.next
        while l2 != None:
            l2_numbers.append(l2.val)
            l2 = l2.next
            
        l1_numbers.reverse()
        l2_numbers.reverse()
        l1_int = int("".join(map(str,l1_numbers)))
        l2_int = int("".join(map(str,l2_numbers)))
        l1_l2_sum = l1_int + l2_int
        
        rev_list = [int(d) for d in str(l1_l2_sum)]
        rev_list.reverse()
        print(rev_list)
        
        sum_l = ListNode(rev_list[0])
        temp = sum_l
        
        for d in rev_list[1:]:
            temp.next = ListNode(d)
            temp = temp.next
        
        return sum_l
