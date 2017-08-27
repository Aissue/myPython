import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba

text_from_file_with_apath = open('C:/Users/Public/Documents/python/result.txt', 'rb').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

backgroud_Image = plt.imread('C:/Users/Public/Documents/python/bigsum.png')
font = 'C:/Users/Public/Documents/python/font/simfang.ttf'
wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片
                max_words = 2000,            # 设置最大现实的字数
                stopwords = STOPWORDS,        # 设置停用词
                font_path = font,               # 设置字体格式，如不设置显示不了中文
                max_font_size = 50,            # 设置字体最大值
                random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
my_wordcloud = WordCloud(collocations=False, font_path=font, width=2000, height=2000, margin=2).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
