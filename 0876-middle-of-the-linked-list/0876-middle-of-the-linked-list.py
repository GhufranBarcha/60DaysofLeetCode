# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        temp = head
        count = 1

        while temp.next:
            temp = temp.next
            count += 1

        if count % 2 == 0:
            count = int(count/2) + 1
        else:
            count = int(count/2) + 1
    
        for _ in range(count-1):
            head = head.next
        return head    

        