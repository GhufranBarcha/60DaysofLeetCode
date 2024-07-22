class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows , cols = len(matrix) ,len(matrix[0])

        r ,c = 0 , -1

        direction = 1
        arr = []

        while rows > 0 and cols > 0:

            for _ in range(cols):

                c += direction
                arr.append(matrix[r][c])
            rows -= 1    

            for _ in range(rows):

                r += direction
                arr.append(matrix[r][c])
            cols -= 1 

            direction *= -1
        return arr    

        