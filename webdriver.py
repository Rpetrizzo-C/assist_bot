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

    def locate_assist_button(self):
        self.assist_link = self.driver.find_element_by_link_text("Asistencia")    

    def reload(self):
        self.driver.refresh()

    def be_pressent(self):
        self.driver.execute_script("window.scrollTo(0,900)")
        self.locate_assist_button()
        self.assist_link.click()
        self.set_assist_link = self.driver.find_element_by_link_text("Enviar asistencia")
        self.set_assist_link.click()
        self.pressent_circle = self.driver.find_element_by_id("id_status_17477")
        self.pressent_circle.click()
        self.set_assist_button = self.driver.find_element_by_id("id_submitbutton")
        self.set_assist_button.click()



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
            self.located = False
            while self.located == False:
                try:
                    self.webmanager.be_pressent()
                    self.located = True
                except NoSuchElementException:
                    
                    self.webmanager.reload()
                    self.located = False 
                    time.sleep(10)
            self.webmanager.locate_elements_on_logout()
            self.webmanager.locate_elements_on_login()

        self.webmanager.driver.close()    
