from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение</div> вернёт строку: "У вас новое сообщение"
    x_element = browser.find_element(By.CSS_SELECTOR, "div [id='input_value']")
    x = x_element.text
    y = calc(x)

    #Проскроллить страницу вниз
    text = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text)

    #Ввести ответ в текстовое поле
    text.send_keys(y)

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