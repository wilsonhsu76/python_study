import unittest

def str_compression(str_t):

    return_str_list = []
    repeat_char_count = 0

    for i in range(len(str_t)):
        repeat_char_count += 1
        if (i+1) >= len(str_t) or str_t[i] != str_t[i+1]:
            return_str_list.append(str_t[i])
            return_str_list.append(str(repeat_char_count))
            repeat_char_count = 0
            
    return  min(''.join(return_str_list), str_t, key=len )

class  str_compression_Test(unittest.TestCase):
    def testing_func(self):
        self.assertEqual(str_compression('aabcccccaaa'),'a2b1c5a3')
        self.assertEqual(str_compression('xxxxxxxxxx'),'x10')

if __name__ == '__main__':
    unittest.main()
