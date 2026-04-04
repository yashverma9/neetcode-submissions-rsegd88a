# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # Brute force - O(k*N) - K is number of lists, N is total elements in the list
    # Space = O(1) not O(N) because we just make a new head node for result everytime
    # but just relink the existing li1 and li2 nodes in the new head. Hence O(1)
    def mergeLists(self, li1, li2):
        res = ListNode()
        resHead = res

        cur1 = li1
        cur2 = li2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                res.next = cur1
                cur1 = cur1.next
            else:
                res.next = cur2
                cur2 = cur2.next
            res = res.next

        if cur1:
            res.next = cur1
        if cur2:
            res.next = cur2
            
        return resHead.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute - sorting lists one by one

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        result = self.mergeLists(lists[0], lists[1])

        for i in range(2, len(lists)):
            result = self.mergeLists(result, lists[i])
        
        return result
            