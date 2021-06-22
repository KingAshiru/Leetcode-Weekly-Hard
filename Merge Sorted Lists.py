from heapq import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        curr = head = ListNode(0)
        while min_heap:
            node_val, i = heappop(min_heap)
            
            curr.next = ListNode(node_val)
            curr = curr.next
            
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        return head.next
            
