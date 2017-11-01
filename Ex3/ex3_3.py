#!/usr/bin/env python3

'''
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
'''


def solve():
    '''Trả về 1 `list` 100 phần tử thỏa mãn yêu cầu đề bài

    :rtype: list
    '''
    result = None

    # Xóa dòng sau và viết code vào đây set các gía trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    result = []
    i = 1
    while i < 101:
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
        i = i+1
    return result


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
