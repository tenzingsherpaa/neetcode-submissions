class Solution:
    def isValid(self, s: str) -> bool:
        
    # Every open bracket is closed by the same type
    # Input Args: Str s
    # Will string always have values? 
    # Constraint 1 <= len(s) <= 1000
    # Return: bool true for if it's valid

        stack = []
        closeToOpen = { ")": "(", "]":"[", "}":"{"}
       
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
            