from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from secret import username, password


class TwBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\salim\PycharmProjects\BOTS\chromedriver.exe')

        self.username = username
        self.driver.get("https://twitter.com/home")
        self.driver.maximize_window()
        sleep(5)

    def login(self):
        wait = WebDriverWait(self.driver, 10)
        user_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'))
        user_in.send_keys(username)

        wait = WebDriverWait(self.driver, 10)
        password_in = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'))
        password_in.send_keys(password)

        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'))
        login_button.click()

        wait = WebDriverWait(self.driver, 10)
        profile = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/a/div[2]'))
        profile.click()

        wait = WebDriverWait(self.driver, 10)
        all_likes = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/nav/div/div[2]/div/div[4]'))
        all_likes.click()

    def unlike(self):
        wait = WebDriverWait(self.driver, 10)
        unlike = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="id__650zp7tuzrg"]/div[3]/div/div/div[1]/div'))
        unlike.click()

# setInterval(() => {
#   for (const d of document.querySelectorAll('div[data-testid="unlike"]')) {
#     d.click()
#   }
#   window.scrollTo(0, document.body.scrollHeight)
# }, 1000)


    def unlike_all(self):
        
        while True:
            # Scroll down to bottom
            wait = WebDriverWait(self.driver, 1000)
            wait.until(lambda driver: self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)"))
        
            # Calculate new scroll height and compare with last scroll height
            wait = WebDriverWait(self.driver, 1000)            
            new_height = wait.until(lambda driver: self.driver.execute_script("return document.body.scrollHeight"))

            # break condition
            if new_height == last_height:
                break
            last_height = new_height
            

            

bot = TwBot(username, password)
bot.login()
bot.unlike_all()
