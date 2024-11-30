import requests
from bs4 import BeautifulSoup

url = 'https://www.hsestudyguide.com/iso-45001-lead-auditor-exam/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content)
text = soup.get_text()
print(text)