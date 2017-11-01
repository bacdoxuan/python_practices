import requests
import bs4
import argparse

'''
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]
'''


def layketqua():
    """
    Lấy kết quả các giải đặc biệt đến giải bay từ trang ketqua.net
    input: http://ketqua.net
    :rtype: dict chứa các list chứa các giải xổ số
    """
    r = requests.get('http://ketqua.net')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    td = soup.find_all('td')
    result = {}
    result['Giai dac biet'] = [td[2].string]
    result['Giai nhat'] = [td[4].string]
    result['Giai nhi'] = [td[i].string for i in (6, 7)]
    result['Giai ba'] = [td[i].string for i in (9, 10, 11, 13, 14, 15)]
    result['Giai tu'] = [td[i].string for i in (17, 18, 19, 20)]
    result['Giai nam'] = [td[i].string for i in (22, 23, 24, 26, 27, 28)]
    result['Giai sau'] = [td[i].string for i in (30, 31, 32)]
    result['Giai bay'] = [td[i].string for i in (34, 35, 36, 37)]
    return result


def main():
    """
    Thuc hien chay script de lay thong tin
    """
    par = argparse.ArgumentParser()
    par.add_argument('xoso', type=str, nargs='*',
                     help='Input: Dien cac so ban da mua', default=None)
    args = par.parse_args()
    result = layketqua()
    if len(args.xoso) == 0:
        print('Ket qua xo so cua hom nay: {}'.format(result))
    else:
        for i in args.xoso:
            for giai in result:
                for so in result[giai]:
                    if str(i)[-2:] == so[-2:]:
                        print('So {} co 2 so cuoi trung voi giai: {} {}'
                              .format(i, giai, result[giai]))


if __name__ == "__main__":
    main()
