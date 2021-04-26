from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import dbdata



class webmanager:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def get_page(self):
        self.driver.get("https://uv.frc.utn.edu.ar/course/view.php?id=4282")
        print("get")

    def locate_elements_on_login(self):
        self.get_page()
        print("locate")
        self.user_login_box = self.driver.find_element_by_name("username")
        self.password_login_box = self.driver.find_element_by_name("password")
        self.login_button = self.driver.find_element_by_id("loginbtn")

    def locate_elements_on_logout(self):
        self.dropdown_arrow = self.driver.find_element_by_link_text('Cerrar sesión')
        self.dropdown_arrow.click()


class webaccions(webmanager, dbdata.database_extract):
    def __init__(self):
        self.webmanager = webmanager()
        self.webmanager.locate_elements_on_login()
        self.user_login_box = self.webmanager.user_login_box
        self.password_login_box = self.webmanager.password_login_box
        self.login_button = self.webmanager.login_button

    def login_actions(self, user, password):
        self.user_login_box.send_keys(user)
        self.password_login_box.send_keys(password)
        self.login_button.click()  


    def work_flow(self):
        self.database_extract = dbdata.database_extract()
        self.allcredentials = self.database_extract.get_users_to_use()

        for i in self.allcredentials:
            
            self.parsed = self.database_extract.parse_information(i)
            self.user = self.parsed[0]
            self.password = self.parsed[1]
            print(self.user, self.password)
            self.login_actions(self.user, self.password)
            time.sleep(3)
            self.webmanager.locate_elements_on_logout()
            time.sleep(3)
            self.webmanager.locate_elements_on_login()

        self.webmanager.driver.close()    
