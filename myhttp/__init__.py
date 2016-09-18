import requests

r = requests.get('https://api.github.com/user', auth=('csjxsw@sina.com', 'jx2333060'))
r.status_code

r.headers['content-type']

r.encoding

r.text

r.json()