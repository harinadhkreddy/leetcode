class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,el in enumerate(nums):
            c = target - el
            if c in dic:
                return [dic[c],i]
            dic[el]=i
        
