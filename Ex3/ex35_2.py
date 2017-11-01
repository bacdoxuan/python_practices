#!/usr/bin/env python3


def solve(N):
    '''Creates a list which contains N random integers, each >=0, <=9

    To generate 1 random integer, use::

      import random
      random.randrange(0, 10)
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    import random
    # Cách làm cũ: Sử dụng vòng lặp và append()
    # result = []
    # index = 1
    # while index <= N:
    #     result.append(random.randrange(0, 10))
    #     index += 1

    # Cách làm mới: Sử dụng List Comprehension

    result = [random.randrange(0, 10) for index in range(1, N+1)]
    return result


def main():
    print(solve(20))


if __name__ == "__main__":
    main()
