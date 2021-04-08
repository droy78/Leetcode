# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1

        # At this point, start is one more than end
        # end points to the last good version
        # start points to the first bad version
        return start
