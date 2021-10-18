from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class WhatsApp_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(3)
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com/')

        sleep(5)

        name = input("To whom will you send the message?: ")

        wait = WebDriverWait(self.driver, 30)
        user = wait.until(lambda driver: self.driver.find_element_by_xpath("//span[@title='{}']".format(name)))
        user.click()

        message = input("What is your message?: ")

        wait = WebDriverWait(self.driver, 30)
        write_message = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
        write_message.send_keys(message)

        send_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button'))
        send_button.click()

bot = WhatsApp_Bot()