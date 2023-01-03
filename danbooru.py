import requests, os, re, time
from bs4 import BeautifulSoup
from settings import *
from modules import *

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
url_front = "https://danbooru.donmai.us/posts?page="
url_back = "&tags=keqing_%28genshin_impact%29&z=2"

file = open("rank.txt", "a")
data = open("data.txt", "r+")
page = int(data.read())
rank = {}
while page <= 272:
    while True:
        try:
            r = requests.get(url_front + str(page) + url_back, cookies=cookies, headers=headers)
        except requests.exceptions.ProxyError or requests.exceptions.SSLError:
            continue
        if r.status_code == 200:
            break
    soup = BeautifulSoup(r.text, 'lxml')

    pics = soup.find_all("article", class_="post-preview")
    for p in pics:
        id_raw = p.get('id')
        r = r"\d+"
        id = re.search(r, id_raw).group()
        score = int(p.get("data-score"))
        file.write(str(id) + ": " + str(score) + "\n")
    data.truncate(0)
    data.write(str(page + 1))
    if page % 20 == 0:
        file.close()
        file = open("rank.txt", "a")
    time.sleep(3)
    page += 1
