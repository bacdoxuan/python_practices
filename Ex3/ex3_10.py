#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, and loop.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    for index in list1:
        if index in list2:
            result.append(index)

    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()
