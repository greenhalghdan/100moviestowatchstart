import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

web_page = response.text

#print(web_page)

soup = BeautifulSoup(web_page, "html.parser")

films = soup.find_all("h3", class_="title")

for film in films:
    print(film.getText())
    try:
        with open("movies.txt", "r", encoding="utf-8") as current:
            data = current.read()
    except FileNotFoundError:
        open("movies.txt", "x", encoding="utf-8")
    with open("movies.txt", "w", encoding="utf-8") as file:
        try:
            file.write(f"{film.getText()}\n{data}")
        except NameError:
            file.write(f"{film.getText()}")


# with open('filename', 'r') as original: data = original.read()
# with open('filename', 'w') as modified: modified.write("new first line\n" + data)