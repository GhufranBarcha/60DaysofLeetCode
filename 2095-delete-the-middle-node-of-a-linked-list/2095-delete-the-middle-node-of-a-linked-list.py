# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        middle = 1
        while temp.next:
            temp = temp.next
            middle += 1
        temp = head    
        if middle == 3:
            temp.next = temp.next.next

        if middle == 2:
            temp.next = None
            return head        
 
        if middle == 1:
            return None
        middle  = middle//2  

        temp = head 
  
      
        

        for i in range(1 , middle):
            temp = temp.next
            if i == middle - 1:
                temp.next = temp.next.next

        return head        
     




           

        