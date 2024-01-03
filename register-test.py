from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from datetime import datetime

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/Penjual-Herbal/")
    time.sleep(5)

    tombol_register = driver.find_element(By.XPATH, "//a[@href='./register.php' and contains(@class, 'btn btn-light')]")

    # Lakukan tindakan pada elemen anchor, misalnya klik
    tombol_register.click()
    time.sleep(5)

    email_field = driver.find_element(By.XPATH, '//input[@name="email"]')
    alamat_field = driver.find_element(By.XPATH, '//input[@name="alamat"]')
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    select_element = driver.find_element(By.XPATH, "//select[@name='role']")

    # Klik elemen <select> untuk membuka dropdown
    select_element.click()

    # Temukan dan klik opsi yang diinginkan berdasarkan XPath

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    email = "Haikalramadhan88@gmail.com"
    alamat = "Perumahan Villa Hanglekir"
    username = "Haikal Ramadhan"
    password = "Haikal"

    email_field.send_keys(email)
    time.sleep(2)
    alamat_field.send_keys(alamat)
    time.sleep(2)
    username_field.send_keys(username)
    time.sleep(2)
    password_field.send_keys(password)
    time.sleep(2)

    # Memilih role
    option_xpath = "//select[@name='role']/option[@value='pembeli']"
    pembeli_option = driver.find_element(By.XPATH, option_xpath)
    pembeli_option.click()

    # Submit
    login_button.click()
    time.sleep(5)
    alert = Alert(driver)
    alert.accept()
    time.sleep(3)

    current_url = driver.current_url

    if '/login' in current_url:
        status = "succesful"
    elif '/register' in current_url:
        status = "login gagal"
    else:
        status = "Failed (Unknown error)"

except Exception as e:
    status = "Gagal"
    print(f"Terjadi kesalahan: {e}")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('uji-fungsionalitas.txt', 'a') as file:
    if "<h1>Internal Server Error</h1>" in driver.page_source:
        file.write(f"Fitur register - Diuji pada: {current_datetime} - Status: Error - Internal Server Error\n")
    else:
        file.write(f"Fitur register - Diuji pada: {current_datetime} - Status: {status}\n")

# Tutup browser
driver.quit()