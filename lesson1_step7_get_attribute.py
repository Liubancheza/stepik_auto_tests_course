from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

#функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    x_element = browser.find_element(By.ID, "treasure")
    #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x =  x_element.get_attribute("valuex")
    #Посчитать математическую функцию от x
    y = calc(x)

    #Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)

    #Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    #Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "[id = 'robotsRule']")
    option2.click()

    #Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()