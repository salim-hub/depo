import requests     #web sayfasından bilgiler request ile çekilir
from bs4 import BeautifulSoup   #web sayfası içindeki bilgiler BS ile çekilir.(mesela a etiketleri, div etiketler vs.)

url = "https://www.trendyol.com/sr/erkek-x-g2?cid=577097"
response = requests.get(url)    # get fonksiyonu sayesinde sayfanın tüm özelliklerine sahip olunur.

# print(response) # <Response [200]> --web sayfasından bilgileri çekebildiğimiz anlamına geliyor.

html_icerigi = response.content  #content ile içeriği alabiliriz

soup = BeautifulSoup(html_icerigi, "html.parser")   # dökümanı daha güzel göstermek için

# print(soup.prettify())  # web sayfasının içeriği görüntülemek için prettify fonksiyonu.


# bütün a etiketlerini almak için
# print(soup.find_all("a"))   

# for i in soup.find_all("a"):
#     print(i)
#     print("***********************")

# for i in soup.find_all("a"):
#     print(i.get("href"))        #a etiketinin href parametrelerinin değerlirini almak için
#     print("***********************")


# for i in soup.find_all("a"):
#     print(i.text)               # a etiketlerinin içindeki yazıları almak için
#     print("***********************")


print(soup.find_all("div", {"class": "p-card-wrppr"}))  #sadece div içindeki class ı almak için






