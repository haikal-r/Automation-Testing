from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/Penjual-Herbal/")
    time.sleep(3)

    tombol_login = driver.find_element(By.XPATH, "//a[@href='./login.php' and contains(@class, 'btn-outline-success')]")


    # Lakukan tindakan pada elemen anchor, misalnya klik
    tombol_login.click()
    time.sleep(3)

    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    username = "pembeli2"
    password = "pembeli2"

    username_field.send_keys(username)
    time.sleep(1)
    password_field.send_keys(password)
    time.sleep(1)
    login_button.click()
    time.sleep(1)

    cart_link = driver.find_element(By.XPATH, "//a[@href='../user/keranjang.php']")

    # Click on the cart link
    cart_link.click()
    time.sleep(3)

    checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")

    # Click on the Checkout button
    checkout_button.click()

    pesanan_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    pesanan_button.click()
    time.sleep(3)

    alert = Alert(driver)
    alert.accept()
    time.sleep(3)
    
    current_url = driver.current_url

    if '/user/' in current_url:
        status = "succesful"
    elif '/' in current_url:
        status = "login gagal"
    else:
        status = "Failed (Unknown error)"

except Exception as e:
    status = "Gagal"
    print(f"Terjadi kesalahan: {e}")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('uji-fungsionalitas.txt', 'a') as file:
    if "<h1>Internal Server Error</h1>" in driver.page_source:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: Error - Internal Server Error\n")
    else:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: {status}\n")



# Tutup browser
driver.quit()