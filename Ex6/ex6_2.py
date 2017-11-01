#!/usr/bin/env python3


def number_of_tube(iterable, N):
    # Sửa tên, set giá trị return
    return len(iterable) // N


def solve(iterable, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = [tuple(iterable[i * N: (i * N + N)])
              for i in range(number_of_tube(iterable, N))]

    return result


def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(solve(li, 2))


if __name__ == "__main__":
    main()
