# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:46:28 2020

@author: gszufa
"""
import sqlite3
import pandas as pd

con = sqlite3.connect('books.db')

c = con.cursor()


df = pd.read_csv('author_book_publisher.csv')
df.to_sql('authors', con, if_exists = 'append')

read = pd.read_sql('SELECT * FROM authors WHERE first_name = "Stephen"', con)



c.close()
con.close()

print('done')