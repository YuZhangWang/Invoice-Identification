import os
import xlwt


def eachFile(filepath):
    pathDir = os.listdir(filepath)  # 遍历文件夹中的text
    return pathDir


def readfile(name):
    fopen = open(name, 'r')
    cou = 0
    for lines in fopen.readlines():  # 按行读取text中的内容
        cou = cou + 1
        lines = lines.replace("\n", "").split(",")  # 分割一下
        lines_l = list(lines)  # 每一行都是一个list了
        # print(lines_l)
    fopen.close()
    return cou


# 装txt的文件夹的路径,只装txt文件，可以多个
filePath = "D:/Code/Python/29invoice/ocr/test_result/test_txt"
pathDir = eachFile(filePath)

ch = []
le = []
le.append(0)
for allDir in pathDir:
    # child = os.path.join('%s%s' % (filepath, allDir))
    child = "D:/Code/Python/29invoice/ocr/test_result/test_txt" + \
        '\\' + allDir  # 装txt的文件夹的路径,只装txt文件
    ch.append(child)
    readfile(child)
    le.append(readfile(child))

# 用le记录一个txt有多少行，方便下一个文件读取的时候不会在写入时覆盖
for i in range(1, len(le)):
    le[i] = le[i] + le[i - 1]
    # print(le)

file = xlwt.Workbook(encoding='utf-8')
# 新建sheet
sheet = file.add_sheet('test')

for i in range(len(ch)):
    k = le[i] + 1
    print(k)
    with open(ch[i]) as f1:
        print(ch[i])
        for lines in f1.readlines():
            lines = lines.replace("\n", "").split(",")
            lines_l = list(lines)  # 每一行都是一个list
            i = 0
            for line in lines_l:
                sheet.write(k, i, line)  # 一个一个写
                i = i + 1
            k = k + 1
        f1.close()

# 生成文件的路径，一定要记得save
file.save("D:/Code/Python/29invoice/ocr/test_result/test.xls")
