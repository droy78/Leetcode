class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(nums) - 1

        # Find the first (leftmost) position of the target
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid + 1
            else:  # nums[mid] >= target
                end = mid - 1

        # At this point, if target exists in sorted array, then start index points to the first appearance
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        first = start

        # Now do a second binary search to find the last (rightmost) position of the target
        # start need not change
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid + 1
            else:  # nusm[mid] > target
                end = mid - 1

        # At this point, end index points to the last appearance of the target
        return [first, end]
