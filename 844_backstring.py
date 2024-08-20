class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackbac(s):
            sta = list()
            for el in s:
                if el == "#":
                    if sta:
                        sta.pop()
                else:
                    sta.append(el)
            return sta
        return stackbac(s) == stackbac(t)
        
