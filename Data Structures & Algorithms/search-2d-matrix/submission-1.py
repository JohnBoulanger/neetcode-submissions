class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, h = 0, len(matrix) - 1
        rowLength = len(matrix[0])
        row = -1
        
        # find potential row first
        while l <= h:
            mid = (l + h) // 2
            lowRow = matrix[mid][0]
            highRow = matrix[mid][rowLength - 1]
            # target within the range of the current row
            if target >= lowRow and target <= highRow:
                row = mid
                break
            elif target < lowRow:
                h = mid - 1
            else:
                l = mid + 1

        if row == -1:
            return False
        
        # row found if we reach here, binary search on the row
        l, r = 0, rowLength - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False


        