import time
import urllib.parse
from types import Final

from requests_html import HTMLSession

from shorten_url import load_access_token_from_file, shorten_url


def main():
    """『プログラマが知るべき97のこと』の各エッセイのURLを取得する
    """
    #BASE_URL: Final = 'https://xn--97-273ae6a4irb6e2hsoiozc2g4b8082p.com/'
    BASE_URL: Final = 'https://ja.wikisource.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9E%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D97%E3%81%AE%E3%81%93%E3%81%A8'
    MAKE_URL_SHORT: Final = False  # URLを短縮するか否かのフラグ

    requests = HTMLSession()
    res = requests.get(BASE_URL)
    links = res.html.find('ol', first=True).find('a')
    token = ''

    if MAKE_URL_SHORT:
        token = load_access_token_from_file('access_token.txt')
    with open('result.txt', mode='w', encoding='utf8') as f:
        for link in links:
            title = link.text
            url = urllib.parse.urljoin(BASE_URL, link.attrs['href'])

            if MAKE_URL_SHORT:
                url = shorten_url(token, url)
                time.sleep(1)
            print(f'{title} - {url}')
            f.writelines(f'{title} - {url}\n')


# エントリポイント
if __name__ == '__main__':
    main()
