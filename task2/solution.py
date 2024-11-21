import time

from bs4 import BeautifulSoup
import numpy as np
import requests


HOST = "https://ru.wikipedia.org"

stop = False
letters_dict = {chr(i): 0 for i in range(ord("А"), ord("Я")+1)}
response = requests.get("https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту")
soup = BeautifulSoup(response.content, 'html.parser')
while nav_page_tags := soup.select("#mw-pages > a"):
    groups = soup.select(".mw-category.mw-category-columns .mw-category-group")
    for group in groups:
        letter = group.select_one("h3").text
        if letter == "A":
            stop = True
            break
        print(letter)
        animals_count = len(group.select("ul li"))
        letters_dict[letter] += animals_count
    if stop:
        break
    if nav_page_tags[-1].text.lower().strip().replace(" ", "") == "предыдущаястраница":
        break
    time.sleep(.2)
    response = requests.get(HOST + nav_page_tags[-1].attrs["href"])
    soup = BeautifulSoup(response.content, 'html.parser')

np.savetxt("beasts.csv", [i for i in letters_dict.items()], delimiter=',', fmt='%s')
n = np.genfromtxt("beasts.csv", delimiter=",", dtype={"names": ("Letter", "Count"), "formats": ["U1", "i4"]})
print(n)
