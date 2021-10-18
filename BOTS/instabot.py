from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from secret import username, password


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\salim\PycharmProjects\BOTS\chromedriver.exe')
        self.username = username
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(5)

    def login(self):
        wait = WebDriverWait(self.driver, 10)
        user_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input'))
        user_in.send_keys(username)

        wait = WebDriverWait(self.driver, 10)
        password_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input'))
        password_in.send_keys(password)

        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button'))
        login_button.click()

        wait = WebDriverWait(self.driver, 10)
        popup1 = wait.until(lambda driver: self.driver.find_element_by_xpath("//button[contains(text(), 'Şimdi Değil')]"))
        popup1.click()

        wait = WebDriverWait(self.driver, 10)
        popup4 = wait.until(lambda driver: self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]"))
        popup4.click()

    def get_unfollowers(self):
        wait = WebDriverWait(self.driver, 10)
        click_username = wait.until(lambda driver: self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)))
        click_username.click()

        wait = WebDriverWait(self.driver, 100)
        following = wait.until(lambda driver: self.driver.find_element_by_xpath("//a[contains(@href,'/following')]"))
        following.click()
        following = self._get_names()

        wait = WebDriverWait(self.driver, 100)
        followers = wait.until(lambda driver: self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]"))
        followers.click()
        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        wait = WebDriverWait(self.driver, 10)
        scroll_box = wait.until(lambda driver: self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP"))
        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht
            sleep(3)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # close button
        wait = WebDriverWait(self.driver, 10)
        close_button = wait.until(lambda driver: self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button"))
        close_button.click()
        return names

    # def _get_names2(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     scroll_box2 = wait.until(lambda driver: self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]"))
    #     last_ht, ht = 0, 1

    #     while last_ht != ht:
    #         last_ht = ht
    #         sleep(3)
    #         ht = self.driver.execute_script("""
    #             arguments[0].scrollTo(0, arguments[0].scrollHeight); 
    #             return arguments[0].scrollHeight;
    #             """, scroll_box2)
    #     links2 = scroll_box2.find_elements_by_tag_name('a')
    #     names2 = [name.text for name in links2 if name.text != '']

    #     # close button
    #     wait = WebDriverWait(self.driver, 10)
    #     close_button = wait.until(lambda driver: self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button"))
    #     close_button.click()
    #     return names2



bot = InstaBot(username, password)
bot.login()
bot.get_unfollowers()