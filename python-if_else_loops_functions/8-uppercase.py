#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if '97' <= i <= '122':
            result += i - 32
        else:
            result += i
    print(result)
