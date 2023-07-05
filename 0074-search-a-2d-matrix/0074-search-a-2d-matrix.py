class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col= len(matrix),len(matrix[0])
        l,r=0,row*col-1
        while l<=r:
            mid=l+(r-l)//2
            rw,cl=mid//col,mid%col
            if matrix[rw][cl]<target:
                l=mid+1
            elif matrix[rw][cl]>target:
                r=mid-1
            else:
                return True
        return False