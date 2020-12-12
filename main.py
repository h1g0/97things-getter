from requests_html import HTMLSession
import urllib.parse

base_url = 'https://xn--97-273ae6a4irb6e2hsoiozc2g4b8082p.com/'

def main():
    requests = HTMLSession()
    res = requests.get(base_url)
    links = res.html.find('a')
    with open('result.txt',mode='w',encoding='utf8') as f:
        for link in links:
            title = link.text
            url = urllib.parse.urljoin(base_url,link.attrs['href'])
            f.writelines('{} - {}\n'.format(title,url))
    
# エントリポイント
if __name__ == '__main__':
    main()