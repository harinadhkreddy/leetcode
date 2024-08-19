class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = 0
        for i in range(len(nums)):
            if nums[i]<0:
                n=i
        p = n+1
        sq = list()
        while(n>=0 or p<len(nums)):
            if (n>=0 and p<len(nums)):
                ns = nums[n]**2
                ps = nums[p]**2
                if ns > ps:
                    sq.append(ps)
                    p=p+1
                else:
                    sq.append(ns)
                    n=n-1
            elif(n>=0):
                sq.append(nums[n]**2)
                n=n-1
            elif(p<len(nums)):
                sq.append(nums[p]**2)
                p=p+1
        return sq


        
