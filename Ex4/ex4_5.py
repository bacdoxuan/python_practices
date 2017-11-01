#!/usr/bin/env python3


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    sum_temp = 0
    product_temp = 1
    for i in numbers:
        sum_temp += i
        product_temp *= i
    result = (sum_temp, product_temp)
    return result


def main():
    # Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11)
    numbers = list(numbers)
    numbers.remove(0)

    print(solve(numbers))


if __name__ == "__main__":
    main()
