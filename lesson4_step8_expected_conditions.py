from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

# ввести значение
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

# нажать submit
button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)

browser.quit()



