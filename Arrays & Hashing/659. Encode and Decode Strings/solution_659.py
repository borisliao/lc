from typing import List


def naive(func_name):
    def encode(strs: List[str]) -> str:
        delimitter = '+'

        return delimitter.join(strs)

    def decode(str: str) -> List[str]:
        delimitter = '+'

        return str.split(delimitter)

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def literal_eval(func_name):
    def encode(strs: List[str]) -> str:
        return str(strs)

    def decode(str: str) -> List[str]:
        return eval(str)

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


# def numberDesc(func_name):
#     def encode(strs: List[str]) -> str:
#         numString = ''
#         for s in strs:
#             numString += str(len(s)) + '#' + s

#         return numString

#     def decode(str: str) -> List[str]:
#         stringNum = []

#         word = ''
#         ignoreDelimitter = False
#         amountOfChar = 0

#         for i in range(len(str)):
#             if ignoreDelimitter:
#                 ignoreDelimitter = False
#             elif amountOfChar > 0:
#                 word += str[i]
#                 amountOfChar -= 1
#                 if amountOfChar == 0:
#                     stringNum.append(word)
#                     word = ''
#             # might break because we are looking i+1
#             elif str[i].isnumeric() and str[i+1] == '#':
#                 amountOfChar = int(str[i])
#                 ignoreDelimitter = True
#             else:
#                 raise ValueError('str is malformed')

#         return stringNum

#     if func_name == 'encode':
#         return encode
#     if func_name == 'decode':
#         return decode


# def review1(func_name):
#     """
#     Anki 11-16-23
#     Used: debugger (4)
#     """
#     def encode(strs: List[str]) -> str:
#         result = ''
#         for s in strs:
#             result += str(len(s)) + '#' + s  # debugger (1,4)

#         return result  # debugger (2)

#     def decode(str: str) -> List[str]:
#         i = 0
#         result = []
#         while i < len(str)-1:  # debugger (3)
#             amount = 0
#             for s in str[i:]:
#                 if s == "#":  # debugger (5)
#                     break
#                 amount += 1
#             amount = int(str[i:amount])  # debugger (6)

#             begining_of_word = i+amount  # debugger(7)
#             end_of_word = i+2+amount
#             result.append(str[begining_of_word:end_of_word])
#             i = end_of_word

#         return result  # debugger (2)

#     if func_name == 'encode':
#         return encode
#     if func_name == 'decode':
#         return decode


def review1(func_name):
    """
    Anki 11-16-23
    Used: debugger (4), lookup solution (1)
    Time: 9 min
    """
    def encode(strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s  # debugger (1, 3)

        return result

    def decode(str: str) -> List[str]:
        i = 0
        result = []
        while i < len(str):  # debugger (2), lookup solution (1)
            start = i
            while str[i] != '#':
                i += 1
            characters = int(str[start:i])  # debugger (4)
            beginning = i+1
            end = beginning + characters
            result.append(str[beginning:end])
            i = end

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode
