from selenium import webdriver
from time import sleep
import pyautogui
from random import uniform
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usuario = input("digite seu usuario do insta: ")
senha = getpass("digite sua senha do insta: ")
class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.driver.get('link da publicação')
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)
        sleep(3)
        s = open("./text.txt", "r")
        a = 1
        for words in s:
            sleep(5)
            # pyautogui.click(x=600, y=800)
            text_area = self.driver.find_element_by_class_name("Ypffh")\
                .click()
            sleep(2)    
            self.driver.find_element_by_class_name("Ypffh")\
                .send_keys("@" + words)
            self.driver.find_element_by_class_name("Ypffh")\
                .send_keys(Keys.ENTER)
            print("comentario feito")
            print(a)
            time = uniform(30.0, 60.0)
            sleep(time)
            a = a + 1
InstaBot(usuario, senha)