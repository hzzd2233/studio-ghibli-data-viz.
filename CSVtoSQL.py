import sqlite3
import pandas as pd

csv = pd.read_csv("movies.csv")
sql = sqlite3.connect("movies.db")

csv.to_sql("Movies", sql, if_exists="replace", index=False)

res = sql.execute("SELECT id, title, director, release_date, rt_score FROM Movies LIMIT 5;").fetchall()
print(res)

sql.close()






