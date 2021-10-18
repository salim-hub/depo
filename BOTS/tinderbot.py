from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.support.ui import WebDriverWait


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(3)
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://tinder.com')

        wait = WebDriverWait(self.driver, 10)
        popup1 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button'))
        popup1.click()

        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'))
        login_button.click()

        wait = WebDriverWait(self.driver, 30)
        fb_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'))
        fb_button.click()
        
        sleep(5)

        base_window = self.driver.current_window_handle

        for handle in self.driver.window_handles:
            if handle != base_window:
                print(handle)
                new_window = handle
                break

        self.driver.switch_to.window(new_window)

        
        #base_window = self.driver.window_handles[0]

        #wait = WebDriverWait(self.driver, 30)
        #new_window = wait.until(lambda driver: self.driver.window_handles[1])
        #self.driver.switch_to.window(new_window)

        wait = WebDriverWait(self.driver, 10)
        email_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="email"]'))
        email_in.send_keys(username)

        wait = WebDriverWait(self.driver, 10)
        pw_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="pass"]'))
        pw_in.send_keys(password)

        wait = WebDriverWait(self.driver, 10)
        enter_button= wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="u_0_0"]'))
        enter_button.click()

        self.driver.switch_to.window(base_window)

        wait = WebDriverWait(self.driver, 10)
        popup2 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'))
        popup2.click()

        wait = WebDriverWait(self.driver, 10)
        popup3 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'))
        popup3.click()

        wait = WebDriverWait(self.driver, 10)
        popup4 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]'))
        popup4.click()

    def like(self):
        wait = WebDriverWait(self.driver, 10)
        like_btn = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'))
        like_btn.click()

    def dislike(self):
        wait = WebDriverWait(self.driver, 10)
        dislike_btn = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button'))
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        wait = WebDriverWait(self.driver, 10)
        popup_3 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]'))
        popup_3.click()

    def close_match(self):
        wait = WebDriverWait(self.driver, 10)
        match_popup = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'))
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()

