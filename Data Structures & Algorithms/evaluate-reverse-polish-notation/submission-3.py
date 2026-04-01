class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for val in tokens:
            if val in operands:
                rhs = int(stack.pop())
                lhs = int(stack.pop())
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
                stack.append(val)

        return int(stack[0])
            



                