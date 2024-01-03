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

    username_field.send_keys(username)
    time.sleep(3)
    password_field.send_keys(password)
    time.sleep(3)
    login_button.click()
    time.sleep(3)

    shop_icon = driver.find_element(By.CLASS_NAME, 'fa-shop')

    # Click the user circle icon
    shop_icon.click()
    time.sleep(3)

    product_link = driver.find_element(By.XPATH, "//div[contains(text(), 'Produk')]/..")
    product_link.click()
    time.sleep(3)

    add_product = driver.find_element(By.XPATH, '//button[@name="tambah"]')
    add_product.click()
    time.sleep(3)

    input_nama_barang = driver.find_element(By.NAME, "nama_barang")
    input_nama_barang.send_keys("Tropicana Slim Sweetener Stevia")
    time.sleep(3)

    input_harga = driver.find_element(By.NAME, "harga")
    input_harga.send_keys("40000")
    time.sleep(3)

    input_deskripsi = driver.find_element(By.NAME, "deskripsi")
    input_deskripsi.send_keys("Stevia adalah pemanis buatan yang berasal dari daun tanaman Stevia rebaudiana. Tanaman ini berasal dari Amerika Selatan dan telah digunakan untuk makanan dan pengobatan selama ratusan tahun. Produk ini cocok Untuk anda yang sedang berdiet atau seda")
    time.sleep(3)

    input_stok = driver.find_element(By.NAME, "stok")
    input_stok.send_keys("10")
    time.sleep(3)

    input_gambar = driver.find_element(By.XPATH, "//input[@type='file']")
    input_gambar.send_keys("C:/Users/Haikal/Downloads/steia.png")
    driver.implicitly_wait(10)
    time.sleep(3)

    tombol_submit =  driver.find_element(By.XPATH, '//input[@type="submit"]')
    tombol_submit.click()
    time.sleep(2)
    
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