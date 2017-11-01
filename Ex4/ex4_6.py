#!/usr/bin/env python3


def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Bé lên 3 bé đi lớp 4' -> [3, 4]
    '''

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    import string

    temp_str = []
    text = text.replace(' ', ' a')
    for word in text.strip().split():
        for char in word:
            temp_str.append(char)

    temp_str.append('.')
    # print(temp_str)
    result = []
    i = 0
    l = len(temp_str)
    while i < l:
        if temp_str[i] in string.digits and i != l - 1:
            for j in range(i + 1, l):
                if temp_str[j] not in string.digits:
                    result.append(int(''.join(temp_str[i: j])))
                    i = j
                    break
        i += 1
    return result


def main():
    ss = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    # ss = ' 0 a1asdf44  444444asdf asdf 3456'
    print(solve(ss))
    assert solve(ss) == [60, 20, 0]


if __name__ == "__main__":
    main()
