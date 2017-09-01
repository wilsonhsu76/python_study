import unittest

def fill_zeros_in_martix(matrix_t):
    if  not isinstance(matrix_t, list) or  not isinstance(matrix_t[0], list):
        return -1 #not matrix case
    row_length = len(matrix_t)
    col_length = len(matrix_t[0])
    row_toZeros_list = [False for x in range(row_length)]
    col_toZeros_list = [False for x in range(col_length)]

    for i in range(row_length):
        for j in range(col_length):
            if matrix_t[i][j] == 0:
                row_toZeros_list[i] = True
                col_toZeros_list[j] = True

    for i in range(row_length):
        if row_toZeros_list[i] == True:
            null_row(matrix_t, i)

    for j in range(col_length):
        if col_toZeros_list[j] == True:
            null_col(matrix_t, j)

    return matrix_t

def null_row(matrix_t, row_num):
    for j in range(len(matrix_t[0])):
        matrix_t[row_num][j] = 0

def null_col(matrix_t, col_num):
    for i in range(len(matrix_t)):
        matrix_t[i][col_num] = 0

class fill_zeros_in_martix_Test(unittest.TestCase):

    test_data = [ [1, 0, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 0, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25] ]

    test_result = [ [0, 0, 0, 0, 0],
                    [6, 0, 8, 0, 10],
                    [0, 0, 0, 0, 0],
                    [16, 0, 18, 0, 20],
                    [21, 0, 23, 0, 25] ]


    def testing_func(self):
        self.assertEqual(fill_zeros_in_martix(self.test_data), self.test_result)

if __name__ == '__main__':
    unittest.main()


        
