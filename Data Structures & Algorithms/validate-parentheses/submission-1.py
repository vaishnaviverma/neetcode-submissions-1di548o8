class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            else:
                if i in ("]", "}", ")") and len(stack)<=0:
                    return False
                if i == "]":
                    top = stack.pop()
                    if top != "[":
                        return False
                elif i == "}":
                    top = stack.pop()
                    if top != "{":
                        return False
                if i == ")":
                    top = stack.pop()
                    if top != "(":
                        return False
        if len(stack)>0:
            return False
        return True