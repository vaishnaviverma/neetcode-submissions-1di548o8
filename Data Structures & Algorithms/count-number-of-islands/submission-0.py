class Solution:
    def check(self, k, l, grid):
        if k not in range(len(grid)) or l not in range(len(grid[0])):
            return 
        if grid[k][l]=="0":
            return
        grid[k][l]="0"
        self.check(k+1,l,grid)
        self.check(k,l+1,grid)
        self.check(k-1,l,grid)
        self.check(k,l-1,grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        b = len(grid[0])
        count = 0
        for i in range(h):
            for j in range(b):
                if grid[i][j]=="1":
                    count+=1
                    self.check(i,j,grid)
        return count