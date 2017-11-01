#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Viết chương trình cứ 1 giây in ra màn hình thời gian hiện tại.
- Sau N lần thì chương trình kết thúc

Gợi ý:
time.sleep, datetime.datetime.now
'''

import time
import datetime  # NOQA

import log
logger = log.get_logger(__name__)


def print_time(N):
    '''Trả về tuple chứa 2 phần tử bao gồm:
    - List chứa các điểm thời gian (string) sau N lần thực hiện
    theo yêu cầu từ ``__doc__``
    - Tổng thời gian chạy của function

    :rtype tuple:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    start = time.time()
    # NOTE: DO NOT FORMAT log by % or .format
    # http://www.familug.org/2014/09/python-logging-ung-format-log-message.html
    logger.debug("Start at %f", start)
    result = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for _ in range(N):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        result.append(current_time)
        time.sleep(1)
    end = time.time()
    logger.debug("End at %f", end)
    total_time = end - start

    return (result, total_time)


def solve(N):
    '''Học viên không cần chỉnh sửa trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    Hàm solve dùng cho mục đích `test`
    :rtype tuple:
    '''
    result = print_time(N)
    return result


def main():
    print(solve(5))


if __name__ == "__main__":
    main()
