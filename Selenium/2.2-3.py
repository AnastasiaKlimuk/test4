from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id=\"num1\"]')
    y_element = browser.find_element(By.XPATH, '//*[@id=\"num2\"]')
    x = x_element.text
    y = y_element.text
    z = str(int(x)+int(y))

    browser.find_element(By.XPATH, '//*[@id=\"dropdown\"]').click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{z}']").click()

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()