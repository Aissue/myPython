from urllib import request
from bs4 import BeautifulSoup as bs
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

#定义保存函数
def savefile(data):
    path = "C:/Users/Public/Documents/python/result.txt"
    f = open(path, 'a+')
    f.write(data)
    f.close()

# single crawler
def single_craw(url):
    req = request.Request(url=url, headers=headers)
    resp = request.urlopen(req)
    data = resp.read()
    html_data = data.decode('utf-8')

    soup = bs(html_data, 'html.parser')
    girl_info = soup.find_all('li', attrs={'class': 'media'})
    girl_info_detail = []
    leng = len(girl_info)
    for i in range(1, leng):
        items = girl_info[i].find_all('a', attrs={'target': '_blank'})
        for item in items:
            title = item.getText()
            if '【' in title or '】' in title:
                continue
            girl_info_detail.append(item['href'])

    predel_list = []
    for detail in girl_info_detail:
        new_req = request.Request(url=detail, headers=headers)
        new_resp = request.urlopen(new_req)
        new_html = new_resp.read().decode('utf-8')
        new_soup = bs(new_html, 'html.parser')
        new_detail = new_soup.find_all('div', attrs={'class', 'p-entry'})
        for target in new_detail:
            result = target.find_all('p')
            for p in result:
                text = p.getText()
                if '要求' in text:
                    temp = re.findall(r"[\w']+", text)
                    predel_list = predel_list + temp[1:]

    final_data = "".join(predel_list)
    #print(final_data)
    savefile(final_data)


if __name__ == '__main__':
    for i in range(1, 11):
        url_1 = 'http://date.jobbole.com/page/'
        url_2 = i
        url_3 = '/'
        url = '%s%d%s' % (url_1, url_2, url_3)
        print(url)
        single_craw(url)

#
