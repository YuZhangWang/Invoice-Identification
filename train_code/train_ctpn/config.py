import os

# base_dir = 'path to dataset base dir'
base_dir = './images'
img_dir = os.path.join(base_dir, 'D:/Code/Python/29invoice/VOC2007/JPEGImages')  # VOC数据集路径
xml_dir = os.path.join(base_dir, 'D:/Code/Python/29invoice/VOC2007/Annotations')

icdar17_mlt_img_dir = '/home/data2/egz/ICDAR2017_MLT/train/'  # ICdar19
icdar17_mlt_gt_dir = '/home/data2/egz/ICDAR2017_MLT/train_gt/'

num_workers = 2
pretrained_weights = 'train_data/checkpoints/ctpn_ep01_0.0737_0.1721_0.2458.pth'
train_txt_file = os.path.join(base_dir, r'D:/Code/Python/29invoice/VOC2007/ImageSets/Main/train.txt')
val_txt_file = os.path.join(base_dir, r'D:/Code/Python/29invoice/VOC2007/ImageSets/Main/val.txt')

anchor_scale = 16
IOU_NEGATIVE = 0.3
IOU_POSITIVE = 0.7
IOU_SELECT = 0.7

RPN_POSITIVE_NUM = 150
RPN_TOTAL_NUM = 300

# bgr can find from  here: https://github.com/fchollet/deep-learning-models/blob/master/imagenet_utils.py
IMAGE_MEAN = [123.68, 116.779, 103.939]
OHEM = True

checkpoints_dir = 'train_data/checkpoints'  # 模型文件夹路径
outputs = r'./logs'
