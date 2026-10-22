class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        res = []    
        
        to obtain 0, we need a combination of negative and positive numbers, so we sort to create a split between

        start looping through nums:

            break the loop when we encounter a positive number
            
            skip the iteration if we already encountered the number

            mark left and right pointers, where l = i + 1 and r = len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    append threeSum to results
                    move left pointer left
                    move right pointer right
                    
                    move the left pointer left until different number 
        """
        
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

            


        