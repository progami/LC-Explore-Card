class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        results = []

        if not matrix:
            return
        
        top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while top <= bottom and left <= right:

            # go right 
            for col in range(top, right + 1):
                _val = matrix[top][col]
                results.append(_val)
            # mark top row done
            top += 1
            
            # go down
            for row in range(top, bottom + 1):
                _val = matrix[row][right]
                results.append(_val)
            # mark right column done
            right -= 1
            
            # go left
            if top <= bottom:

                for col in range(right, left - 1, -1):
                    _val = matrix[bottom][col]
                    results.append(_val)
                # mark bottom row done
                bottom -= 1

            # go right
            if left <= right:
                
                for row in range(bottom, top - 1, -1):
                    _val = matrix[row][left]
                    results.append(_val)
                # mark left most column done
                left += 1

        return results

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
