class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mRight = len(matrix) -1 # 0
        nRight = len(matrix[0]) -1 # 0
        mLeft = 0
        nLeft = 0
        midRow = int(mRight/2) #1
        midCol = int(nRight/2) #2
        

        while mLeft < mRight and midRow + 1 <= len(matrix):
            if target >= matrix[midRow][0] and target < matrix[midRow+1][0]:
                break
            if target < matrix[midRow][0]:
                mRight = midRow
            else:
                mLeft = midRow + 1

            midRow = int((mLeft + mRight) /2)

        while nLeft < nRight :
            if target == matrix[midRow][midCol]:
                return True
            if target < matrix[midRow][midCol]:
                nRight = midCol - 1
            else:
                nLeft = midCol + 1

            midCol = int((nLeft + nRight) /2)

        return matrix[midRow][midCol] == target









