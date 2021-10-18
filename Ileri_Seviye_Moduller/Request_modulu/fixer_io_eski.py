import requests
import sys

url = "http://data.fixer.io/api/"

birinci_doviz = input("Birinci Döviz: ")
ikinci_döviz = input("İkinci Döviz: ")

miktar = float(input("Miktarı giriniz: "))


response = requests.get(url + birinci_doviz)

json_verisi = response.json()   #çekilen veriyi json objesine çevirir.

try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)

except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()