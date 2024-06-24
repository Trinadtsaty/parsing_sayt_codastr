import zipfile
import os
from datetime import datetime
# Запоминаем время старта программы для подсчитывания времени её работы
time_start = datetime.now()

# создаём папку ZIP, если она ещё не была создана
if not os.path.isdir("ZIP"):
    os.mkdir("ZIP")

# записываем названия папок из директории download в переменную folders_download
folders_download=os.listdir(path="downlod")

# дём в цикле по переменным
for item in folders_download:
    with zipfile.ZipFile(f"ZIP/{item}.zip", "w") as zf:
        os.chdir("downlod")
        os.chdir(item)
        # Идём по деревьям до ПДФ файла, после чего добовляем его в ZIP архив
        for folder, subfolders, files in os.walk("."):
            for file in files:
                if file.endswith('.pdf'):
                    zf.write(os.path.join(folder, file))
        os.chdir("..")
        os.chdir("..")


# Создаём папку time и считаем время работы кода
if not os.path.isdir("time"):
    os.mkdir("time")
    os.chdir("time")
else:
    os.chdir("time")
time_stop = datetime.now()
time_documen = open("time_Zip_Posled.txt", "w")
time_documen.write(str(time_stop-time_start))
