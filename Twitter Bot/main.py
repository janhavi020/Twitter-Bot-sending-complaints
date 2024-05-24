from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PROMISED_DOWN = 158
PROMISED_UP = 10
CHROME_DRIVER_PATH = os.environ.get("driver_path")
TWITTER_EMAIL = os.environ.get("login_email")
TWITTER_PASSWORD = os.environ.get("login_password")
USER_NAME = os.environ.get("username")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        click_ok = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        click_ok.click()
        start = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        sleep(40)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        sleep(20)
        email = self.driver.find_element(By.NAME, value='text')
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        sleep(3)
        phn_no = self.driver.find_element(By.NAME, value='text')
        phn_no.send_keys(USER_NAME,Keys.ENTER)
        sleep(3)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        sleep(20)
        if int(float(self.up)) < int(float(PROMISED_UP)) or int(float(self.down)) < int(float(PROMISED_DOWN)):
            enter_message = self.driver.find_element(By.CLASS_NAME, value='public-DraftStyleDefault-block')
            sleep(2)
            enter_message.send_keys(f"Hey internet provider, why my internet speed is {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up!!")
            post_message = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            post_message.click()
            sleep(5)
        else:
            print("Good speed today!!")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


