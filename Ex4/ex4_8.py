#!/usr/bin/env python3


def solve():
    '''Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    # a + b + c = 24
    # a**2 + b**2 = c**2

    # result = []
    # for a in range(1, 11):
    #     for b in range(1, 11):
    #         for c in range(1, 11):
    #             if a + b + c == 24 and a**2 + b**2 == c**2:
    #                 result.append((a,b,c))

    result = [(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in
              range(1, 11) if (a + b + c == 24 and a**2 + b**2 == c**2)]
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
