from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input.send_keys(y)

    checkbox = browser.find_element(By.XPATH, "//*[@id=\"robotCheckbox\"]")
    checkbox.click()

    radio = browser.find_element(By.XPATH, "//*[@id=\"robotsRule\"]")
    radio.click()

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/div/button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()