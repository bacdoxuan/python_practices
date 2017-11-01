#!/usr/bin/env python3


def solve(N):
    '''Create a list which contains N elements 2'''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # Cách cũ: Sử dụng vòng lặp và append
    # index = 1
    # while index < N+1:
    #     result.append(2)
    #     index += 1

    # Cách mới: Sử dụng List Comprehension
    result = [2 for index in range(1, N+1)]

    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
