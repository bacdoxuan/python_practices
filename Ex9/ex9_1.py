import requests
import sys

"""
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``hvnsweeting``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/hvnsweeting/repos

Câu lệnh của chương trình có dạng::

  githubrepos.py username
"""


def list_repos(username):
    """
    Lay du lieu ve danh sach repo cua 1 user, tra ve 1 list cac repo cua user
    do
    input: username
    ouput: list repo
    rtype: list cac ten cua repo cua username dang string
    """
    result = []
    first_page = requests.get('https://api.github.com/users/{}/repos'
                              .format(username))
    if 'link' in first_page.headers:  # neu user co 2 trang repo tro len
        link = first_page.headers['link']
        number_of_pages = int(link[link.rfind('e=')+2:link.rfind('>')])
        base_user_link = link[1:link.find('e=')+2]
        for i in range(1, number_of_pages + 1):
            repos = requests.get('{}{}'.format(base_user_link, i))
            for repo in repos.json():
                result.append(repo['name'])
        return result
    else:  # neu user chi co 1 trang repo thi header khong co 'link'
        for repo in first_page.json():
            result.append(repo['name'])
        return result


def main():
    """
    Thuc hien chay script de lay thong tin
    """
    username = sys.argv[1]
    result = list_repos(username)
    print('Cac repo cua {} la:\n {}'.format(username, result))
    print('So repo: {}'.format(len(result)))


if __name__ == "__main__":
    main()
