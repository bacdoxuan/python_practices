#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Viết decorator in ra thời gian chạy của 1 function
'''

import time


def time_count(function):
    '''Tính thời gian chạy của `function` (float)
    '''
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        return end_time - start_time
    return wrapper


# Sửa tên decorator cho phù hợp
@time_count
def worker():
    for i in range(10000):
        pass
    time.sleep(1)


def solve():
    '''Thực hiện 1 tính toán bất kì trong function `solve`

    Trả về kết quả tùy ý, gán lại vào `result`
    '''
    result = worker()
    # Xoá dòng sau sau khi đã thay đổi time_count phù hợp
    return result


def main():
    print("Function worker chạy mất: {0} giây".format(solve()))


if __name__ == "__main__":
    main()
