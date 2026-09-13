# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        nodes=[]
        while cur:
            nodes.append(cur)
            cur=cur.next
        dummy=curr=ListNode()
        for i in range(len(nodes)):
            if i==len(nodes)-n:
                continue
            curr.next=nodes[i]
            curr=curr.next
        curr.next=None
        return dummy.next
        
        