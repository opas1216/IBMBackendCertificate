import requests


url = 'https://www.ibm.com/'
r = requests.get(url)
print(f'r.status_code = {r.status_code}')
print(f'r.request.headers = {r.request.headers}')
print(f'r.request.body = {r.request.body}')
print(f'r.headers = {r.headers}')
