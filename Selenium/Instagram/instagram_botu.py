from selenium import webdriver
from time import sleep
from loginInfo import username, password

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.maximize_window()
sleep(3)

username_label = driver.find_element_by_name("username")
username_label.send_keys(username)
password_label = driver.find_element_by_name("password")
password_label.send_keys(password)

giris_yap_butonu = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
giris_yap_butonu.click()

sleep(10)

pop_up = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
pop_up.click()

pop_up2 = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
pop_up2.click()

profileButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div/div[1]/div")
profileButton.click()

followersButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followersButton.click()

