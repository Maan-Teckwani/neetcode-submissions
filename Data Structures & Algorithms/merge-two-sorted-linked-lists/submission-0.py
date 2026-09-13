# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        vals=[]
        while list1!=None:
            vals.append(list1.val)
            list1=list1.next
        while list2!=None:
            vals.append(list2.val)
            list2=list2.next
        vals.sort()
        print(vals)
        for i in range(len(vals)):
            if i==0:
                head=ListNode(vals[i])
                curr=head
                continue
            tmp=ListNode(vals[i])
            curr.next=tmp
            curr=tmp
        return head
            
        
        