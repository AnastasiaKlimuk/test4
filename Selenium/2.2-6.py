from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id=\"input_value\"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//*[@id=\"answer\"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    checkbox = browser.find_element(By.XPATH, "//*[@id=\"robotCheckbox\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element(By.XPATH, "//*[@id=\"robotsRule\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()