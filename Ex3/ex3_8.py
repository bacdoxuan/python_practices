#!/usr/bin/env python3


def solve(text):
    '''Kiểm tra text có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    reversed_text = text[::-1]
    text_processed = ''.join(text.lower().strip().rstrip().split(' '))
    reversed_text_processed = ''.join(reversed_text.lower().
                                      strip().rstrip().split(' '))

    if len(text_processed) <= 1:
        result = False
    else:
        result = text_processed == reversed_text_processed

    return result


def main():
    print(solve('Able was I ere I saw Elba'))


if __name__ == "__main__":
    main()
