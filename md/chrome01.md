使用chrome浏览器自带的开发者工具查看http头的方法 
1.在网页任意地方右击选择审查元素或者按下 shift+ctrl+c, 打开chrome自带的调试工具; 
2.选择network标签, 刷新网页(在打开调试工具的情况下刷新); 
---
3.刷新后在左边找到该网页url,点击 后右边选择headers,就可以看到当前网页的http头了


8888888888888888

超完整的 Chrome 浏览器客户端调试大全
http://web.jobbole.com/89344/

Chrome 浏览器客户端调试 name headers preview

Request Payload数据如何查看详细的json数据？点击旁边的view source按钮-》复制-》找个json在线转换网站，输入，即可查看。

返回的数据如何查看？有2种看法。一个是preview看大概浏览模式，另一个是response看详细json数据。

如何查看请求的服务器地址？点击network->xhr->name显示请求地址；右侧Headers->Request URL显示详细的url。

有的时候找不到请求的url怎么办？因为xhr只显示ajax请求的地址。推荐的步骤是这样的。先看xhr下面有没有-》然后看Doc下面-》再看other-》然后其他几个选项卡都看看-》最后在后台打断点，日志输出。

https://blog.csdn.net/milogenius/article/details/78897745

Chrome（谷歌）浏览器调试教程珍藏版

https://www.cnblogs.com/LibraThinker/p/5981346.html

Chrome开发者工具详解(2)-Network面板
---
这些按钮的功能点如下：

Elements:查找网页源代码HTML中的任一元素,手动修改任一元素的属性和样式且能实时在浏览器里面得到反馈。
Console:记录开发者开发过程中的日志信息，且可以作为与JS进行交互的命令行Shell。
Sources:断点调试JS。
Network:从发起网页页面请求Request后分析HTTP请求后得到的各个请求资源信息（包括状态、资源类型、大小、所用时间等），可以根据这个进行网络性能优化。
Timeline:记录并分析在网站的生命周期内所发生的各类事件，以此可以提高网页的运行时间的性能。
Profiles:如果你需要Timeline所能提供的更多信息时，可以尝试一下Profiles,比如记录JS CPU执行时间细节、显示JS对象和相关的DOM节点的内存消耗、记录内存的分配细节。
Application:记录网站加载的所有资源信息，包括存储数据（Local Storage、Session Storage、IndexedDB、Web SQL、Cookies）、缓存数据、字体、图片、脚本、样式表等。
Security:判断当前网页是否安全。
Audits:对当前网页进行网络利用情况、网页性能方面的诊断，并给出一些优化建议。比如列出所有没有用到的CSS文件等。


Network面板

面板可以记录页面上的网络请求的详情信息，从发起网页页面请求Request后分析HTTP请求后得到的各个请求资源信息（包括状态、资源类型、大小、所用时间、Request和Response等），可以根据这个进行网络性能优化。

我把Google官方网站上介绍Network面板的图贴到这里，该面板主要包括5大块窗格(Pane)：

Controls 控制Network的外观和功能。
Filters 控制Requests Table具体显示哪些内容。
Overview 显示获取到资源的时间轴信息。
Requests Table 按资源获取的前后顺序显示所有获取到的资源信息，点击资源名可以查看该资源的详细信息。
Summary 显示总的请求数、数据传输量、加载时间信息。


Capture screenshots（捕捉网页截图）


