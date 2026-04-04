class Solution:
    def findMedian(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums)%2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2)+1])/2
        else:
            return nums[len(nums)//2]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Optimal
        '''
            Instead of merging and storing them, we need to find 2 partitions left and right 
            in both the arrays such that the last element of 1st left partition should be
            smaller than the first element of 2nd right partition and last element of 2nd
            left partition should be smaller than first element of 1st right partition

            This way left1 + left2 and right1 + right2 gives us the accurate left and right
            partition of the merged array eventually. Fod odd total elements, median will be last
            element of left partition and for even the avg of last left and first right element

            We use binary search to arrive at the partitions
        '''

        # When either are empty / both are empty case
        len1 = len(nums1)
        len2 = len(nums2)

        A, B = nums1, nums2

        if len2< len1:
            A, B = B, A # Swap to make A the shortest array
        
        total = len1 + len2
        half = total//2
        l = 0
        r = len(A) - 1

        while True:
            leftPartA = (l+r)//2
            leftPartB = half - leftPartA - 2

            leftA = A[leftPartA] if leftPartA >= 0 else float('-inf')
            leftB = B[leftPartB] if leftPartB >= 0 else float('-inf')
            rightA = A[leftPartA + 1] if leftPartA < len(A)-1 else float('inf')
            rightB = B[leftPartB + 1] if leftPartB < len(B)-1 else float('inf')

            if leftA <= rightB and leftB <= rightA:
                break
            elif leftA > rightB:
                r = leftPartA - 1
            else:
                l = leftPartA + 1
            
        
        if total % 2 == 0:
            median = (max(leftA, leftB) + min(rightA, rightB))/2
        else:
            median = min(rightA, rightB)
        
        return median