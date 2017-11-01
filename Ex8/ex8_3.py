#!/usr/bin/env python3


data = ['nhung', 'bong', 'hoa', 'nho', 'va', 'nhung', 'bong', 'hoa', 'to']


def make_uppercase(iterable):
    '''Trả về list chứa các phần tử của iterable đã chuyển thành chữ HOA
    Không dùng list comprehension, for.

    Gợi ý:
        iterator, while, try/except

    :param input_data: dữ liệu sử dụng iterable
    :rtype list:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = []

    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    it = iter(iterable)
    while True:
        try:
            result.append(it.__next__().upper())
        except StopIteration as e:
            break
    return result


def solve(input_data):
    # function `solve` dành cho mục đích `test`, không cần sửa
    # Gía trị trả về của `solve` và `make_uppercase` là như nhau
    result = make_uppercase(input_data)

    return result


def main():
    words = data
    result = solve(words)
    assert isinstance(result, list)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
