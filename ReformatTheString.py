# 1417. Reformat The String
class Solution:
    def reformat(self, s: str) -> str:
        alpha, num = "", ""
        for c in s:
            if c.isalpha() and not c.isnumeric(): alpha+=c
            else: num += c
        if abs(len(num)-len(alpha))>=2: return ""
        temp = ""
        if len(num)>=len(alpha):
            for i,j in zip(num, alpha):
                temp += i+j
            if len(num)-len(alpha)==1:
                temp += num[-1]
        else:
            for i,j in zip(alpha, num):
                temp += i+j
            if len(num)-len(alpha)==-1:
                temp += alpha[-1]
        return temp