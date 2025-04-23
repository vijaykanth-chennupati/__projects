import sqlite3
import pandas as pd
box = pd.read_csv("AB_NYC_2019.csv")
connection = sqlite3.connect("airbnb_project.db")

box.to_sql("airbnb", connection, if_exists="replace", index=False)
print(connection.execute("select name, host_name, price from airbnb order by price desc limit 5").fetchall())
print(connection.execute("select room_type, avg(price) as avg_price from airbnb group by room_type").fetchall())
print(connection.execute("select name, number_of_reviews, price from airbnb where number_of_reviews>100 order by number_of_reviews desc").fetchall())
