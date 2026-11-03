class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary Search:

        for loop to go through every row, checking if the target is within the bounds of row

        if true:
            binary search the row
            if found:
                return true
            else:
                return false

        if it iterates through for loop, return False
        """

        for row in matrix:
            curr = row
            l, r = 0, len(curr) - 1
            if target >= curr[l] and target <= curr[r]:
                while l <= r:
                    m = l + ((r - l) // 2)
                    if curr[m] < target:
                        l = m + 1
                    elif curr[m] > target:
                        r = m - 1
                    else:
                        return True
        return False