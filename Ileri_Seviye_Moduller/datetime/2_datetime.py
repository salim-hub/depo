from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL, "") # çıktıları türkçe almak için

tarih = datetime(2019, 12, 1)

su_an = datetime.now()

print(tarih - su_an)