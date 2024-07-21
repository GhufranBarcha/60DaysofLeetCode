class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        x = len(matrix)
        y = len(matrix[0])

        i_arr = []
        j_arr = []

        for i in range(x):
            for j in range(y):
                print(i,j)
                if matrix[i][j] == 0:
                    i_arr.append(i)
                    j_arr.append(j)


        for i in range(x):
            for j in range(y):
                if i in i_arr:
                    matrix[i][j] = 0
                if j in j_arr:
                    matrix[i][j] = 0
        