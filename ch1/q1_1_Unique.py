import unittest

def is_every_char_unique(str_s):
    if len(str_s) > 128: #assume srt_s only includes ASCII 128 chars
        return False
    char_list = [False for i in range(128)] 
    for char_c in str_s:
        list_index = ord(char_c)
        if char_list[list_index] is True: #check whether char_c repeats in str_s
            return False
        char_list[list_index] = True
    return True

class is_every_char_unique_Test(unittest.TestCase):
    def test_unique(self):
            self.assertEqual(is_every_char_unique('jump'), True)
            self.assertEqual(is_every_char_unique('so far'), True)
            self.assertEqual(is_every_char_unique(''), True)

            self.assertEqual(is_every_char_unique('apple'), False)
            self.assertEqual(is_every_char_unique('so good'), False)
            self.assertEqual(is_every_char_unique('xyz  abc'), False)

if __name__ == '__main__':
    unittest.main()
            
        
    
    
