import json
import os
import requests
import argparse
import time

"""
Sử dụng ``requests`` viết một script lấy toàn bộ thông tin các Page của
các quán cafe, trà ở trung tâm Hà Nội bằng **Facebook Graph API**.
Các từ khóa: ``"coffee", "tea", "cafe", "caphe", "tra da"``.
Tọa độ: ``21.027875,105.853654`` với bán kính là ``1km``.
Trả về kết quả bao gồm ``name, id, location, website`` của mỗi Page.
- Hướng dẫn dùng Facebook API:
https://developers.facebook.com/docs/graph-api/using-graph-api#search

- Sử dụng Grapth API Explorer để thử:
https://developers.facebook.com/tools-and-support/

- Hướng dẫn tạo Token:
https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens
**Chú ý**:
- Để ý đến phần paging của mỗi response trả về. Hãy bấm vào đó để xem chuyện gì
sẽ xảy ra.
- Kết quả trả về xuất ra một file ``hanoi_coffee.json``.
- Hãy sử dụng option ``indent`` cho function ``json.dump()``
"""


def graphfb_search(token):
    """
    Su dung graph api cua Facebook:
    https://graph.facebook.com/search?q=coffe&type=place&center=21.027875,105.853654&distance=1000&access_token=yourtoken
    Trong do:
    search? (tim kiem)
    q= (keywork can tim)
    type= (place)
    center = (Latitude and longitude)
    distance = (radius by meter)
    access_token = (your token)

    Ket qua tim kiem moi trang ra 25 ket qua (goolemapapis tra ve 20 ket qua
    cho 1 trang)

    Neu ket qua tra ve lon hon nhieu hon 25 se co 'next' dang url de truy cap
    vao trang ket qua tiep theo. Doi voi googlemapapis chi tra ve token cua
    trang tiep theo (khong tien bang cua facebook graph api)
    Vi du de sang trang tiep theo, su dung 'next' theo dang sau:
    https://graph.facebook.com/v2.6/search?access_token=1537101179929447%7COgflvAlB1-PYxAZA1XXBpsSqkzY&pretty=1&q=coffe&type=place&center=21.027875%2C105.853654&distance=1000&limit=25&after=MjQZD
    """
    keywords = ["coffee", "tea", "cafe", "caphe", "tra da"]
    kwlength = len(keywords)
    count = 1
    result = []
    print('*' * 40)
    for keyword in keywords:
        url = 'https://graph.facebook.com/search?q={}&type=place&center='\
              '21.027875,105.853654&distance=1000&fields='\
              'name,id,location,website&access_token={}'.format(keyword, token)
        r = requests.get(url)
        print(url)
        print(r)
        print('*' * 40)
        for i in r.json()['data']:
            if 'city' in i['location']:
                        if i['location']['city'] == 'Hanoi':
                            result.append(i)

        # Neu ket qua tim kiem chi ra 1 trang thi lay luon ket qua trang dau
        # va tiep tuc tim kiem voi tu khoa sau
        if 'paging' not in r.json():
            count += 1
            if count <= kwlength:
                continue
            else:
                break
        # Neu ket qua tim kiem dau tien co 'next' thi tiep tuc tim kiem den het
        else:
            while True:
                time.sleep(2)
                nexturl = r.json()['paging']['next']
                r = requests.get(nexturl)
                for j in r.json()['data']:
                    if 'city' in j['location']:
                        if j['location']['city'] == 'Hanoi':
                            result.append(j)
                if 'paging' in r.json():
                    if 'next' in r.json()['paging']:
                        continue
                else:
                    break
        print('So ket qua tim duoc den tu khoa {} la {}'.format(keyword,
              len(result)))
        print('*' * 40)

    try:
        with open('hanoi_coffee.json', 'w') as f:
            f.write(json.dumps(result, indent=4))
            print('Du lieu da duoc luu tai: {}'.format(os.getcwd()))
    except Exception as e:
        print(e)
    return result


def main():
    """
    Nguoi su dung nhap thong tin app token facebook de thuc hien tim kiem
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('token', type=str, help='Nhap app token facebook')
    args = parser.parse_args()
    graphfb_search(args.token)


if __name__ == "__main__":
    main()
