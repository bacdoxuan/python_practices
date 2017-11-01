#!/usr/bin/env python3


def solve(N):
    '''Calculates sum of a list contains all integers less than N,
    which are multiple of 3 or 5.

    Given `sum` function:
    >>>  sum([1,2,3,4]) == 10
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    # list_1 = [i for i in range(N)]
    # result = 0
    # for index in list_1:
    #     if index % 3 == 0 or index % 5 == 0:
    #         result += index

    result = sum(i for i in range(N) if i % 3 == 0 or i % 5 == 0)
    return result


def main():
    '''Nhập 1 số nguyên đầu vào và tính
    Ví du: Bạn hãy nhập 1 số:
    Điền 10
    Kết quả ra 23
    '''
    print("Bạn hãy nhập vào 1 số nguyên lớn hơn 1:")
    input_data = int(input())
    print("Kết quả tính toán là:")
    print(solve(input_data))


if __name__ == "__main__":
    main()
