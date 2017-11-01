#!/usr/bin/env python3

import random  # NOQA
import string  # NOQA


def pass_gen(length=16):
    '''Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    all_symbol = ''.join([string.ascii_letters, string.digits,
                          string.punctuation])
    no_uppercase_letter = 0
    no_lowercase_letter = 0
    no_digit = 0
    no_punc = 0
    result = ''.join([random.choice(all_symbol) for _ in range(length)])
    condition = True
    while condition:
        for letter in result:
            if letter in string.ascii_uppercase:
                no_uppercase_letter += 1
            elif letter in string.ascii_lowercase:
                no_lowercase_letter += 1
            elif letter in string.digits:
                no_digit += 1
            elif letter in string.punctuation:
                no_punc += 1
        if no_uppercase_letter == 0 or no_lowercase_letter == 0 or no_digit \
                == 0 or no_punc == 0:
            result = ''.join([random.choice(all_symbol) for _ in range(length)])
            no_uppercase_letter = 0
            no_lowercase_letter = 0
            no_digit = 0
            no_punc = 0
            condition = True
        else:
            condition = False
    return result


def generate_and_append(length, passwords=None):
    '''
    Sinh password ngẫu nhiên và append vào list passwords.
    Nếu không có list nào được gọi với function, trả về list chứa một
    password vừa tạo ra.
    Sửa argument tùy ý.
    '''
    if passwords is None:
        passwords = []
    passwords.append(solve(length))
    return passwords


def solve(input_data):
    result = pass_gen(input_data)
    return result


def main():
    '''
    Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.
    '''
    passwords8 = generate_and_append(8)
    passwords10 = generate_and_append(10)
    passwords12 = generate_and_append(12)

    passwords12 = generate_and_append(12, passwords12)

    assert len(passwords8) == 1, passwords8
    assert len(passwords10) == 1, passwords10
    assert len(passwords12) == 2, passwords12

    for ps in passwords8, passwords10, passwords12:
        for p in ps:
            plen = len(p)
            print('Mậu khẩu tự tạo {0} ký tự của bạn là {1}'.format(plen, p))


if __name__ == "__main__":
    main()
