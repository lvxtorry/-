import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
#станция, год, месяц, день, час, направление ветра, осадки, температуа, влажность
cursor.execute("""
    CREATE TABLE IF NOT EXISTS station(
    inducations INT PRIMARY KEY,
    stname TEXT,
    year INT,
    month INT,
    day INT,
    hour INT,
    dirwild TEXT,
    precipit REAL,
    temperature REAL,
    humidity REAL);"""
    )

conn.commit()