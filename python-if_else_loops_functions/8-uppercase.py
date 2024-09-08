#!/usr/bin/python3
def uppercase(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    print("Converted string: {}".format(result))
print('')
