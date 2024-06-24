import requests
from bs4 import BeautifulSoup
import codecs
import sqlite3
import os
from datetime import datetime
#время начала работы программы, для подсчета времени её выполнения
time_start = datetime.now()

conn = sqlite3.connect('data.db')

cur = conn.cursor()


# Часть кода для создания индекс файла, для удобства вынесена в отдельный файл
# url = 'https://lk.rs-class.org/regbook/rules?ln=ru'
# page = requests.get(url)
# src = page.text
# with codecs.open('index.html','w', "utf_8_sig" ) as file:
#     file.write(src)


# Открытие индекс файла
with codecs.open('index.html', 'r', "utf_8_sig") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")

# Поиск по файлу, всех контейнеров с классом "mainDocument" и сохранение их в переменную find_text
find_text = soup.find_all(class_="mainDocument")


# Цикли в котором мы идём по ранее сохраненым контейнерам, выделяя названия, дату загрузки, ссылку на документ на русском и на английсом языках
for i in find_text:
    data = i.next_element.next_element.text
    name = i.find_all("td")
    name = name[2].text
    name= name[:len(name) - 11]
    if i.find("a", string="Рус.") != None:
        Rus_url = "https://lk.rs-class.org/regbook/" + i.find("a", string="Рус.").get("href")
    else:
        Rus_url = None
    if i.find("a", string="Eng.") != None:
        Eng_url = "https://lk.rs-class.org/regbook/" + i.find("a", string="Eng.").get("href")
    else:
        Eng_url = None

    # Добавление файлов в базу данных
    data1=(name, data, Rus_url, Eng_url)
    cur.execute("INSERT INTO data VALUES(?, ?, ?, ?)", data1)
    conn.commit()

# Создание папки time (если её не было) и сохранение в ней файла "Parsing.txt" с временем выполнения кода
if not os.path.isdir("time"):
    os.mkdir("time")
    os.chdir("time")
else:
    os.chdir("time")
time_stop = datetime.now()
time_documen = open("Parsing.txt", "w")
time_documen.write(str(time_stop-time_start))