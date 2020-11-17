import os 
from selenium import webdriver
from time import sleep
from random import uniform
from getpass import getpass
from selenium.webdriver.common.keys import Keys


op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
usuario = input("digite seu usuario do insta: ")
senha = getpass("digite sua senha do insta: ")

driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
driver.get('https://www.instagram.com/p/CHiQLRjnIg8/?igshid=6zw5rv08q1nk')
sleep(2)
driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]")\
    .click()
sleep(2)
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(usuario)
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(senha)
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(4)
driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
    .click()
sleep(2)
sleep(3)
s = open("./text.txt", "r")
for words in s:
    # pyautogui.click(x=600, y=800)
    text_area = driver.find_element_by_class_name("Ypffh")\
        .click()
    sleep(2)    
    driver.find_element_by_class_name("Ypffh")\
        .send_keys("@" + words)
    driver.find_element_by_class_name("Ypffh")\
        .send_keys(Keys.ENTER)
    print("comentario feito")
    time = uniform(30.0, 60.0)
    sleep(time)
