import requests
import codecs

# Сoздание tml файла, с кодом страницы

url="https://lk.rs-class.org/regbook/rules?ln=ru"


req=requests.get(url)
src=req.text

with codecs.open('index.html','w', "utf_8_sig" ) as file:
    file.write(src)
