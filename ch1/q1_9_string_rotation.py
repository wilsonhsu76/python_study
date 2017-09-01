import unittest

def check_string_rotation(str1, str2):
    if len(str1)!= len(str2):
        return False
    str1_str1 = str1 + str1  #str1:xy, str2:yx, yx should find in xyxy.
    return isSubstring(str1_str1,  str2)

def isSubstring(str_a, str_b):
    index = str_a.find(str_b)
    if index >= 0:
        return True
    else:
        return False

class check_string_rotation_Test(unittest.TestCase):
    def testing_func(self):
        self.assertEqual(check_string_rotation('waterbottle', 'erbottlewat'), True)
        self.assertEqual(check_string_rotation('waterbottle', 'erbottlewbt'), False)

if __name__ == '__main__':
    unittest.main()
