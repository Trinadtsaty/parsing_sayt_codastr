import sqlite3
import os
from datetime import datetime
time_start = datetime.now()
conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("""SELECT * from data""")
records = cur.fetchall()
c=0
print(len(records))
# Обрезание лишних частей в название которые иногда попадают в name из-за не одинаковой структуры контейнеров
for i in records:
    name = i[0]
    error = 'Рус.'
    if error in name:
        name_new = name.split('Рус.')
        name_new = name_new[0]
        query = """Update data set name = ? where name = ?"""
        perem = (name_new, name)
        cur.execute(query, perem)
        conn.commit()

# Обрезание имени слишком больших файлов (сохраняем первые 100 символов)
for i in records:
    name = i[0]
    if len(name)>100:
        name_new=name[:100]
        query = """Update data set name = ? where name = ?"""
        perem=(name_new, name)
        cur.execute(query,perem)
        conn.commit()
        print(name_new)
        print('1')

# Замена символов запрещённых в имени файла
for i in records:
    name = i[0]
    rep=['/','\\','|',':','*','?','"','<','>']
    for item in rep:
        if item in name:
            name_new=name.replace(item, "_")
            query = """Update data set name = ? where name = ?"""
            perem=(name_new, name)
            cur.execute(query,perem)
            conn.commit()

if not os.path.isdir("time"):
    os.mkdir("time")
    os.chdir("time")
else:
    os.chdir("time")
time_stop = datetime.now()
time_documen = open("redactBD.txt", "w")
time_documen.write(str(time_stop-time_start))
