#!/usr/bin/env python3


def solve(N):
    '''Creates a list like this by listcomps::

      ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN]

    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # Sử dụng List Comprehension
    result = [str(index)*6 for index in range(1, N+1)]
    return result


def main():
    print(solve(11))


if __name__ == "__main__":
    main()
