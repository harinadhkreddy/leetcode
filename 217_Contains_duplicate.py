class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for el in nums:
            if dic.get(el,None):
                return True
            else:
                dic[el]=1
        return False
