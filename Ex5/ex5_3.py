#!/usr/bin/env python3

data = '''Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.''' # NOQA


# Chú ý: dấu “ không phải double quotes "

def solve(input_data):
    '''
    Đặt result bằng list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất,
    mỗi tuple chứa từ và số lần xuất hiện tương ứng.
    (Nếu có nhiều từ cùng xuất hiện với số lần như nhau thì trả về từ nào
    cũng được).
    '''
    temp_result = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    text = input_data.replace('“', '').replace(',', '').replace('.', '')
    text = text.replace('”', '').replace(';', '').lower().split()
    # Thuc hien tim so lan moi chu xuat hien trong doan text va dua ra 1 list
    # va trong list khong co 2 phan tu nao bi trung lap
    for index in range(len(text)):
        if text[index] not in text[:index]:
            temp_result.append((text[index], text.count(text[index])))

    # Sap xep theo cach moi:
    result = sorted(temp_result, key=lambda temp: temp[1], reverse=True)
    print(result[:5])
    return result[:10]


def main():
    # Đây là một cách làm khác với kiểu dữ liệu có sẵn
    # trong thư viện collections của Python
    from collections import Counter
    # Regex (re) là một công cụ xử lý string khác so với các method của
    # `str`, linh hoạt nhưng phức tạp, khó đọc, dễ sai.
    import re
    cleaned = re.sub(r'“|”|\.|,', ' ', data)
    c = Counter(cleaned.split())
    top = c.most_common(5)
    result = solve(data)
    assert result[:5] == top, (result[:5], top)

    # In ra 10 từ xuất hiện nhiều nhất kèm số lần xuất hiện
    # Viết code in ra màn hình sau dòng này


if __name__ == "__main__":
    main()
