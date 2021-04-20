class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = start + (end - start) / 2
            if matrix[mid / cols][mid % cols] == target:
                return True
            elif matrix[mid / cols][mid % cols] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
