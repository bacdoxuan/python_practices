#!/usr/bin/env python3

NUMBER_OF_LINES = 30000000


def solve(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: 30 triệu dòng.
    '''
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    result = []
    with open(output_path, 'w') as f:
        for index in range(1, NUMBER_OF_LINES + 1):
            if index % 2 == 0:
                f.write(str(2 * index) + '\n')
            else:
                f.write('1'*30 + '\n')

    with open(output_path, 'r') as f:
        for line in f:
            result.append(line)
            if len(result) == 11:
                result.pop(0)
    f.close()
    import os
    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()
