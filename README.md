Для корректной работы коды, необходимо:  
  Python 3.8   
  Библиотеки:  
    •	requests – библиотека для составления HTTP запросов;  
    python -m pip install requests  
    •	BeautifulSoup - библиотека для анализа документов HTML и XML;  
      python -m pip install beautifulsoup4  
    •	lxml – библиотека для парсинга.  
      python -m pip install lxml  
Так же, по мимо выше перечисленных, я использовал следующие внутренние библиотеки:  
  •	sqlite3 – библиотека для доступа к базе данных SQL;  
  •	datetime – библиотека, предоставляющая классы для управления датами и временем;  
  •	os – библиотека предоставляющие ф-ции для работы с операционной системой;  
  •	codecs – библиотека для изменения кодеков, позволяет перекодировать файлы  
  •	zipfile – библиотека для работы с ZIP файлами  
  •	threading – библиотека для создания много-поточности (позволяет создавать дополнительные потоки, работающие параллельно)  
  •	time – библиотека, предоставляющая различные функции, связанные со временем  
Процесс:  
1.	Необходимо извлечь все файлы из архива, в одну папку, где будет проходить дальнейшая работа. Запас свободного места на диске, должен быть не менее 35 Гигабайт;  
2.	Необходимо открыть и запустить файл «CreateBD.py», в результате работы которого, в директории будет создан файл «data.db». В данный файл в дальнейшем будет записана информация, взятая с сайта;  
3.	После создания файла базы данных, необходимо открыть и запустить файл «Create_Index.py». Данный файл сделает копию страницы, и сохранит её в файл «index.html» для будущего парсинга. Данный шаг необходим, для того чтобы защита сайта не восприняла нас как бота;  
4.	После создания файла «index.html», необходимо запустить файл «Code.py», в результате работы данной программы будет заполнена база данных «data.db».  
5.	Далее необходимо запустить файл «redactBD.py», в результате его работы, таблица в базе данных, будет отредактирована, данную операцию нужно повторить несколько раз, пока программа перестанет выдавать дополнительную информацию, кроме одного числа (это размер таблицы);  
6.	После редактирования базы данных, нужно запустить файл «download.py», данный файл начнёт скачивать все файлы, взятые нами с сайта, и сохранять их в каталог, под необходимыми именами. Каждый файл, будет записан в свою категорию, и находиться в папке, название которой, это первые 100 символов из названия файла с сайта и дата его появления. (100 символов, т.к. в windiws есть ограничение на максимальную длину имени файла). В случае, если программа вылетит или выдаст ошибку в ходе работы, не нужно повторно её запускать, вместо этого необходимо запустить программу «download_add.py» которая продолжить скачивать файлы, с того момента где прервалась предыдущая программа. Так же есть программа, «download_add.py» которая работает так же, как и «download_add.py», но должна выдавать время своей работы, даже в случае вылета, но она не была испытана (так и не вылетела).   
ДАННЫЙ ЭТАП ЗАТЯНЕТСЯ НЕМЕНЕЕ ЧЕМ НА ЧАС, ИЗ-ЗА ОБЩЕГО ОБЪЁМА ФАЙЛОВ В 11 ГИГАБАЙ  
