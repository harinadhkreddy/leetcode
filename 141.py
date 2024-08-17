# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowp = fastp = head
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if slowp == fastp:
                return True
        return False
         
