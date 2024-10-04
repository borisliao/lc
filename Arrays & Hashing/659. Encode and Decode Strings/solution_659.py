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


def review2(func_name):
    """
    Anki 11-18-23
    Time: ~20 min
    """
    def encode(strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(str: str) -> List[str]:
        result = []
        i = 0
        start = 0
        while i < len(str):
            if str[i] == '#':
                amount = int(str[start:i])
                word_beginning = i + 1
                word_end = word_beginning + amount
                result.append(str[word_beginning: word_end])
                i = word_end
                start = word_end
            else:
                i += 1
        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def neetcode_solution(func_name):
    """
    https://www.youtube.com/watch?v=B1k_sxOSgv8
    """
    def encode(strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review3(func_name):
    """
    Review 11-27-23
    Used: debugger (1)
    """
    def encode(strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s  # 1d

        return result

    def decode(str: str) -> List[str]:
        result = []
        i = 0
        while i < len(str):
            num = ''
            while str[i] != '#':
                num += str[i]
                i += 1

            result.append(str[i + 1: i + 1 + int(num)])
            i += 1 + int(num)

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review4(func_name):
    """
    Anki 12-10-23
    Used: debugger (2)
    Time: 24:55
    """
    def encode(strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f'{len(s)}#{s}'
        return result

    def decode(str: str) -> List[str]:
        result = []

        i = 0
        while i < len(str):
            num = ''

            while str[i] != '#':
                num += str[i]
                i += 1

            result.append(str[i + 1:i + 1 + int(num)])  # d2
            i += 1 + int(num)  # d1

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review4(func_name):
    """
    Anki 12-27-23
    Time: 16 min
    Used: debugger 4
    """
    def encode(strs: list[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s  # d1 forgot str()

        return result  # d2 forgot return

    def decode(str: str) -> list[str]:
        i = 0
        amount = ''
        result = []

        while i < len(str):
            if str[i] == '#':
                # d4 add i in i+int(amount)+1
                result.append(str[i+1:i+int(amount)+1])
                i += int(amount)+1
                amount = ''  # d3
            else:
                amount += str[i]
                i += 1

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review5(func_name):
    """
    Anki 1-19-24
    """
    def encode(strs: list[str]) -> str:
        result = ''
        for s in strs:
            result += f'{len(s)}#{s}'
        return result

    def decode(str: str) -> list[str]:
        i = 0
        str_num = ''
        result = []
        while i < len(str):
            if str[i] == '#':
                num = int(str_num)  # d2 str()
                result.append(str[i+1:i+1+num])
                i += 1+num
                str_num = ''  # s3
            else:
                str_num += str[i]
                i += 1  # d1

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review6(func_name):
    """
    Anki 3-7-24
    Time: 14:44
    Used: Solution 1
    """
    def encode(strs: list[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return ''.join(result)

    def decode(str: str) -> list[str]:
        result = []
        num = ''
        i = 0
        while i < len(str):
            if str[i] != '#':
                num += str[i]
                i += 1
            else:
                val = int(num)
                result.append(str[i+1:i+1+val])  # s1 +1 +1+val
                i += val + 1
                num = ''

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode


def review7(func_name):
    """
    Mochi 10-4-24
    """

    # issue is determining when a element ends
    # put a delimiter: len(element)#
    def encode(strs: list[str]) -> str:
        result = ''

        for e in strs:
            result += str(len(e)) + '#' + e

        return result

    # identify the the number based on when you see the delimiter
    # inc based on how the number in the str.
    # make sure we skip the delimiter
    def decode(str: str) -> list[str]:
        result = []
        numStr = ''

        # l = 1
        # r = 1+3+1
        # 3#abc
        l = 0
        while l < len(str):
            if str[l] == '#':
                r = l+int(numStr)+1
                result.append(str[l+1:r])
                l = r
                numStr = ''  # s1
            else:  # gpt2
                numStr += str[l]
                l += 1

        return result

    if func_name == 'encode':
        return encode
    if func_name == 'decode':
        return decode

# def review8(func_name):
#     """
#     Anki 10-4-24
#     """
#     def encode(strs: list[str]) -> str:

#     def decode(str: str) -> list[str]:

#     if func_name == 'encode':
#         return encode
#     if func_name == 'decode':
#         return decode
