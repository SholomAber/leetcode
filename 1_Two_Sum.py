class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, val in enumerate(nums):
            for j, valTwo in enumerate(nums):
                if i != j and val + valTwo == target:
                    return [i, j]