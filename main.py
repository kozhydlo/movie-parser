from bs4 import BeautifulSoup
import requests
import random

import sqlite3

db = sqlite3.connect("Triangle_kino.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Triangle_kino(
    ID INTEGER PRIMARY KEY,
    RESURS TEXT,
    NAME TEXT,
    QUALITY TEXT,
    OPISANIE TEXT,
    LINK_STR TEXT
) """)

db.commit()

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

url = "https://uakino.club/filmy/"

while True:
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.text, "lxml")

    name_list = []
    quality_list = []
    link1_list = []
    opsanie_list = []

    # імя всіх фільмів в діві "movie-title"
    for name in page.find_all("a", class_="movie-title"):
        name_text = name.text
        print(name_text)
        name_list.append(name_text)

    # тут ми збираємо якісь всіх фільмів в діві "full-quality"
    for quality in page.find_all("div", class_="full-quality"):
        quality_text = quality.text
        print(quality_text)
        quality_list.append(quality_text)

    # Збираємо посилання на фільми
    for film in page.find_all("div", class_="movie-item short-item"):
        link_element = film.find("a", class_="movie-title")
        if link_element:
            link_str = link_element.get("href")
            print(link_str)
            link1_list.append(link_str)

    # Збираємо опис фільмів
    for link0 in link1_list:
        page2 = BeautifulSoup(requests.get(link0, headers=headers).text, "lxml")
        opisanie = page2.find("div", class_="full-text clearfix").text
        print(opisanie)
        
        b_split_list = opisanie.split("                        ")
    if len(b_split_list) > 1:
        bl = b_split_list[1]
        print(bl)

        link1_list.append(link_str)
        opisanie_list.append(bl)

    i = 0

    while i < len(opsanie_list):
        name1 = name_list[i]
        quality1 = quality_list[i]
        opisanie1 = opisanie_list[i]
        link2 = link1_list[i]

        cur.execute("""INSERT INTO Triangle_kino (RESURS, NAME, QUALITY, OPISANIE, LINK_STR) VALUES(?, ?, ?, ?, ?); """,
                    (resursZERO, name1, quality1, opisanie1, link2))
        db.commit()
        print(f"Добавлено запис: RESURS={resursZERO}, NAME={name1}, QUALITY={quality1}, OPISANIE={opisanie1}, LINK_STR={link2}")
        i += 1

x = x + 1
url = "https://uakino.club/filmy/page/" + str(x) + "/"


# це я не буду робити бо це буде дуже довго з кожної сторінки збирати фільми зроблю для тесту 2 
# if x == 230:
#     break

if x == 2:
    sys.exit()