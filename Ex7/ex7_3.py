#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Lưu file ``https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls`` về máy với tên event.yaml

- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

- Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
  thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
  thêm tại đây:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
'''  # NOQA


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA


def read_write():
    '''Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    file_path = os.path.join(os.path.dirname(__file__), 'event.yaml')
    with open(file_path, 'r') as f:
        data = yaml.load(f.read())

    print(len(data))
    print_size('event.yaml')

    json_data = json.dumps(data)
    with open(os.path.join(os.path.dirname(__file__), 'event.json'), 'w') as f:
        f.write(json_data)

    print_size('event.json')

    pickle_data = pickle.dumps(data)
    with open(os.path.join(os.path.dirname(__file__), 'event.pkl'), 'wb') as f:
        f.write(pickle_data)

    print_size('event.pkl')
    return data


def print_size(filename):
    path_file = os.path.join(os.path.dirname(__file__), filename)
    print(os.stat(path_file).st_size)


def solve():
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    '''
    result = read_write()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
