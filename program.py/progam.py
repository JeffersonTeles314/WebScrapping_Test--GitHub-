import requests
import BeautifulSoup
 
r = requests.get('http://www.reddit.com/r/programming/')
soup = BeautifulSoup.BeautifulSoup(r.content)
for a in soup.findAll('a', attrs={'class': 'title '}):
    print(a.text)