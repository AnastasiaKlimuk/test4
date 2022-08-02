from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
    input3.send_keys("Smolensk")

    element = browser.find_element(By.XPATH, '//*[@id=\"file\"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()