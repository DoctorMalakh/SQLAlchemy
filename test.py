# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:46:28 2020

@author: gszufa
"""
import pandas as pd

df = pd.read_csv("author_book_publisher.csv")


df.assign(name=df.first_name.str.cat(df.last_name, sep=" ").groupby(["publisher"]).loc[:, "name"].sort_values(ascending=True))