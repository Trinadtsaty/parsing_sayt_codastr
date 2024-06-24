import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS data(
    name TEXT,
    data TEXT,
    Rus_Url TEXT,
    Eng_Url TEXT);
""")
conn.commit()