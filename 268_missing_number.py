class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)+1):
            dic[i]=1
        for num in nums:
            dic[num]=0
        for el in dic.keys():
            if dic[el]==1:
                return el
        

        
        
