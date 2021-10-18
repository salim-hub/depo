import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")


a = float(input("Rating'i giriniz: "))

# for i in soup.find_all("td", {"class": "titleColumn"}):
#     print(i.text)
#     print("**********************")

basliklar = soup.find_all("td", {"class": "titleColumn"})

ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})

# print(len(basliklar), len(ratingler))

# zip fonksiyonu ile iki listeyi birleştirebiliriz
for baslik, rating in zip(basliklar, ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip() #baştaki ve sondaki boşlukları silmek için
    baslik = baslik.replace("\n", "")

    rating = rating.strip() #baştaki ve sondaki boşlukları silmek için
    rating = rating.replace("\n", "")

    # print("Başlık: ", baslik)
    # print("Rating: ", rating)
    # print("---------------------------")

    if (float(rating) > a):
        print("Film ismi: {}\nFilmin Rating'i: {}".format(baslik, rating))

