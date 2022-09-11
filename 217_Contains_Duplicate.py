#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        past_val = nums[0]
        for index, val in enumerate(nums):
            if index == 0:
                continue
            if val == past_val:
                return True
            past_val = val
        return False