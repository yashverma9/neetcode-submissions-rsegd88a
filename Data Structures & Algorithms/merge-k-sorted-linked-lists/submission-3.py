# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    
    # Basic merge list function for 2 lists
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

        # Optimal - O(Nlogk) time: logk because every iteration we reduce the number of sorts to be done by half
        '''
            We keep halving the lists by sorting pairs till we are left with only 1 list
        '''
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            resultList = []
            for i in range(0, len(lists), 2): # We iterate in gap of 2 to group lists into pairs
                first = lists[i]
                second = lists[i+1] if i+1 < len(lists) else None # For the last pair, if 2nd is out of bound - edge case
                resultList.append(self.mergeLists(first, second))

            lists = resultList

        return lists[0]                







        