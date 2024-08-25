# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return None
        if head.next == None and head:
            return True      
        arr = []    
        temp = head
        arr.append(temp.val)
        

        while True:
            
            temp = temp.next
            arr.append(temp.val)
            if not temp.next:
                break

        if arr == arr[::-1]:
            return True
        else:
            return False        




        