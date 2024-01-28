# Importing libraries

from bs4 import BeautifulSoup
import requests

# Connecting to the website

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_Kingdom'

page = requests.get(url)

soup = BeautifulSoup(page.text , 'html')

print(soup.prettify())

print('=' * 99)

table = soup.find('table')

print(table)

print('=' * 99)

table_headers = table.find_all('th')

print(table_headers)

print('=' * 99)

table_headers_text = [title.text.strip() for title in table_headers]

print(table_headers_text)

print('=' * 99)

# Creating the DataFrame

import pandas as pd

df = pd.DataFrame(columns=table_headers_text)

column_data = table.find_all('tr')

print(column_data)

print('=' * 100)

for row in column_data[1:]:
    row_data = row.find_all('td')
    single_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = single_row_data
    
print(df)

# Saving the dataframe to a csv file

import os

# Make sure the directory exists
directory = r"F:\Projects\Python"
if not os.path.exists(directory):
    os.makedirs(directory)

# Saving the dataframe to a csv file
df.to_csv(os.path.join(directory, "Wiki_web_scraping_project_UK.csv"), index=False)

# -- End of project ^^ --