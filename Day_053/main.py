from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website,"html.parser")
tagsss= soup.find_all(name="h3", class_="title")
movie_list =[]
for title in tagsss:
    movie_list.append(title.getText())
rev= movie_list[::-1]
print(rev)
with open("Top 100 Movie List.txt","w",encoding="utf-8") as file:
    for movies in rev:
        file.write(movies)
        file.write("\n")
print("Movie List Created Successfully")


