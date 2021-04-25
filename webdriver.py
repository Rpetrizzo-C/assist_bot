from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import dbdata



class webmanager:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def get_page(self):
         self.driver.get("https://uv.frc.utn.edu.ar/course/view.php?id=4282")

    def locate_elements_on_loggin(self):
        self.get_page()

        self.user_login_box = self.driver.find_element_by_name("username")
        self.password_login_box = self.driver.find_element_by_name("password")
        self.login_button = self.driver.find_element_by_id("loginbtn")


class webaccions(webmanager, dbdata.database_extract):
    def __init__(self):
        self.webmanager = webmanager()
        self.webmanager.locate_elements_on_loggin()
        self.user_login_box = self.webmanager.user_login_box
        self.password_login_box = self.webmanager.password_login_box
        self.login_button = self.webmanager.login_button

    def send_accions_to_loggin(self):
        self.database_extract = dbdata.database_extract()
        self.parsed = self.database_extract.parse_information()
        self.user = self.parsed[0]
        self.password = self.parsed[1]
        self.user_login_box.send_keys(self.user)
        self.password_login_box.send_keys(self.password)
        self.login_button.click()

start = webaccions()
start.send_accions_to_loggin()        