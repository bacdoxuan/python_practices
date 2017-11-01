#!/usr/bin/env python3

'''
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
'''


def solve(input_data):
    result = None
    # Viết code vào đây set result làm kết quả của tính toán
    # Gọi số lần đi sang phải là x, số lần đi xuống dưới là y
    # Do chỉ được di chuyển sang phải, hoặc xuống dưới, nên sau khi di chuyển
    # từ góc trên bên trái đến góc dưới bên phải thì x = n và y = n.
    # Bài toán chuyển về sắp xếp n phần tử x và n phần tử y vào 1 dãy 2n ô
    # trống, không phân biệt về thứ tự sắp xếp --> tổ hợp chập n của 2n phần
    # tử. Đáp án chung là (2*n)!/n!/n!
    from math import factorial as F
    result = int(F(input_data*2) / F(input_data) / F(input_data))
    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
