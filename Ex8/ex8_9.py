#!/usr/bin/env python3

__doc__ = '''
Yêu cầu:
- Tìm và in ra tổng số dòng của mỗi loại file (kể cả thư mục con,
dựa vào phần mở rộng abc.py và xyz.py là cùng loại) khi thực hiện lệnh:

    ex8_9.py `duong_dan_toi_thu_muc`

- Mặc định là thư mục hiện tại: PATH = '.'

Gợi ý: sử dụng `os.walk` để duyệt vào thư mục con.

Yêu cầu nâng cao:
- Trong thư mục hiện tại nếu tìm thấy file là python module
in ra màn hình tên của các function trong đó

Gợi ý: sử dụng 2 module `inspect` và `importlib`
``from inspect import isfunction``
``from importlib import import_module``
'''


import log
import os
import sys
logger = log.get_logger(__name__)
PATH = '.'


def analyze_dir(input_data):
    '''Trả về `dict` chứa tổng số dòng của từng loại file trong thư
    mục hiện tại (bao gồm cả thư mục con) theo format:

        result = {
            ".py": 1234,
            ".txt": 5678,
            ...
        }

    Lưu ý:
    - Nếu file không đọc được, gán số dòng bằng 0

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    # result can la 1 dict gom extension: so luong dong cua extension do
    result = {}
    for root, dirs, files in os.walk(input_data):
        for file in files:
            extension = file[file.rfind('.'):]
            if extension not in result:
                result[extension] = 0
            try:
                with open(os.path.join(root, file)) as f:
                    for _ in f:
                        result[extension] += 1
            except Exception:
                continue
    return result


def solve(input_data):
    '''Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    '''

    logger.debug("Statically analysing directory %s", input_data)
    result = analyze_dir(input_data)
    return result


def main():
    path = PATH  # thư mục hiện tại

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu vào biến `path`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    if len(sys.argv) == 1:  # Neu khong co tham so thi sys.argv co len = 1
        path = PATH
    else:  # Neu nguoi dung bo sung duong dan --> chua o sys.argv[1]
        path = sys.argv[1]
    print(solve(path))


if __name__ == "__main__":
    main()
