import json
import os
import requests
import argparse
import time

'''
Viết script lấy về 50 kết quả đầu tiên tìm được với từ khoá "coffee"
quanh toạ độ 10.779614,106.699256 (nhà thờ Đức Bà - HCM) với bán kính 5KM.
Ghi kết quả theo định dạng JSON vào file hcm_coffee.json. (hoặc lưu vào
1 SQLite DB)

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API.
'''


def ggmap_search(location, keyword, radius, token):
    """
    Dinh danh cau lenh de tim kiem dia diem tren Google API:
    Rank the results by distance
    https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&rankby=distance&radius=500&types=food&key=YOUR_API_KEY
    Parameters:
    json? (or xml)
    location (latitude/longitude)
    radius (m)
    rankby (distance) (can't use radius and rankby distance at the same time)
    types (str)
    key (token)
    To see the next set of results you can submit a new query, passing the
    result of the next_page_token to the pagetoken parameter. For example:
    https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={}&key=YOUR_API_KEY
    """
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' \
          'location={}&radius={}&types={}&key={}'\
          .format(location, radius, keyword, token)
    print('Firsr URL: ', url)
    first_page = requests.get(url)
    result = first_page.json()['results']
    # Neu ket qua tra ve chi co 1 trang thi khong co next_page_token
    # lay het ket qua trong trang dau tien va ket thuc tim kiem luon
    if 'next_page_token' not in first_page.json():
        try:
            with open('hcm_coffee.json', 'w') as f:
                f.write(json.dumps(result, indent=4))
            print('Du lieu da duoc luu tai: {}'.format(os.getcwd()))
        except Exception as e:
            print(e)
        return result

    pagetoken = first_page.json()['next_page_token']
    print('*' * 40)
    print('First token: ', pagetoken)
    print('*' * 40)
    while len(result) <= 50:
        next_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/' \
                   'json?pagetoken={}&key={}'.format(pagetoken, token)
        print('Next URL: ', next_url, type(next_url))
        print('*' * 40)
        # Cho 5s de web server thiet lap trang web voi token moi.
        # Neu thuc hien request luon se co loi trang tra ve khong co du lieu
        time.sleep(5)
        r = requests.get(next_url)
        for i in r.json()['results']:
            if len(result) > 49:
                break
            else:
                result.append(i)
        if 'next_page_token' in r.json():
            pagetoken = r.json()['next_page_token']
            print('Next token: ', pagetoken)
            print('*' * 40)
        else:
            break

    print('So ket qua tim kiem duoc: ', len(result))

    try:
        with open('hcm_coffee.json', 'w') as f:
            f.write(json.dumps(result, indent=4))
        print('Du lieu da duoc luu tai: {}'.format(os.getcwd()))
    except Exception as e:
        print(e)
    return result


def main():
    """
    Nguoi dung nhap thong tin 'location, keyword, radius, token' de chay script
    """
    parsr = argparse.ArgumentParser()
    parsr.add_argument('location', type=str, help='Toa do google map lat,long')
    parsr.add_argument('keyword', type=str, help='Noi dung can tim kiem')
    parsr.add_argument('radius', type=str, help='Ban kinh tim kiem (m)')
    parsr.add_argument('token', type=str, help='Token Google cua ban')
    args = parsr.parse_args()
    ggmap_search(args.location, args.keyword, args.radius, args.token)


if __name__ == "__main__":
    main()
