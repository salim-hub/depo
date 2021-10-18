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

with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + "\n" + entry + "\n")
        file.write("**************************************************************************************")
        entryCount += 1

driver.close()
