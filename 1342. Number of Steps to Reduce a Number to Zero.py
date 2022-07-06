#1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        n = num
        while(n):
            if n%2 :
                n=n-1
                ans+=1
            else:
                n=n//2
                ans+=1
        return ans
        
