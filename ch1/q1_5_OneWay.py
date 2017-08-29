import unittest

def check_one_way_edit(str1, str2):
    if len(str1) == len(str2):
        return check_one_way_replace(str1, str2)
    elif (len(str1) + 1 ) == len(str2):
        return check_one_way_insert(str1, str2)
    elif (len(str1) - 1 ) == len(str2):
        return check_one_way_insert(str2, str1)
    else:
        return False

def check_one_way_replace(str1, str2):
    once_diff_flag = False
    
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if once_diff_flag == True:
                return False
            once_diff_flag = True

    return True

def check_one_way_insert(str1, str2):
    # str1 is shorter length
    index1, index2 = 0, 0
    
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True

class check_one_way_edit_Test(unittest.TestCase):
    def testing_func(self):
        self.assertEqual(check_one_way_edit('pale',  'ple'), True)
        self.assertEqual(check_one_way_edit('pales', 'pale'), True)
        self.assertEqual(check_one_way_edit('pale',  'bale'), True)
        self.assertEqual(check_one_way_edit('pale',  'bae'), False)

if __name__ == '__main__':
    unittest.main()
