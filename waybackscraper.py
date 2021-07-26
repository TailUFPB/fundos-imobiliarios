from logging import exception
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

urls = ["https://web.archive.org/web/20161115035831/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20161231151111/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20170427071347/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20170528171838/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20170628231303/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20170731002400/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20170831030312/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20171001130049/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20171101213831/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20171204063605/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180105215805/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180206152413/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180310103209/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180403075219/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180510014107/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180605202706/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180719112345/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180820030324/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20180922182927/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20181025163800/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20181128135225/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20181217222839/http://www.fundsexplorer.com.br:80/ranking",
    "https://web.archive.org/web/20190114205401/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20190208101643/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20200313180727/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20200919165821/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20200928043253/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20201022010221/https://www.fundsexplorer.com.br/ranking",
    "https://web.archive.org/web/20201202223051/https://www.fundsexplorer.com.br/ranking"
]

path = "chromedriver.exe"

for url in urls:
    

    browser = webdriver.Chrome(path)
    browser.get(url)

    data = browser.find_element_by_tag_name("table")
    html_table = data.get_attribute("outerHTML")

    soup = BeautifulSoup(html_table, "html.parser")
    table = soup.find(name="table")

    pd.read_html(str(table))[0].to_csv(url[28:42]+".csv", sep=";")