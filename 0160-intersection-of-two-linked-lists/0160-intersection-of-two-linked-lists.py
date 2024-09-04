# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB

        count1 = 1
        while temp1 and temp1.next:
            temp1 = temp1.next
            count1 += 1

        count2 = 1
        while temp2 and temp2.next:
            temp2 = temp2.next
            count2 += 1  
        if temp1 != temp2:
            return None   

        temp1 = headA
        temp2 = headB

        if count1  < count2:
            count = count2 - count1
            for _ in range(count):
                temp2 = temp2.next
        if count1  > count2:  
            count = count1 - count2
            for _ in range(count):
                temp1 = temp1.next

        while temp1 and temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 == temp2:
                return temp1

        return None        

                                
            


        