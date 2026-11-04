class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                newVal = 0
                if tokens[i] == "+":
                    newVal = val2 + val1
                elif tokens[i] == "-":
                    newVal = val2 - val1
                elif tokens[i] == "*":
                    newVal = val2 * val1
                else:
                    newVal = int(val2 / val1)
                stack.append(newVal)
        return stack[0]