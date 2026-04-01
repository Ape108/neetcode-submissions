class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for val in tokens:
            if val in operands:
                rhs = stack.pop()
                lhs = stack.pop()
                if val == '+':
                    print(f"add to stack {lhs} + {rhs}")
                    stack.append(lhs + rhs)
                elif val == '-':
                    print(f"add to stack {lhs} - {rhs}")
                    stack.append(lhs - rhs)
                elif val == '*':
                    print(f"add to stack {lhs} * {rhs}")
                    stack.append(lhs * rhs)
                elif val == '/':
                    print(f"add to stack {lhs} / {rhs}")
                    stack.append(int(lhs / rhs))
                
            else:
                stack.append(int(val))

        return stack[0]
            



                