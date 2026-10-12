class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s != []:
            for element in s:
                if element == "(":
                    stack.append("(")
                elif element == "{":
                    stack.append("{")
                elif element == "[":
                    stack.append("[")
                elif element == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif element == "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif element == "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True
        else:
            return False