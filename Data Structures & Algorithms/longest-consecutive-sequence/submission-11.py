class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        create a hashset and add each number to the hashset

        create a count variable
        for each number in the set:
            if num - 1 doesn't exist:
                get the max between res and current count
                reset the count to 1
            else:
                count increments
        """
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                