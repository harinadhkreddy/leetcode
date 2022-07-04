# Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list()
        tmp = 0
        for i in range(len(nums)):
            tmp+=nums[i]
            ans.append(tmp)
        return ans
