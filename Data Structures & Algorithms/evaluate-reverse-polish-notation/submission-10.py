class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Keep some sort of stack that remembers the last number
        # When encountering a operation, conduct it with the last total 
        total = []
        for t in tokens:
            if t == '+':
                total.append(total.pop() + total.pop())
            elif t == '*':
                total.append(total.pop() * total.pop())
            elif t == '/':
                a, b = total.pop(), total.pop()
                total.append(int(float(b) / a))
            elif t == '-':
                a, b = total.pop(), total.pop()
                total.append(b - a)
            else: 
                total.append(int(t))
        return total[0]
