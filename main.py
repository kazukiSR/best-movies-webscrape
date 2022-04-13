import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movieNames = [element.getText() for element in soup.find_all(name="h3", class_="title")]

with open('movie_names.txt', 'w') as file:
    for i in reversed(movieNames):
        file.write(f"{i}\n")
