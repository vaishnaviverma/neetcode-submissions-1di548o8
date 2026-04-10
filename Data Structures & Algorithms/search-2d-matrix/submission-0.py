class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_r = len(matrix)
        n_c = len(matrix[0])
        l = 0
        h = n_r-1
        target_row=-1
        while l<=h:
            mid = l + int((h-l)/2)
            # print(mid)
            if matrix[mid][-1]>=target:
                target_row=mid
                h = mid-1
            else:
                l = mid+1
        # print(target_row)

        l = 0
        h = n_c-1
        while( l<=h):
            mid = l + int((h-l)/2)
            if matrix[target_row][mid]==target:
                return True
            elif matrix[target_row][mid]<target:
                l = mid+1
            else:
                 h=mid-1
        return False
        


        