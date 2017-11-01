#!/usr/bin/env python3
import log
import datetime
from datetime import date
import sys
logger = log.get_logger(__name__)

__doc__ = '''
Viết script get_version nhận vào ngày ở format <month>/<day>/<year>.
VD: 03/28/16 làm parameter và in ra một version được tính theo quy luật sau:
- Version ở dạng format: <MAJOR>.<MINOR>.<PATCH>, vd: "6.9.2"
- Cách đánh version này gọi là semver http://semver.org/
- Từ ngày 09 tháng 02 năm 2016, phiên bản bắt đầu là "1.0.0"
- Mỗi 28 ngày, MAJOR lại tăng thêm 1, MINOR và PATCH set về 0
- Mỗi 7 ngày, MINOR tăng thêm 1 và PATCH sẽ set về 0
- Cứ mỗi ngày, PATCH lại tăng thêm 1.

In ra phiên bản tương ứng.

Gợi ý: học viên sử dụng `sys.argv` hoặc module `argparse`
'''

# Tim ngay bat dau version 0.0.0. Ngay 2016/02/09 la version 1.0.0
date_v0 = date(2016, 2, 9) - datetime.timedelta(28)


def change_date_format(input_data):
    '''
    input_data = "<month>/<day>/<year>"
    output_data = (year, month, day)
    rtype = tuple gom thong tin year, month, day dang int
    '''
    new_format = ''.join(['20', input_data[-2:], '/', input_data[:-3]])
    year = int(new_format[:4])
    month = int(new_format[5:7])
    day = int(new_format[-2:])
    return (year, month, day)


def find_version(input_data):
    '''Trả về tên phiên bản như yêu cầu tại ``__doc__``

    :param input_data: ngày format ở dạng <month>/<day>/<year>,
                       ví dụ: "02/03/16"
    :rtype str:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    # Thay doi thong tin dau input data sang dang tuple (year, month, day)
    ymd = change_date_format(input_data)
    # Tim so ngay chenh lech giua input_data voi ngay bat dau verion 0.0.0
    no_days = (date(ymd[0], ymd[1], ymd[2]) - date_v0).days

    # Tinh toan ra version theo ngay nhap vao
    if no_days >= 28:
        major = no_days // 28
        if no_days % 28 >= 7:
            minor = (no_days % 28) // 7
            patch = (no_days % 28) % 7
        else:
            minor = no_days % 28
            patch = 0
    else:
        major = 0
        if no_days >= 7:
            minor = no_days // 7
            patch = no_days % 7
        else:
            minor = 0
            patch = no_days

    result = '.'.join([str(major), str(minor), str(patch)])
    return result


def solve(input_data):

    '''Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `find_version` là như nhau

    :rtype str:
    '''
    result = find_version(input_data)
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return result


def main():
    input_data = sys.argv[1]
    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu
    # vào biến `input_data`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    logger.debug("Getting version for the day %s", input_data)
    print(input_data, solve(input_data))

    for d in "02/03/16", "09/06/16", "06/23/17":
        print(d, solve(d))


if __name__ == "__main__":
    main()
