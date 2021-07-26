from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.fundsexplorer.com.br/ranking"
path = "chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get(url)

data = browser.find_element_by_xpath('//*[@id="table-ranking"]')
html_table = data.get_attribute("outerHTML")

soup = BeautifulSoup(html_table, "html.parser")
table = soup.find(id="table-ranking")

df = pd.read_html(str(table))[0]
print(df)

df.to_csv("fundos imobiliarios.csv", sep=";")


browser.quit()
