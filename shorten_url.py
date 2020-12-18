from requests_html import HTMLSession
import json


def load_access_token_from_file(file_name: str = 'access_token.txt') -> str:
    with open(file_name, mode='r') as f:
        result = f.readline().replace('\n', '')
        return result


def shorten_url(access_token: str, url: str) -> str:
    api_url = 'https://api-ssl.bitly.com/v3/shorten'
    param = {
        "access_token": access_token,
        "longUrl": url
    }
    req = HTMLSession()
    res = req.request('GET', api_url, params=param)
    return res.json()['data']['url']


'''
def shorten_url(access_token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    requests = HTMLSession()
    header = {
        'Authorization':'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'}
    requests.headers.update(header)
    data = json.dumps({"long_url":url})
    res = requests.post(api_url,json=data)
    return res.json['link']
'''
if __name__ == "__main__":
    token = load_access_token_from_file('access_token.txt')
    print(shorten_url(token, 'https://google.com/'))
