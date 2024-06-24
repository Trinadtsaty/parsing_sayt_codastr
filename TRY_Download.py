import os
import re
import sqlite3
import requests
from datetime import datetime
time_start = datetime.now()


conn = sqlite3.connect('data.db')
cur = conn.cursor()
try:
    if not os.path.isdir("downlod"):
        os.mkdir("downlod")
        os.chdir("downlod")
        os.mkdir("Правила")
        os.mkdir("Руководства")
        os.mkdir("Освидетельствование и сертификация систем менеджмента")
        os.mkdir("Рекомендации, методики, справочники, нормативно-методические указания")
        os.mkdir("Научно-технический сборник")
        os.mkdir("Дайджест")
    else:
        os.chdir("downlod")

    # вывести текущую директорию
    # print("Текущая деректория:", os.getcwd())
    # изменение текущего каталога на 'folder'
    # os.chdir("folder")
    # вернуться в предыдущую директорию
    # os.chdir("..")

    cur.execute("""SELECT * from data""")
    records = cur.fetchall()
    folder_1='Правила'
    dop_1=1
    folder_2='Руководство'
    dop_2=1
    folder_3='Положение по освидетельствованию'
    dop_3=1
    folder_4=None
    dop_4=1
    folder_5='Научно-технический'
    dop_5=1
    folder_6='Дайджест'
    dop_6=1
    for i in records:
        name=i[0]
        data=i[1]
        Rus_URL=i[2]
        Eng_URL=i[3]
        if folder_1 in name:
            os.chdir("Правила")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_1)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_1)+")")
                dop_1+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")

        elif folder_2 in name:
            os.chdir("Руководства")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_2)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_2)+")")
                dop_2+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")
        elif folder_3 in name:
            os.chdir("Освидетельствование и сертификация систем менеджмента")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_3)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_3)+")")
                dop_3+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")
        elif folder_5 in name:
            os.chdir("Научно-технический сборник")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_5)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_5)+")")
                dop_5+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")
        elif folder_6 in name:
            os.chdir("Дайджест")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_6)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_6)+")")
                dop_6+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")
        else:
            os.chdir("Рекомендации, методики, справочники, нормативно-методические указания")
            if not os.path.isdir(name+' ' + data):
                os.mkdir(name+' ' + data)
                os.chdir(name + ' ' + data)
            else:
                os.mkdir(name + ' ' + data + " (" + str(dop_4)+")")
                os.chdir(name + ' ' + data + " (" + str(dop_4)+")")
                dop_4+=1
            os.mkdir("Eng")
            os.mkdir("Rus")
            if Rus_URL != None:
                response = requests.get(Rus_URL)
            if response.status_code == 200:
                file_rus = f'Rus/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            if Eng_URL != None:
                response = requests.get(Eng_URL)
            if response.status_code == 200:
                file_rus = f'Eng/{data}.pdf'
                with open(file_rus, 'wb') as file:
                    file.write(response.content)
            os.chdir("..")
            os.chdir("..")



    if not os.path.isdir("time"):
        os.mkdir("time")
        os.chdir("time")
    else:
        os.chdir("time")
    time_stop = datetime.now()
    time_documen = open("TRY_Download.txt", "w")
    time_documen.write(str(time_stop - time_start))

except:
    if not os.path.isdir("time"):
        os.mkdir("time")
        os.chdir("time")
    else:
        os.chdir("time")
    time_stop = datetime.now()
    time_documen = open("TRY_Download.py", "w")
    time_documen.write(str(time_stop - time_start))
