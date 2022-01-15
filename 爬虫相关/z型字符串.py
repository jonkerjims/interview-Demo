# -*- coding: utf-8 -*-
def convert( s: str, numRows: int) -> str:
    if numRows == 1: return s

    s = list(s)
    x = len(s) // numRows + 1
    # print(s)
    arr = [[0 for j in range(0,x)] for i in range(0,numRows)]
    sign = 0
    try:
        col = 0
        row = 0
        while True:

            for i in range(0, numRows):
                row = i
                sign = arr[row][col] = s.pop(0)

            while row > 1:
                col += 1
                row -= 1
                arr[row][col] = s.pop(0)
                col += 1

    except:
        print(arr)
        str = ''
        for i in range(0,numRows):
            for j in range(x):
                if arr[i][j] != 0:
                    str += arr[i][j]
        print("PAYPALISHIRING")
        print(str)


# convert("PAYPAL",3)

convert("PAYPALISHIRING",3)