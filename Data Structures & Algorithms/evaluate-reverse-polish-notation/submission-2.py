class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i.lstrip('-').isnumeric():
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()
                if i == '+':
                    ans = first+second
                elif i == '-':
                    ans = first-second
                elif i == '/':
                    ans = int(first/second)
                else:
                    ans = first*second
                stack.append(ans)
        final_ans = stack.pop()
        return final_ans