#!/usr/bin/env python3


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    import string
    # print(string.ascii_lowercase)
    str_letter = string.ascii_lowercase
    temp_sum = 0
    result = []
    i = 0
    j = 0

    # return [sum(string.ascii_letters.index(char_of_word) + 1
    #             for char_of_word in word.lower())
    #             for word in words]

    for word in words:
        while i < len(word):
            while j < len(str_letter):
                if word.lower()[i] == str_letter[j]:
                    # temp_sum += str_letter.index(str_letter[j])
                    temp_sum += j + 1
                j += 1
            j = 0
            i += 1
        result.append(temp_sum)
        i = 0
        temp_sum = 0
    return result


def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
             'Python', 'FAMILUG', 'pymi']

    print(solve(words))


if __name__ == "__main__":
    main()
