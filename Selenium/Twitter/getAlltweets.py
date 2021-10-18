from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from loginInfo import username, password, email

class TwitterBot():
    def __init__(self, username, password, email):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/")
        sleep(5)

    def TwLogin(self):
        wait = WebDriverWait(self.driver, 10)
        giris_yap = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span'))
        giris_yap.click()

        wait = WebDriverWait(self.driver, 10)
        username_ile_giris = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span'))
        username_ile_giris.click()

        wait = WebDriverWait(self.driver, 10)
        username_gir = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
        username_gir.send_keys(username)

        wait = WebDriverWait(self.driver, 10)
        ileri_butonu = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))
        ileri_butonu.click()

        try:
            wait = WebDriverWait(self.driver, 10)
            mail_gir = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
            mail_gir.send_keys(email)

            wait = WebDriverWait(self.driver, 10)
            ileri_butonu2 = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))
            ileri_butonu2.click()

            wait = WebDriverWait(self.driver, 10)
            password_gir = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'))
            password_gir.send_keys(password)

        except:
            wait = WebDriverWait(self.driver, 10)
            password_gir = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'))
            password_gir.send_keys(password)

        wait = WebDriverWait(self.driver, 10)
        giris_yap_butonu = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'))
        giris_yap_butonu.click()

        # wait = WebDriverWait(self.driver, 10)
        # profile_git = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/a/div[2]'))
        # profile_git.click()
        
        # wait = WebDriverWait(self.driver, 10)
        # begenilere_git = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[4]/a/div'))
        # begenilere_git.click()

        wait = WebDriverWait(self.driver, 10)
        searchArea = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))
        searchArea.send_keys("pythoncoding")
        searchArea.send_keys(Keys.RETURN)

    def unlike_tweets(self):
        wait = WebDriverWait(self.driver, 10)
        like_button = wait.until(lambda driver: self.driver.find_element_by_css_selector(''))
        
        for tweetsss in like_button:
            try:
                lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match=False
                while(match==False):
                    lastCount = lenOfPage
                    sleep(2)
                    lenOfPage = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount == lenOfPage:
                        match=True
                sleep(2)
                like_button.click()
                sleep(1)
            except Exception:
                print("Bir sorun oluştu...")
        
        # FETCHING TWEETS
        # wait = WebDriverWait(self.driver, 20)
        # elements = wait.until(lambda driver: self.driver.find_elements_by_css_selector(""))
        # for element in elements:
        #     print("*********************************************************************")
        #     print(element.txt)


        


bot = TwitterBot(username, password, email)
bot.TwLogin()
bot.unlike_tweets()