class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        pascals_tri = [[1]]

        for row in range(1, numRows):
                
            row_list = []

            for col in range(0, row + 1):
                
                if col == 0 or col == row:
                    val = 1
                else:
                    val = pascals_tri[row - 1][col - 1] + pascals_tri[row - 1][col]

                row_list.append(val)

            pascals_tri.append(row_list)


        return pascals_tri
            



print(Solution().generate(7))
