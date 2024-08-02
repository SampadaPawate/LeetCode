class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, val in enumerate(nums):
            if target - val in targets:
                return [i, targets[target-val]]
            targets[val] = i
        
