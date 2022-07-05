class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = list()
        for i in range(n):
            c = i+1
            if c%3==0 and c%5==0:
                ans.append('FizzBuzz')
            elif c%3==0:
                ans.append('Fizz')
            elif c%5==0:
                ans.append('Buzz')
            else:
                ans.append(str(c))
        return ans
        
