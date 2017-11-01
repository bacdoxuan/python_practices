#!/usr/bin/env python3

import os
import json  # NOQA


data = os.path.join(os.path.dirname(__file__), 'salt_contributors.json')


def list_user(datapath):
    '''Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, html_url và contributions.
    Nếu html_url nào bị thiếu, tạo html_url mới bằng
    "https://github.com/" + login tương ứng.
    '''
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.
    result = []
    with open(datapath, 'r') as f:
        users = json.loads(f.read())

    for user in users:
        temp_user = {}
        if 'html_url' not in user or user['html_url'] == "":
            temp_user['html_url'] = ''.join(['https://github.com/',
                                             user['login']])
        else:
            temp_user['html_url'] = user['html_url']
        temp_user['login'] = user['login']
        temp_user['contributions'] = user['contributions']
        result.append(temp_user)
    return result


def solve(input_data):
    result = list_user(input_data)

    return result


def main():
    '''Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=3 Lưu lại
    thành file salt_contributors.json.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    File đã được lưu sẵn trong thư mục này - link để đây để học viên biết
    dữ liệu lấy từ đâu.
    '''
    datafile = data

    for d in solve(datafile):
        print("User: {login} - URL {html_url} - {contributions}".format(**d))


if __name__ == "__main__":
    main()
