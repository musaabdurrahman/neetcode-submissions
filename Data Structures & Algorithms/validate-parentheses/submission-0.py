class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = True
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == "[":
                stack.append("[")
            elif i == "{":
                stack.append("{")
            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    a = False
                    break
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    a = False
                    break
            elif i == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    a = False
                    break
        return a and len(stack) == 0