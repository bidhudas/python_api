#!/usr/bin/python3

import pandas as pd

import matplotlib.pyplot as plt

### building a dataframe
excel_file = 'movies.xls'

movies = pd.read_excel(excel_file)

#### working with a dataframe

print(movies.head())


movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

print(movies_sheet1.head())

movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)

print(movies_sheet2.head())

movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

print(movies_sheet3.head())

###
allmovies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

# get some info about the single dataframe
print(allmovies.shape)

sorted_by_gross = allmovies.sort_values(["Gross Earnings"], ascending=False)

print(sorted_by_gross["Gross Earnings"].head(10))


##### build a graph
#sorted_by_gross["Gross Earnings"].head(10).plot(kind="barh")
#plt.savefig("stackedbar.png")


movies['IMDB Score'].plot(kind="hist")
plt.savefig("imdbscore.png")


export_excel = allmovies.to_excel("bigdataset.xlsx", index = None, header=True)
