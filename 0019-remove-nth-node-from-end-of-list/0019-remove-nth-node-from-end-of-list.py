# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return None    
      

         


        first = head
        second = head

        for i in range(n):
            second = second.next

        while second and second.next:
            first = first.next
            second = second.next

        if first.next and first.next.next:
            first.next = first.next.next
        else:
            first.next = None

        return head    



      
