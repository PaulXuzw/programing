# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        p = l3
        flag = 0
        while l1 and l2:
            sum = l1.val + l2.val + flag
            flag = sum//10
            value = sum % 10
            p.val = value
            p.next = l1.next
            l1 = l1.next
            l2 = l2.next
            pre = p
            p = p.next
        if l1 == None and l2 == None and flag == 1:
            p =ListNode(1)
            pre.next = p
        while l1:
            sum = l1.val+flag
            flag = sum//10
            value = sum%10
            p.val = value
            p.next = l1.next
            l1 = l1.next
            pre = p
            p = p.next
        while l2:
            sum = l2.val+flag
            flag = sum//10
            value = sum%10
            p = ListNode(value)
            #print(p.val)
            pre.next = p
            pre = p
            l2 = l2.next
        if flag == 1:
            p = ListNode(1)
            pre.next=p
        return l3
            
