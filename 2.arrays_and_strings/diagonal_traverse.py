class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        def initial_coordinates(diagonal: int, direction_flag: int) -> tuple[int, int]:
            
            if direction_flag == 0:
            # even diagonal
                start_row = min(diagonal, m-1) 
                start_col = diagonal - start_row 
            else:  # odd diagonal
                start_col = min(diagonal, n-1)
                start_row = diagonal - start_col
            
            return start_row, start_col
                

        m, n = len(mat), len(mat[0])
        res = []
        num_diagonals = m + n - 1
        direction_flag = 0 # start with even diagonal

        for diagonal in range(num_diagonals):
            
            # determine if even or odd diagonal
            row, col = initial_coordinates(diagonal, direction_flag)

            while (0 <= row < m) and (0 <= col < n):
                
                # traverse diagonals
                res.append(mat[row][col])
                
                if direction_flag == 0: # even diagonal
                    row -= 1
                    col += 1
                
                else: # odd diagonal
                    row += 1
                    col -= 1


            # reverse direction
            direction_flag = 1 - direction_flag

        return res
            

print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
