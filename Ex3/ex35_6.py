#!/usr/bin/env python3


def solve(N):
    '''
    What is the sum of the digits of the number `2**1000`?
    https://projecteuler.net/problem=16
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # Sử dụng List Comprehension - Trả về 10 ký tự cuối cùng của 2 ** N
    # result = [int(index) for index in str(2 ** N)[-10:]]
    result = sum(int(index) for index in str(2 ** N))

    return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
