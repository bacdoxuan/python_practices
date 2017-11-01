#!/usr/bin/env python3


def solve(*args, **kwargs):
    '''Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    import os
    import sys
    no_lines = 0
    with open(os.__file__, 'r') as f:
        for line in f:
            no_lines += 1
    result = (os.__file__, dir(os) + dir(sys), no_lines)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
