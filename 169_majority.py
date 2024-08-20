class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c =-1
        v =0
        for el in nums:
            if v==0:
                c= el
                v=1
            else:
                if el == c:
                    v+=1
                else:
                    v-=1
        return c
        
