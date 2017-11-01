#!/usr/bin/env python3


def solve(numbers):
    '''Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
    '''
    assert isinstance(numbers, list)
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i
    return result


def main():
    print(solve([-1, 5, 9, 6, 2, 1]))


if __name__ == "__main__":
    main()
