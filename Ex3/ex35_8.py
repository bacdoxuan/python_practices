#!/usr/bin/env python3


def solve(N):
    '''Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    '''
    Cách thực hiện sinh matrix như bên dưới sẽ sinh ra các list [1,..,9]
    trong matrix có cùng id, dẫn đến khi thay đổi 1 giá trị trong matrix theo
    cách matrix[i][j] = '@' sẽ đổi toàn bộ các vị trí [j] trong các list
    [1,..,9] thành '@' theo, chứ không phải thay đổi chỉ mỗi vị trí
    matrix[i][j]

    Không tin chạy thử xem:

    row = [index1 for index1 in range(N)]
    matrix = [row for index2 in range(N)]

    print(matrix)

    for row_i in range(N):
        for col_i in range(N):
            if row_i == col_i or matrix[row_i][col_i] == N - 1 - row_i:
                matrix[row_i][col_i] = str(row_i)
            else:
                matrix[row_i][col_i] = "*"

    result = '\n'.join([''.join(line_i) for line_i in matrix])
    return result
    '''

    matrix = [[index1 for index1 in range(N)] for index2 in range(N)]
    # print(matrix)

    for row_i in range(N):
        for col_i in range(N):
            if row_i == col_i or matrix[row_i][col_i] == N - 1 - row_i:
                matrix[row_i][col_i] = str(row_i)
            else:
                matrix[row_i][col_i] = "*"

    result = '\n'.join([''.join(line_i) for line_i in matrix])
    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
