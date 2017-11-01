#!/usr/bin/env python3

__doc__ = '''
Chuẩn bị cho buổi sau
---------------------

- Cài đặt `requests`, `BeautifulSoup4` lên máy:
http://docs.python-requests.org/en/latest/user/install/#install
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

Chú ý cách đọc docstring của function:
--------------------------------------

- :rtype abc: kiểu dữ liệu trả về của function là `abc`
- :param name: phần mô tả cho argument `name` truyền vào function

Từ bài này, thay vì dùng print, ta sẽ dùng logging để ghi lại "nhật ký" (log)
của chương trình.
'''


def main():
    print(__doc__)


if __name__ == "__main__":
    main()
