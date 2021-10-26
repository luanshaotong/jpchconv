from unicodedata import normalize
from urllib.parse import unquote_plus
from re import compile
from contextlib import suppress
import os

def repare_name(name: str):
    '''修改文件名乱码,
    返回正常的字符串'''
    for root, dirs, files in os.walk(name):  # 遍历目录
        for f in files:                      # 获取目录下所有文件
            print(os.path.join(root, f))

        # 遍历所有的文件夹
        #for d in dirs:
        #    print(os.path.join(root, d))
            with suppress(UnicodeEncodeError):  # 如无法编码，则跳过
                with suppress(UnicodeDecodeError):
                    data = f.encode('gbk')  # 以gbk编码（当前系统编码）字符串，因为原jis编码被系统错误的解码成了gbk编码
                    print(data)
                    n = data.decode('shift_jis')  # 将二进制数据以日文解码
                    print(n)
                    if n != f:  # 如果内容不同，说明其中存在非拉丁字符
                        os.rename(os.path.join(root, f), os.path.join(root, n))  # 重命名为解码后的日文文件名
                        print(os.path.join(root, n))


if __name__ == '__main__':
    from pathlib import Path

    for path in Path('.').glob('*.*'):
        repare_name(path.name)