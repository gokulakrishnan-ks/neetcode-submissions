class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index in range(len(nums)):
            print(nums[index])
            if target - nums[index] in indices:
                return [indices[target - nums[index]], index]
            
            indices[nums[index]] = index