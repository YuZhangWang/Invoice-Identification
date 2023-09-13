import os
import time
from glob import glob

import numpy as np
from PIL import Image

from ocr import ocr

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result, image_framed


if __name__ == '__main__':

    # 确定需要检测的图片文件
    image_files = glob('./test_images/*.*')
    # 指定检测结果输出文件夹
    result_dir = './test_result'

    # 将输入文件夹的文件按照文件名，在for循环中依次进行读取
    for image_file in sorted(image_files):
        t = time.time()
        result, image_framed = single_pic_proc(image_file)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        txt_file = os.path.join(result_dir, image_file.split('/')[-1].split('.')[0] + '.txt')

        print(txt_file)
        txt_f = open(txt_file, 'w')
        Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])
            txt_f.write(result[key][1] + '\n')
        txt_f.close()

    # 将输出结果的txt进行读取，输入到excel表格当中
