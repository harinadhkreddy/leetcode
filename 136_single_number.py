class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sing = nums[0]
        for el in nums[1:]:
            sing = sing^el
        return sing
