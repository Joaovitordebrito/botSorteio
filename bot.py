from selenium import webdriver
from time import sleep
import pyautogui
from random import uniform

usuario = input("digite seu usuario do insta: ")
senha = input("digite sua senha do insta: ")
class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.driver.get('https://www.instagram.com/p/CG_R1RvDB25/')
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
            pyautogui.click(x=600, y=800)
            pyautogui.typewrite("@" + words)
            pyautogui.press("enter")
            time = uniform(30.0, 60.0)
            sleep(time)
InstaBot(usuario, senha)