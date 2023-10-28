#!/usr/bin/python3
"""valid utf8 encoding"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8
    encoding
    """
    i = 0
    # dealing with single bit characters (0b00000000 to 0b10111111)
    while i < len(data):
        if data[i] < 128:
            i += 1
        else:
            if data[i] < 192 or data[i] > 247:
                return False
            # dealing with multibyte characters
            temp = 0
            # 0b11000000 to 0b11011111
            if 192 <= data[i] <= 223:
                temp = 2
            # 0b11100000 to 0b11101111
            elif 224 <= data[i] <= 239:
                temp = 3
            # 0b11110000 to 0b11110111
            elif 240 <= data[i] <= 247:
                temp = 4
            i += 1
            for _ in range(temp - 1):
                if i >= len(data) or not (128 <= data[i] <= 191):
                    return False
                i += 1
    return True
