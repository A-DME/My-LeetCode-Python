"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

example...

Input: l1 = [2,4,3], l2 = [5,6,4].........(l1: 2-->4-->3, l2: 5-->6-->4)
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2='',''
        while l1 :
            s1 += str(l1.val)
            l1 = l1.next

        while l2 :
            s2 += str(l2.val)
            l2 = l2.next


        res=str(int(s1[::-1])+int(s2[::-1]))
        
        l3= ListNode() # a dummy head with value 0
        l3res= l3 # to refer to the dummy head of the list
        for digit in res[::-1]:
            l3.next= ListNode(int(digit)) # inserting digits in reverse order
            l3= l3.next

        return l3res.next
