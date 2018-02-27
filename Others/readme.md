# atom中自己使用的一些格式

---

首先安装YaHei.Consolas字体，中文使用微软雅黑，英文使用consolas。在一些字体设置里，都会使用这个字体。比较美观。

---

1. markdown-themeable-pdf部分

  下载markdown-themeable-pdf，用来通过markdown生成pdf文件。
  替换**C:\Users\当前用户名\.atom\markdown-themeable-pdf**目录下的文件

  > 这一部分是基础的格式，这里的styles.css包括了代码，标题等内容。
  但对于代码高亮则在不同的位置。

  - 在C:\Users\hanyx\.atom\packages\markdown-themeable-pdf\css下，把全局文档的`document.css`里做修改。主要是高亮代码的背景部分。已经将修改好的该文件放在当前目录下了。
  -  在C:\Users\hanyx\.atom\packages\markdown-themeable-pdf\node_modules\highlight.js\styles目录下，找到需要的代码高亮的css文件，然后更改里面的背景色等。比如atom-one-light.css。将里面的`.hljs`改成：
  ```css
  .hljs {
    display: block;
    overflow-x: auto;
    padding: 0.5em;
    color: #383a42;
    background: #e8e8e8;
  }
  ```
  这里也放置了`github-gist.css`和`atom-one-light.css`两个高亮主题

2. styles.less部分

  替换`C:\Users\hanyx\.atom`目录下的`style.less`，用来指定在atom里github markdown preview的预览
