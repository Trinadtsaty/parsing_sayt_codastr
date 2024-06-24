import threading
import time
import zipfile
import os
from datetime import datetime
time_start = datetime.now()

if not os.path.isdir("ZIP_Potok"):
    os.mkdir("ZIP_Potok")

folders_download=os.listdir(path="downlod")
# Создаём функциб для архивирования файлов из директории, поступаемой при иницации
def ZIP_ing(item):
    with zipfile.ZipFile(f"ZIP_Potok/{item}.zip", "w") as zf:
        for folder, subfolders, files in os.walk(f"downlod/{item}"):
            for file in files:
                if file.endswith('.pdf'):
                    zf.write(os.path.join(folder, file))


# СОздаём массив, в котором будут содержаться потоки, для взаимодействия с ними
threads = []
j=0
t=[]*len(folders_download)
for item in folders_download:
    t = threading.Thread(target=ZIP_ing, args=(item, ))
    t.name = f"{item}"
    threads.append(t)
    t.start()

# Функция, которая будет каждый 10 секунд выводить сколько прошло времени, с момента старта програмы, она ориентируется по 4-ому потоку, в котором архивируется самый массивный архив
while threads[3].is_alive():
    time.sleep(10)
    time_abz = datetime.now()
    print(str(time_abz - time_start))

# Метод который не будет выполнять следующий за ним код, до тех пор пока 4-ый поток, не завершиться (взят 4-ый поток, т.к. он самый большой)
threads[3].join()






if not os.path.isdir("time"):
    os.mkdir("time")
    os.chdir("time")
else:
    os.chdir("time")

time_stop = datetime.now()
time_documen = open("time_Zip_Parall.txt", "w")
time_documen.write(str(time_stop-time_start))

# Сигнал выплнения программы
print("finish")
