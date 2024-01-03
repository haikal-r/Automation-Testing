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


    username = "Risky"
    password = "Risky"

    # Input Data user
    username_field.send_keys(username)
    time.sleep(3)
    password_field.send_keys(password)
    time.sleep(3)
    login_button.click()
    time.sleep(3)


    # Click the user circle icon
    shop_link = driver.find_element(By.CLASS_NAME, 'fa-shop')
    shop_link.click()
    time.sleep(3)

    # Click Produk Button
    product_link = driver.find_element(By.XPATH, "//div[contains(text(), 'Produk')]/..")
    product_link.click()
    time.sleep(3)

    # Click edit button
    tombol_edit = driver.find_element(By.XPATH, "//a[text()='Edit']")
    tombol_edit.click()
    time.sleep(3)

    # Find Element
    input_nama_barang = driver.find_element(By.NAME, "nama")

    # Input data product
    input_nama_barang.clear()
    time.sleep(2)
    input_nama_barang.send_keys("Wyvern")
    time.sleep(3)

    # Submit Data Product
    tombol_submit =  driver.find_element(By.XPATH, "//button[text()='Update']")
    tombol_submit.click()
    time.sleep(5)

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
        file.write(f"Fitur Checkout - Diuji pada: {current_datetime} - Status: Error - Internal Server Error\n")
    else:
        file.write(f"Fitur Checkout - Diuji pada: {current_datetime} - Status: {status}\n")



# Tutup browser
driver.quit()