class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1
        mid1 = (l1 + r1) // 2
        while l1 <= r1:
            if target < matrix[mid1][0]:
                r1 = mid1 - 1
            elif target > matrix[mid1][0]:
                l1 = mid1 + 1
            else:
                return True

            mid1 = (l1 + r1) // 2
            
        l2, r2 = 0, len(matrix[0]) - 1
        mid2 = (l2 + r2) // 2
        while l2 <= r2:
            if target < matrix[mid1][mid2]:
                r2 = mid2 - 1
            elif target > matrix[mid1][mid2]:
                l2 = mid2 + 1
            else:
                return True

            mid2 = (l2 + r2) // 2
        
        return False