from requests_html import HTMLSession
import json


def load_access_token_from_file(file_name='access_token.txt'):
    with open(file_name, mode='r') as f:
        result = f.readline().replace('\n','')
        print(result)
        return result


def shorten_url(access_token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    requests = HTMLSession()
    header = {
        'Authorization':'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'}
    requests.headers.update(header)
    print(requests.headers)
    data = '{"long_url":"https://dev.bitly.com"}'
    print(data)
    res = requests.post(api_url,json=data)
    print(res.content)
    return 'test'

if __name__ == "__main__":
    token = load_access_token_from_file('access_token.txt')
    print(shorten_url(token,'https://google.com/'))