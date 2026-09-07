class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        validS = []
        i = 0;
        for c in s:
            if c == "(":
                validS.append(c)
                i += 1
            elif c== ")" and i > 0:
                validS.append(c)
                i -= 1
            elif c != ')':
                validS.append(c)

        filtered = [] 
        for c in reversed(validS):
            if c == "(" and i > 0:
                i -= 1
            else: 
                filtered.append(c)
        return "".join(reversed(filtered))
                
            
