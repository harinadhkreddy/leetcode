class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(1,len(nums)+1):
            dic[i]=1
        for el in nums:
            dic[el]=0
        mis = list()
        for i in dic.keys():
            if dic[i]==1:
                mis.append(i)
        return mis
        
