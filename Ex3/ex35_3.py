#!/usr/bin/env python3


def solve(N):
    '''Creates a list which contains N first even integers. ``[2, 4 ...]``
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # Cách làm cũ sử dụng vòng lặp while và append()
    # index = 1
    # result = []
    # while index <= N:
    #     result.append(index*2)
    #     index += 1

    # Cách làm mới sử dụng List Comprehension

    result = [2 * index for index in range(1, N+1)]
    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
