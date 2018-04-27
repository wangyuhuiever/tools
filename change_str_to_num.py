# -*- coding: utf-8 -*-


def inverse(string):
    '''
    :param string:
    :return:number

    输入一个英文字母，转化成excel列对应的数字
    '''
    single_string = [s.upper() for s in string]

    def _add27(string_list):
        string_length = len(string_list)
        if string_length > 0:
            if string_length == 1:
                number = ord(string_list[0]) % 64
            else:
                number = 0
                i = 0
                while i < len(string_list):
                    number += (_add27([string_list[i]]) % 27) * (26 ** (string_length - i - 1))
                    i += 1
            return number
    num = _add27(single_string)
    return num

