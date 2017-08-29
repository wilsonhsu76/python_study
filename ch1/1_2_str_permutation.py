import unittest

def str_permutation(str_1, str_2):
    if len(str_1)!= len(str_2):
        return False
    list_1 = list(str_1)
    list_2 = list(str_2)
    result = list_1.sort() == list_2.sort()
    return result

class str_permutation_Test(unittest.TestCase):

    def test_permutation(self):
        self.assertEqual(str_permutation('cat','act'), True)
        self.assertEqual(str_permutation('hippo ','hi opp'), True)
        self.assertEqual(str_permutation('oh oh oh oh','ho ho ho ho'), True)
        
        self.assertEqual(str_permutation('apple','apex'), False)
        self.assertEqual(str_permutation('go go go','go go g'), False)
        self.assertEqual(str_permutation('write','wr ite'), False)

if __name__ == '__main__':
    unittest.main()
