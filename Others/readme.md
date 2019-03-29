# atom中使用github风格的markdown

> 实现了github风格的markdown预览与PDF输出, PDF输出使用了markdown-themeable-pdf这个package

## 1. 字体

首先安装YaHei.Consolas字体，中文使用微软雅黑，英文使用consolas。字体显示效果非常好, 十分推荐。

## 2. github风格的markdown预览

把`styles.less`这个文件复制到用户的atom配置目录下, 路径如下:

```
C:\Users\你的用户名\.atom\
```

这样在atom中写的markdown, 预览(ctrl+shift+m)的样式就是github的markdown样式了。

## 3. 使用markdown-themeable-pdf这个package

pdf输出样例: [readme.pdf](./readme.pdf)

首先在atom中安装这个package。

把路径:

```
C:\Users\你的用户名\.atom\markdown-themeable-pdf\
```

里的`styles.css`用我给出的文件替换。

但是代码部分显示还是不好看, 打开这个目录:

```
C:\Users\你的用户名\.atom\packages\markdown-themeable-pdf\css
```

把里面的`document.css`用我给的替换掉, 这里改掉了原来的代码部分的背景色。

此外, 打开:

```
C:\Users\你的用户名\.atom\packages\markdown-themeable-pdf\node_modules\highlight.js\styles
```

这里存放了各种不同的代码高亮样式, 我这里给出了两个常用主题`github-gist.css`和`atom-one-light.css`的样式修改。把我改过的这两个文件放到这里即可。个人感觉github样式里代码块太浅了, 所以这里改的比较深. 具体颜色可以自行设置.

最后, 关于页眉和页脚的设置, 目录同样在:

```
C:\Users\你的用户名\.atom\packages\markdown-themeable-pdf\css
```

自己更改`footer.js`或者`header.js`即可。

全部弄好后要重启atom.
