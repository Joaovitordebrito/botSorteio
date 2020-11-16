from selenium import webdriver
from time import sleep
import pyautogui
from random import uniform
import os

os.environ['DISPLAY'] = ':0'

usuario = input("digite seu usuario do insta: ")
senha = input("digite sua senha do insta: ")
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
            self.driver.find_element_by_class_name("Ypffh")\
                .click()
            pyautogui.typewrite("@" + words)
            pyautogui.press("enter")
            print("comentario feito")
            time = uniform(30.0, 60.0)
            sleep(time)
InstaBot(usuario, senha)