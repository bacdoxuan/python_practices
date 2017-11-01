#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    assert (input_data in range(1, 13)), "Tháng không tồn tại"
    result = ("MONTH", "DATE")

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    month_day = [("January", 31), ("February", 28), ("March", 31),
                 ("April", 30), ("May", 31), ("June", 30),
                 ("July", 31), ("August", 31), ("September", 30),
                 ("October", 31), ("November", 30), ("December", 31)]

    result = month_day[input_data - 1]

    return result


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
