
VS Code里面编写Markdown
======================
Hello World!
------------
你好！
------

**雅雅**

*轩轩*

#2019

by hhh2008

可以渲染序列图：

//```sequence
//张三->李四: 嘿，小四儿, 写博客了没?
//Note right of 李四: 李四愣了一下，说：
//李四-->张三: 忙得吐血，哪有时间写。
//```

项目１
项目２
:   定义 A
:   定义 B

项目３
:   定义 C

:   定义 D

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
--------------------- 
作者：qiphon3650 
来源：CSDN 
原文：https://blog.csdn.net/qiphon3650/article/details/81002152 

markdown 基本语法
1、标题
///下划线模式

这是h1
======
这是h2
------
#这是h1
######这是h6

1
2
3
4
5
6
7
8
9
10
2、区块类
用单箭头表示 >

3、无需列表
实现方式

可以用 + 号
也可以用 - 号
还可以用 * 号 
二级
用一个空格隔开
4、有序列表
用阿拉伯数字+ 英文的标点
就是这样，也用单个空格隔开 
这是二级
二级第二个
5、连接
用[]后面跟包有链接的小括号 [qiphon](https://blog.csdn.net/qiphon3650) qiphon 中括号中的是显示的文字

6、加粗
这是加粗的实现现 **这是加粗**

7、斜体
这是斜体 的实现方式 *斜体*

8、图片


![这里是alt qiphon](https://avatar.csdn.net/D/1/5/3_qiphon3650.jpg "qiphon")
1
9、表格
Tables	Are	Cool
col 3 is	right-aligned	$1600
col 2 is	centered	$12
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
1
2
3
4
5
10、分隔线
这是分隔线 ，只需要3个*号
***

11、代码段，
上面的例子展示实际东西用的都是代码段，6个反引号实现 `
''''''
a
b
c

--------------------- 
