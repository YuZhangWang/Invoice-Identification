<a name="readme-top"></a>

<!-- Some icon information related to the project -->
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


<!-- Project Icons -->
<br />
<div align="center">
  <a href="https://github.com/YuZhangWang/Invoice-Identification">
    <img src="https://gcore.jsdelivr.net/gh/YuZhangWang/Creative-pictures02@master/img/202309131528454.png" alt="Logo" width="140" height="140">
  </a>

<h3 align="center">Invoice-Identification</h3>

  <p align="center">
    📰 Projects based on CTPN and CRNN 
    <br />
    <a href="https://yuzhang.wang/110-ctpn-model/"><strong>Read the description document »</strong></a>
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
  <summary>Contents</summary>
  <ol>
    <li><a href="#About">About</a></li>
    <li><a href="#Configure-installationn">Configure-installationn</a></li>
    <li><a href="#Instructions">Instructions</a></li>
    <li><a href="#Train">Train</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About
![product-screenshot](https://gcore.jsdelivr.net/gh/YuZhangWang/Creative-pictures02@master/img/202309131441743.png)

This project used the [Synthetic Chinese String Dataset](https://github.com/senlinuc/caffe_ocr/tree/master/examples/ocr/densenet) data set, and the overall data volume reached **3,644,007**

<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Configure-installationn

Here you can follow[Pytorch安装（包含cuda详细安装教程）](https://liuhuanhuan.blog.csdn.net/article/details/114157146)directly, or follow the[环境配置](https://yuzhang.wang/139-invoice-identification/#%E7%B3%BB%E7%BB%9F%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)in my blog operate. I've run into a trap here. Follow the content in the two links and you can configure it step by step.

The next step is to create a Conda environment. Just fill in whatever packages are missing. If there is a problem, search more. 90% of the problems can be solved. If you really can't solve it, you can contact me by email and ask me to help you configure it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Instructions

由于这里我把炼好的丹也上传上来了，所以可以直接下载。

下载完成之后，在 *test_images* 文件夹中放入你想要识别的的发票图片，然后运行 *demo.py* 文件，等待运行。


等到运行结束之后，在 *test_result/test_images* 中就可以看到两种结果，一种是图片输出形式，上面标注了对文字的识别准确度，另一种是文本形式，将识别到的内容放到了文本之中。

<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Train

如果需要训练的话，请下载Releases中的[VOC2007](https://github.com/YuZhangWang/Invoice-Identification/releases/tag/Training-Data-Set)，这是其中一部分所需的训练集，除此之外，[OCR_DataSet](https://github.com/WenmuZhou/OCR_DataSet)和[crnn_chinese_characters_rec](https://github.com/Sierkinhane/crnn_chinese_characters_rec)中的内容是剩余的数据集。

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under The GLP-3.0 and The 996.ICU License. See <a href="./LICENSE">LICENSE</a> and <a href="./LICENSE-996.ICU">LICENSE-996.ICU</a> for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

YuZhangWang - YuZhangWang233@163.com

More contact information:
[ YuZhangWang](https://github.com/YuZhangWang) or
[YuZhangWang的领域](https://yuzhang.wang/about)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Awesome-Repository-Template](https://github.com/YuZhangWang/Awesome-Repository-Template)
* [OCR_DataSet](https://github.com/WenmuZhou/OCR_DataSet)
* [crnn_chinese_characters_rec](https://github.com/Sierkinhane/crnn_chinese_characters_rec)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
