import unittest

def rotate_matrix(matrix_t):
    
    row_length, col_length = 0, 0
    if isinstance(matrix_t, list) and isinstance(matrix_t[0], list):
        row_length = len(matrix_t)
        col_length = len(matrix_t[0])
    else:
        return -1 #can't rotate

    if row_length != col_length:
        return -1 #can't rotate

    for layer in range(row_length//2):
        first , last = layer, row_length-1-layer
        for i in range(first, last):
            offset = i - first
            temp = matrix_t[first][i]
            matrix_t[first][i] = matrix_t[last-offset][first]
            matrix_t[last-offset][first] = matrix_t[last][last-offset]
            matrix_t[last][last-offset] = matrix_t[i][last]
            matrix_t[i][last] = temp

    return matrix_t

class rotate_matrix_Test(unittest.TestCase):

    test_data = [ [1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25] ]

    test_result = [ [21, 16, 11, 6, 1],
                    [22, 17, 12, 7, 2],
                    [23, 18, 13, 8, 3],
                    [24, 19, 14, 9, 4],
                    [25, 20, 15, 10, 5] ]
        
    
    def testing_func(self):
        self.assertEqual(rotate_matrix(self.test_data), self.test_result)
    


if __name__ == '__main__':
    unittest.main()
