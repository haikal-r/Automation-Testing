from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome()

driver.get("http://localhost/Penjual-Herbal/")
time.sleep(5)

tombol_login = driver.find_element(By.XPATH, "//a[@href='./login.php' and contains(@class, 'btn-outline-success')]")


# Lakukan tindakan pada elemen anchor, misalnya klik
tombol_login.click()
time.sleep(5)

username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

username = "pembeli2"
password = "pembeli2"

username_field.send_keys(username)
time.sleep(2)
password_field.send_keys(password)
time.sleep(2)
login_button.click()
time.sleep(5)



# Tutup browser
driver.quit()