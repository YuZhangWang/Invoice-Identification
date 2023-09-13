<a name="readme-top"></a>

<!-- 项目相关的一些图标信息 -->
<div align="center">
  <a href="https://github.com/YuZhangWang/Invoice-Identification/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/YuZhangWang/Invoice-Identification.svg?style=for-the-badge" alt="">
  </a>
  <a href="https://github.com/YuZhangWang/Invoice-Identification/network/members">
        <img src="https://img.shields.io/github/forks/YuZhangWang/Invoice-Identification.svg?style=for-the-badge" alt="">
  </a>  
  <a href="https://github.com/YuZhangWang/Invoice-Identification/stargazers">
        <img src="https://img.shields.io/github/stars/YuZhangWang/Invoice-Identification.svg?style=for-the-badge" alt="">
  </a>  
  <a href="https://github.com/YuZhangWang/Invoice-Identification/issues">
        <img src="https://img.shields.io/github/issues/YuZhangWang/Invoice-Identification.svg?style=for-the-badge" alt="">
  </a> 
  <a href="https://github.com/YuZhangWang/Invoice-Identification/blob/master/LICENSE.txt">
        <img src="https://img.shields.io/github/license/YuZhangWang/Invoice-Identification.svg?style=for-the-badge" alt="">
  </a>   
</div>


<!-- 项目图标 -->
<br />
<div align="center">
  <a href="https://github.com/YuZhangWang/Invoice-Identification">
    <img src="https://gcore.jsdelivr.net/gh/YuZhangWang/Creative-pictures02@master/img/202309131528454.png" alt="Logo" width="140" height="140">
  </a>

<h3 align="center">Invoice-Identification</h3>

  <p align="center">
    📰 Projects based on CTPN and CRNN 
    <br />
    <a href="https://yuzhang.wang/110-ctpn-model/"><strong>阅读说明文档 »</strong></a>
    <br />
    <br />
    <a href="https://www.bilibili.com/video/BV1n34y1h79n/">View Demo</a>
    ·
    <a href="https://github.com/YuZhangWang/Invoice-Identification/issues">Report Bug</a>
    ·
    <a href="https://github.com/YuZhangWang/Invoice-Identification/issues">Request Feature</a>
  </p>
</div>


<div align="center">
<a href="./README.md">简体中文</a> |
<a href="./README-EN.md">English</a>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#关于">关于</a></li>
    <li><a href="#配置安装">配置安装</a></li>
    <li><a href="#使用方法">使用方法</a></li>
    <li><a href="#训练">训练</a></li>
    <li><a href="#加入这个项目">加入这个项目</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#联系作者">联系作者</a></li>
    <li><a href="#致谢">致谢</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# 关于
![product-screenshot](https://gcore.jsdelivr.net/gh/YuZhangWang/Creative-pictures02@master/img/202309131441743.png)

本项目使用了[Synthetic Chinese String Dataset](https://github.com/senlinuc/caffe_ocr/tree/master/examples/ocr/densenet)数据集，总体数据量达到了**3,644,007**个

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>


# 配置安装

这里可以跟着[Pytorch安装（包含cuda详细安装教程）](https://liuhuanhuan.blog.csdn.net/article/details/114157146)直接来，或者根据我博客中的[环境配置](https://yuzhang.wang/139-invoice-identification/#%E7%B3%BB%E7%BB%9F%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)进行操作。这里我踩过坑了，跟着两个链接中的内容来，一步步来就可以配置成功。

然后就是创建Conda环境，缺什么包补什么包就行了，出了问题的话，多进行搜索，90%的问题都能解决，实在解决不了，你可以邮箱联系我，找我帮你配置一下。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

# 使用方法

由于这里我把炼好的丹也上传上来了，所以可以直接下载。

下载完成之后，在 *test_images* 文件夹中放入你想要识别的的发票图片，然后运行 *demo.py* 文件，等待运行。


等到运行结束之后，在 *test_result/test_images* 中就可以看到两种结果，一种是图片输出形式，上面标注了对文字的识别准确度，另一种是文本形式，将识别到的内容放到了文本之中。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>


# 训练

如果需要训练的话，请下载Releases中的[VOC2007](https://github.com/YuZhangWang/Invoice-Identification/releases/tag/Training-Data-Set)，这是其中一部分所需的训练集，除此之外，[OCR_DataSet](https://github.com/WenmuZhou/OCR_DataSet)和[crnn_chinese_characters_rec](https://github.com/Sierkinhane/crnn_chinese_characters_rec)中的内容是剩余的数据集。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- CONTRIBUTING -->
# 加入这个项目

贡献是使开源社区成为一个学习、激励和创造的奇妙场所的原因。我们**非常感谢**你的任何贡献。

如果你有什么建议可以让它变得更好，请fork这个repo并创建一个pull request。你也可以简单地打开一个带有 "enhancement"标签的问题。
不要忘了给这个项目一颗星! 再次感谢!

1. Fork 这个项目
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推广到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个Pull Request

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>



<!-- LICENSE -->
# License

在GLP-3.0和996.ICU许可下发布。更多信息见<a href="./LICENSE">LICENSE</a> 和 <a href="./LICENSE-996.ICU">LICENSE-996.ICU</a>。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>



<!-- CONTACT -->
# 联系作者

YuZhangWang - YuZhangWang233@163.com

更多联系方式:
[ YuZhangWang](https://github.com/YuZhangWang) or
[YuZhangWang的领域](https://yuzhang.wang/about)

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>



<!-- ACKNOWLEDGMENTS -->
# 致谢

* [Awesome-Repository-Template](https://github.com/YuZhangWang/Awesome-Repository-Template)
* [OCR_DataSet](https://github.com/WenmuZhou/OCR_DataSet)
* [crnn_chinese_characters_rec](https://github.com/Sierkinhane/crnn_chinese_characters_rec)

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>
