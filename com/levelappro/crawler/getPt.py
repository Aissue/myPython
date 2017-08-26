from urllib import request
from bs4 import BeautifulSoup as bs

#定义保存函数
def savefile(data):
    path = "E:\\projects\\Spider\\02_douban.out"
    f = open(path,'wb')
    f.write(data)
    f.close()

url = 'https://movie.douban.com/nowplaying/beijing/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
req = request.Request(url=url, headers=headers)
resp = request.urlopen(req)

data = resp.read()
html_data = data.decode('utf-8')

soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    for tag_img_item in item.find_all('img'):
        nowplaying_dict['name'] = tag_img_item['alt']
        nowplaying_list.append(nowplaying_dict)


print(nowplaying_list)



