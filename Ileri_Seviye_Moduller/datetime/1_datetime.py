from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL, "") # çıktıları türkçe almak için

# print(datetime.now())

su_an = datetime.now()

# print(su_an.year)
# print(su_an.month)
# print(su_an.microsecond)
# print(su_an.hour)

# print(datetime.ctime(su_an))

# print(datetime.strftime(su_an, "%Y"))

# print(datetime.strftime(su_an, "%B"))

# print(datetime.strftime(su_an, "%A"))

# print(datetime.strftime(su_an, "%B %Y"))

# print(datetime.strftime(su_an, "%Y %B %A"))

saniye = datetime.timestamp(su_an)
print(saniye)

suan2 = datetime.fromtimestamp(saniye)
print(suan2)