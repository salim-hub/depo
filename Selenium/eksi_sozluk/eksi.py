from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

driver.get(url)

time.sleep(5)

elements = driver.find_elements_by_css_selector(".content")

for element in elements:
    print("***************")
    print(element.text)

driver.close()

