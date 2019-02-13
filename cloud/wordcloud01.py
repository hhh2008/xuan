import os, time
 
import jieba.analyse
 
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
 
 
def read_content(content_path):
    content = ''# 初始化内容为空
    print('...正在扫描文件...')
    for f in os.listdir(content_path): # 使用os模块的listdir函数枚举文件夹下所有文件
        time.sleep(1)
        file_fullpath = os.path.join(content_path,f) # 拼接文件完整路径
        if os.path.isfile(file_fullpath): # 判断是否是文件
            content += open(file_fullpath,'r',encoding='UTF-8').read()
            content += '\n'
    print('...正在扫描完毕...')
    return content
 
# 读取文件夹内容
content = read_content('D:/code18/xiaoshuo/')
 
 
print('...正在提取关键字...')
time.sleep(2)
# 这里使用jieba的textrank提取出1000个关键词及其比重
result = jieba.analyse.textrank(content, topK=1000, withWeight=True)
# 生成关键词比重字典
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
# print(keywords)
print('...关键字提取完毕...')
 
#//////////////////////////////////////////////////
print('...正在生成云图...')
time.sleep(2)
# 初始化图片
image = Image.open('D:/workspace_python/zfiles/tmc.png')
graph = np.array(image)
# 生成云图，这里需要注意的是WordCloud默认不支持中文，所以这里需要加载中文黑体字库
wc = WordCloud(font_path='./fonts/simhei.ttf',
    background_color='white', max_words=1000, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
print('...生成云图成功...')
# 显示图片
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off") # 关闭图像坐标系
plt.show()

'''--------------------- 
作者：smartdt 
来源：CSDN 
原文：https://blog.csdn.net/smartdt/article/details/78054706 
版权声明：本文为博主原创文章，转载请附上博文链接！'''