class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        sort nums

        define a recursive function dfs(i, currentList, total):
            if total == target:
                add copy of currentList to result
                return
            loop j from i to end of list:
                if total + nums[j] > target, stop the loop (no need to check larger numbers)
                add nums[j] to current list
                call dfs(j, currentList, total + nums[j])
                Remove last element to backtrack
        start recursion with dfs(0, [], 0)
        return res
        """

        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return 
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res