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


def numberDesc(func_name):
    def encode(strs: List[str]) -> str:
        numString = ''
        for s in strs:
            numString += str(len(s)) + '#' + s

        return numString

    def decode(str: str) -> List[str]:
        stringNum = []

        word = ''
        ignoreDelimitter = False
        amountOfChar = 0

        for i in range(len(str)):
            if ignoreDelimitter:
                ignoreDelimitter = False
            elif amountOfChar > 0:
                word += str[i]
                amountOfChar -= 1
                if amountOfChar == 0:
                    stringNum.append(word)
                    word = ''
            # might break because we are looking i+1
            elif str[i].isnumeric() and str[i+1] == '#':
                amountOfChar = int(str[i])
                ignoreDelimitter = True
            else:
                raise ValueError('str is malformed')

        return stringNum

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode
