from selenium import webdriver
from time import sleep
from random import uniform
from getpass import getpass
from selenium.webdriver.common.keys import Keys

usuario = input("digite seu usuario do insta: ")
senha = getpass("digite sua senha do insta: ")
class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.driver.get('https://www.instagram.com/p/CHiQLRjnIg8/?igshid=6zw5rv08q1nk')
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
        for words in s:
            # pyautogui.click(x=600, y=800)
            text_area = self.driver.find_element_by_class_name("Ypffh")\
                .click()
            sleep(2)    
            self.driver.find_element_by_class_name("Ypffh")\
                .send_keys("@" + words)
            self.driver.find_element_by_class_name("Ypffh")\
                .send_keys(Keys.ENTER)
            print("comentario feito")
            time = uniform(30.0, 60.0)
            sleep(time)
InstaBot(usuario, senha)