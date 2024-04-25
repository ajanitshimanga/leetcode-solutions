class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # Output: [[7,4,1],[8,5,2],[9,6,3]]
        self._transposition(matrix)
        self._vertical_reflection(matrix)
        

    
    def _transposition(self, matrix: List[List[int]]) -> None:
        # Input     ===> Output
        # [1, 2, 3] ===> [1, 4, 7]
        # [4, 5, 6] ===> [2, 5, 8]
        # [7, 8, 9] ===> [3, 6, 9]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                # # We to do this only once for each pair of (i, j) ex.
                # If we have (0,1) we already do all the work needed for that pair. 
                # We don't want to additionally do (1, 0) since it will apply the transpose again.
                if i > j: 
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
    def _vertical_reflection(self, matrix: List[List[int]]) -> None:
        # a transposition is when the rows become columns, and the columns become rows. For example:
        #[3, 1] ===> [1, 3]
        #[4, 2] ===> [2, 4]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                column_length = len(matrix[0])
                indexable_col_len = column_length - 1
                # we want to reflect over axis = 1.
                # So the original columns need to be reflected, so we go through
                # half of the columns only, so we don't double reflect.
                # and we want to do it for every row.
                if col < column_length // 2:
                    matrix[row][col], matrix[row][indexable_col_len - col] = matrix[row][indexable_col_len - col], matrix[row][col]
