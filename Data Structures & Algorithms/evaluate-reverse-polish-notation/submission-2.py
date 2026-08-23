class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())

                if token == '+':
                    stack.append(num_1 + num_2)  
                elif token == '-':
                    stack.append(num_1 - num_2)
                elif token == '*':
                    stack.append(num_1 * num_2)
                else:
                    stack.append(num_1 / num_2)
            else:
                stack.append(token)
        return int(stack[-1])