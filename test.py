# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:46:28 2020

@author: gszufa
"""
import sqlite3
import pandas as pd

con = sqlite3.connect('authorsDB.db')

c = con.cursor()


df = pd.read_csv('author_book_publisher.csv')
df.to_sql('authors', con, if_exists = 'replace')

read = pd.read_sql('authors', con)



c.close()
con.close()
