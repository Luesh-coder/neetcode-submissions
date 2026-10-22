class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        backtracking

        define a recursive function dfs(i, currentList, total) where:
            - i is the current index in nums
            - currentList is the current combination begin built
            - total is the sum of numbers in currentList
        
        if total == target, add a copy of currentList to the result and return

        if i goes out of bounds or total exceeds the target, return (stop exploring)

        choose to include nums[i]:
            Add nums[i] to currentList
            Call dfs(i , currentList, total + nums[i])
            Remove nums[i]

        Choose to skip nums[i]:
            call dfs(i + 1, currentList, total)
        
        Start with dfs(0, [], 0) and return the result list
        """
        res = []
        def dfs(i , cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return 

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res