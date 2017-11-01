#!/usr/bin/env python3


def solve(N):
    '''Creates a string which contains N random ASCII letters.

    To create 1 letter, use::

      import random
      import string
      random.choice(string.ascii_letters)

    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    import random
    import string

    # Cách làm cũ
    # result = ""
    # index = 1
    # while index <= N:
    #     result += random.choice(string.ascii_letters)
    #     index += 1

    # Cách làm mới: Sử dụng List Comprehension
    result = ''.join([random.choice(string.ascii_letters) for
                      index1 in range(1, N+1)])

    return result


def main():
    print(solve(16))


if __name__ == "__main__":
    main()
