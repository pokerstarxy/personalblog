<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vim使用</title>
    <style type="text/css" media="all">
      body {
        margin: 0;
        font-family: "Helvetica Neue", Helvetica, Arial, "Hiragino Sans GB", sans-serif;
        font-size: 14px;
        line-height: 20px;
        color: #777;
        background-color: white;
      }
      .container {
        width: 700px;
        margin-right: auto;
        margin-left: auto;
      }

      .post {
        font-family: Georgia, "Times New Roman", Times, "SimSun", serif;
        position: relative;
        padding: 70px;
        bottom: 0;
        overflow-y: auto;
        font-size: 16px;
        font-weight: normal;
        line-height: 25px;
        color: #515151;
      }

      .post h1{
        font-size: 50px;
        font-weight: 500;
        line-height: 60px;
        margin-bottom: 40px;
        color: inherit;
      }

      .post p {
        margin: 0 0 35px 0;
      }

      .post img {
        border: 1px solid #D9D9D9;
      }

      .post a {
        color: #28A1C5;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="post">
        <h1 class="title">Vim使用</h1>
        <div class="show-content">
          <div class="image-package"><img src="http://upload-images.jianshu.io/upload_images/2600308-deb2aaf0e2c1b807.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2600308-deb2aaf0e2c1b807.png?imageMogr2/auto-orient/strip" data-image-slug="deb2aaf0e2c1b807" data-width="598" data-height="411"><br><div class="image-caption">行首行尾</div></div><p>正常编辑 需要调节写入位置，可从正常模式切换到插入模式&nbsp; ； <br></p><p>o 新开一行 ； O之上新开一行&nbsp; 并转入插入模式<br></p><p>s 替换光标之后的字符； S 替换整行</p><p>r&nbsp; 正常模式替换单个&nbsp; R 到 replace --&gt;替换后面的，但是需要按esc回到正常模式</p><p>v 进入可视化界面&nbsp;&nbsp; v单位是字符&nbsp; V单位是line&nbsp; 从当前字符串（行）算起&nbsp; 3e 3个单位，c删除选中并进入编辑</p><p>h,j,k,l&nbsp;&nbsp;&nbsp;&nbsp; 最左和最右&nbsp;&nbsp; h,l&nbsp; 对应左右，j,k 对应<b>下 上&nbsp;&nbsp;&nbsp;&nbsp; <br></b></p><p>^&nbsp; 移到开头 $ 到结尾&nbsp;&nbsp; H到窗口最高 ，M 中，L最低</p><p>2w 后移2个单词 2b前移 &nbsp; e 单词结尾（）&nbsp; 上/下 句 {} 上/下 段</p><p>ma 标记此处a&nbsp;&nbsp;&nbsp; ‘a&nbsp; 返回值当前行最前，`a 返回至标记处</p><p>~&nbsp;&nbsp; 大小写切换&nbsp; <br></p><p>参考包含在第二段里。将光标置于两个管道符号（'|'）之间，并按下ctrl-]就借助链接跳转到了相应的:help主题，跳回的话请按ctrl-o</p><p>d 剪切&nbsp;&nbsp; dw dl dd 单词，字母 ，行<br></p><p>y 复制&nbsp; <br></p><p>p 粘贴 p 右边&nbsp; P 左边&nbsp; 光标位置分析&nbsp; -------光标后字母基准<br></p><p>撤销返回&nbsp;&nbsp;&nbsp; earlier 4m later45s&nbsp; undo 5 撤销5步 <br></p><p>u&nbsp; 回退&nbsp; 和 ctrl + r&nbsp; 回退前&nbsp; <br></p><p>&nbsp; 完整匹配&nbsp;&nbsp; <br></p><div class="image-package"><img src="http://upload-images.jianshu.io/upload_images/2600308-9f5589329bc55118.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2600308-9f5589329bc55118.png?imageMogr2/auto-orient/strip" data-image-slug="9f5589329bc55118" data-width="285" data-height="103"><br><div class="image-caption">利用格式\&lt;(\w+)\&gt;</div></div><p>&nbsp; set hlsearch&nbsp; 设置高亮</p><p>vim -R 编辑&nbsp;&nbsp; --只读模式，若是已经打开，则需要set ro命令，提升速度 ，减少不必要的操作</p><p>r filename&nbsp;&nbsp; 插入其它文本内容</p><p>寄存器使用&nbsp; "a3yy&nbsp;&nbsp;&nbsp; 寄存器a&nbsp;&nbsp; 三行&nbsp; 全部复制</p><p>set textwidth=20&nbsp;&nbsp; 以及gwap&nbsp; 进行重新生成文本</p><p>替换&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :s/\(bachchan\) \(amitabh\)/\2 \1/g&nbsp;&nbsp;&nbsp; --两个字符串替换位置&nbsp; --转义(\2) &nbsp;&nbsp; g全局 c加上确认信号，确认每一次更改</p><p>自动拼写检查&nbsp;&nbsp; <br></p><p>简写（常用语）&nbsp;&nbsp;&nbsp;&nbsp; iab&nbsp;&nbsp; 插入模式使用&nbsp;&nbsp; ----iab name&nbsp; content&nbsp;&nbsp;&nbsp; ----:ab查询有那些简写 ----:abclear 清除所有缩写 --- 清除部分 una[name]&nbsp;&nbsp; :una name</p><p>插入模式name输出完，然后空格，就可以看到。</p><p><br></p><div class="image-package"><img src="http://upload-images.jianshu.io/upload_images/2600308-428fd3834dfe3f18.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2600308-428fd3834dfe3f18.png?imageMogr2/auto-orient/strip" data-image-slug="428fd3834dfe3f18" data-width="370" data-height="379"><br><div class="image-caption">visual block 一列下来，需要移至行尾<br></div></div><p>new新建文件&nbsp; 并粘贴过去</p><p>vim 远程编辑ftp文件&nbsp; <br></p><p>折叠模式设置&nbsp; --需要依靠foldmethod 折叠方法&nbsp; 如 indent&nbsp; 依靠缩进符判断折叠</p><p><br></p><div class="image-package"><img src="http://upload-images.jianshu.io/upload_images/2600308-c48a1019f00c5eef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2600308-c48a1019f00c5eef.png?imageMogr2/auto-orient/strip" data-image-slug="c48a1019f00c5eef" data-width="463" data-height="284"><br><div class="image-caption">折叠定义方式</div></div><p>缓存技术</p><p>同事打开多个文件 ，通过 b 1&nbsp; 切换缓存位置 ，或者e 11.txt 编辑文件名&nbsp; ：buffers | ：ls查看所有缓存的文件 <br></p><p>ctrl +w 两次切换 两个文档编辑的界面（单一文档new后会存在上下两个缓存区）</p><p>:sp&nbsp; 同文件多窗口，可以对比。操作一致。在同一内存中，任何一个改变会同事反应到两个文件中&nbsp; 若是需要垂直分割，则:vsp命令&nbsp; ctrl+w _ 最大化&nbsp; tabnew新建标签页 gt</p><h2>宏使用：</h2><p>qa 开始录制宏a&nbsp; q退出&nbsp; @a&nbsp; 调用宏</p><p>gUl&nbsp;&nbsp; 下一个字母大写&nbsp; g所有U大写u小写 l一个字母&nbsp;&nbsp; gUU <br></p><p>~大小写</p><p><br></p><div class="image-package"><img src="http://upload-images.jianshu.io/upload_images/2600308-1972c1f1443318f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" data-original-src="http://upload-images.jianshu.io/upload_images/2600308-1972c1f1443318f1.png?imageMogr2/auto-orient/strip" data-image-slug="1972c1f1443318f1" data-width="412" data-height="154"><br><div class="image-caption">python 和vi<br></div></div><p>通过echo has("python")判断是否支持python</p><p>vim下加载该文件&nbsp;&nbsp;&nbsp; source xx.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 然后回调函数 call function()</p><p>利用EOF 包含python程序</p>
        </div>
      </div>
    </div>
  </body>
</html>