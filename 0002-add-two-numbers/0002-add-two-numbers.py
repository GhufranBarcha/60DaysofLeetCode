# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        tail = dummyhead
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + carry

            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        result = dummyhead.next
        return result    

        ## My approch works but not optimal
        # num1 = l1
        # num2 = l2

        # val1 = ""
        # val2 = ""
        # while num1 and num1.next:
        #     val1 = str(num1.val) + val1
        #     num1 = num1.next
        # val1 = str(num1.val) + val1    
        # while num2 and num2.next:
        #     val2 = str(num2.val) + val2
        #     num2 = num2.next
        # val2 = str(num2.val) + val2   

        # sum1 = str(int(val1) + int(val2))
        # dummynode = ListNode(0)
        # temp = dummynode
        # for i in sum1[::-1]:
        #     prev = temp
        #     temp.val = int(i)
        #     temp.next = ListNode(0)
        #     temp = temp.next
            
        # prev.next = None    
        # print(dummynode)
        # return dummynode
            
        