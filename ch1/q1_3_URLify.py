import unittest

def str_URLify(str_t, org_length):
    # str_t: input str. org_length: length of str_t without extensive space  
    space_cnt = 0
     
    for char_c in str_t[0:org_length]:
        if char_c == ' ':
            space_cnt+=1

    access_index = org_length + 2*space_cnt
    return_str_list = ['' for x in range(access_index)]
    
    for i in reversed(range(org_length)):
        if str_t[i] == ' ':
            return_str_list[access_index - 3: access_index] = '%20'
            access_index-=3
        else:
            return_str_list[access_index - 1] = str_t[i]
            access_index-=1
    return ''.join(return_str_list)


class URLify_Test(unittest.TestCase):

    def testing_func(self):
        self.assertEqual(str_URLify('Mr John Smith    ', 13), 'Mr%20John%20Smith')

if __name__ == '__main__':
    unittest.main()
