#!/usr/bin/env python3

data = {'first_50': 1230, 'from_51_to_100': 1530, 'above_100': 1786}


def calculate_cost(usage, prices):
    '''Tính tiền điện (integer)
    với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
    '''
    # Viết code tính toán vào đây
    price_50 = 50 * prices['first_50']
    price_100 = price_50 + 50 * prices['from_51_to_100']
    usage = int(usage)
    if usage < 51:
        return usage * prices['first_50']
    elif usage < 101:
        return price_50 + (usage - 50) * prices['from_51_to_100']
    else:
        return price_100 + (usage - 100) * prices['above_100']


def solve(input_data):
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # Bài này làm mẫu, gọi function học viên định nghĩa với input để
    # tính kết quả.
    # Các bài còn lại học viên tự định nghĩa function và gọi function để
    # tính toán kết quả `result`
    result = [(i[0].title(), calculate_cost(i[1], input_data['prices']))
              for i in input_data['usages']]

    return result


def main():
    '''
    Cho tiền điện sinh hoạt được tính theo công thức:

    - 50 số đầu: 1230 VND/số.
    - 50 số tiếp: 1530 VND/số.
    - Các số tiếp theo: 1786 VND/số.
    '''
    idata = {'usages': [('nam', '1'), ('pikalong', '29'),
                        ('phan quan', '1235'), ('maria', '69'),
                        ('trump', '100')],
             'prices': data}
    print(solve(idata))


if __name__ == "__main__":
    main()
