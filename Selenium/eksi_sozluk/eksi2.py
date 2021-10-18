from selenium import webdriver
import time
import random


driver = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,1290)
    newUrl = url + str(randomPage)
    driver.get(newUrl)

    elements = driver.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

for entry in entries:
    print(str(entryCount) + "***************************")
    print(entry)
    entryCount += 1

driver.close()
