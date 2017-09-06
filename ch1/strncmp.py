def strncmp(str1, str2, n):
    n = min([n,len(str1), len(str2)])
    if n == 0:
        return 0
    str1_slice = str1[0:n]
    str2_slice = str2[0:n]
    if str1_slice == str2_slice:
        return 0
    else :
        return  calc_value(str1_slice, str2_slice)

def calc_value(str1_s, str2_s):
    for i in range(len(str1_s)):
        if str1_s[i]!= str2_s[i]:
         return ord(str1_s[i]) - ord(str2_s[i])

test1 = 'ABC'
test2 = 'AbC'

print(strncmp(test1, test2, 100))
