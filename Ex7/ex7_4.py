#!/usr/bin/env python3


def solve(text):
    '''Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    '''
    tmp_result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    i = 0
    text = ''.join([text, '.'])
    while i < len(text):
        for j in range(i + 1, len(text)):
            if text[j] != text[i]:
                tmp_result.append(text[i:j])
                i = j - 1
                break
        i += 1

    result = ''.join([chars if len(chars) == 1 else
                      ''.join([chars[0] * 2, str(len(chars))])
                      for chars in tmp_result])
    return result


def main():
    print(solve('abbbccccdddd'))


if __name__ == "__main__":
    main()
