import unittest

def check_palindrome_permutation(str_t):
    char_table = [0 for x in range(ord('z') - ord('a') + 1)]
    odd_count = 0 #How many values are odd in table

    for char_c in str_t:
        index = mapping_func(char_c)
        if index != -1:
            char_table[index] += 1
            if (char_table[index] % 2):
                odd_count += 1
            else:
                odd_count -= 1
    return odd_count <= 1

def mapping_func(c):
    value = ord(c)
    value_a = ord('a')
    value_z = ord('z')
    value_A = ord('A')
    value_Z = ord('Z')
    
    if value_a <= value <= value_z:
        return value - value_a
    elif value_A <= value <= value_Z:
        return value - value_A
    else:
        return -1

class check_palindrome_permutation_Test(unittest.TestCase):
    def testing_func(self):
        self.assertEqual(check_palindrome_permutation('Tact Coa'), True)
        self.assertEqual(check_palindrome_permutation('sgs gy% ygZz'), True)
        self.assertEqual(check_palindrome_permutation('sktg tt ytzz'), False)
        self.assertEqual(check_palindrome_permutation('sktg jtgs'), False)

if __name__ == '__main__':
    unittest.main()
