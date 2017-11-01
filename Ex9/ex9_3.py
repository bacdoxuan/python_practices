import requests
import argparse

'''
Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên
stackoverflow.com. In ra màn hình: Title câu hỏi, link đến câu trả lời được
vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  so.py N LABEL
'''


def get_best_question_answer(tagname, N):
    """
    Lay ra top N cau hoi theo tagname, vi du: python 10 -> lay ra 10 cau hoi
    co tag python duoc vote cao nhat, moi cau hoi kem 1 cau tra loi vote cao
    nhat
    input: tagname, N
    :rtype
    """
    # Lay N cau hoi theo tag, sap xep theo thu tu so vote tu cao den thap
    r = requests.get('https://api.stackexchange.com/2.2/questions?pagesize={}'
                     '&order=desc&sort=votes&tagged={}&site=stackoverflow'
                     .format(N, tagname))

    # Lay N cau hoi dau tien va link tra loi tuong ung
    for i in range(N):
        question_title = r.json()['items'][i]['title']
        question_id = r.json()['items'][i]['question_id']
        answers_list = requests.get('https://api.stackexchange.com/2.2/'
                                    'questions/{}/answers?pagesize=1&order='
                                    'desc&sort=votes&site=stackoverflow'
                                    .format(str(question_id)))
        best_answer_id = str(answers_list.json()['items'][0]['answer_id'])
        best_answer_link = ''.join(['https://stackoverflow.com/a/',
                                    best_answer_id])

        print('Question', i + 1, end=': ')
        print(question_title, end='. ')
        print('Best answer link: ', best_answer_link)


def main():
    """
    function main truyen tham so cho script tu nguoi dung
    """
    parsr = argparse.ArgumentParser()
    parsr.add_argument('N', type=int, help='N la so cau hoi')
    parsr.add_argument('tagname', type=str, help='tagname can tim kiem')
    args = parsr.parse_args()
    # 1 truong hop dac biet, khi tim tagname = c# thi khi tim request se chuyen
    # thanh c%23
    if args.tagname == 'c#':
        args.tagname = 'c%23'
    get_best_question_answer(args.tagname, args.N)


if __name__ == "__main__":
    main()
