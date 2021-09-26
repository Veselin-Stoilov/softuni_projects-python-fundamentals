data = input()
url_list = []
import re
pattern = r'(?P<email>www(\.)[A-Za-z0-9\-]+(\.)[a-z\.]+)'
while data != '':
    valid_urls = re.finditer(pattern, data)
    for match in valid_urls:
        url_list.append(match.group())
    data = input()
for url in url_list:
    print(url)