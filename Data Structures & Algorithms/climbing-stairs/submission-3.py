class Solution:
    def climbStairs(self, n: int) -> int:
        visited = [-1]*n
        def check(cs):
            if cs>=n:
                if cs==n:
                    return 1
                return 0
            if visited[cs]!=-1:
                return visited[cs]
            visited[cs] = check(cs+1) + check(cs+2)
            return visited[cs]
        ans = check(0)
        return ans