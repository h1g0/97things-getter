import time
import urllib.parse

from requests_html import HTMLSession

from shorten_url import load_access_token_from_file, shorten_url

base_url = 'https://xn--97-273ae6a4irb6e2hsoiozc2g4b8082p.com/'
make_url_short = True

def main():
    requests = HTMLSession()
    res = requests.get(base_url)
    links = res.html.find('ol',first = True).find('a')
    token = ''
    if make_url_short:
        token = load_access_token_from_file('access_token.txt')
    with open('result.txt',mode='w',encoding='utf8') as f:
        for link in links:
            title = link.text
            url = urllib.parse.urljoin(base_url,link.attrs['href'])

            if make_url_short:
                url = shorten_url(token,url)
                time.sleep(1)
            print('{} - {}'.format(title,url))
            f.writelines('{} - {}\n'.format(title,url))
    
# エントリポイント
if __name__ == '__main__':
    main()
