import requests
from bs4 import BeautifulSoup
lst = []
def func():
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    # }
    # , headers = headers
    url = 'https://bits.media/news/'
    responce = requests.get(url=url)
    soup = BeautifulSoup(responce.text , 'html.parser')
    res = soup.find_all('div' , class_='news-item')
    for i in res:
        i_title = i.find('div' , class_='news-text').text.strip()
        lst.append(i_title)

if __name__ == '__main__':
    func()
