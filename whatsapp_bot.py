from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def create_whatsapp_group(group_name, contacts):
    # set path ke chromedriver
    service = Service(r'path/to/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    # bukakan WhatsApp
    driver.get('https://web.whatsapp.com')
    
    # tunggu sampai tombol 'Scan QR code' ditemukan
    print("Scan the QR code and press Enter")
    
    try:
        # tungu sampai tombol 'Menu' ditemukan
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@title="Menu"]'))
        )

        # klik tombol 'Menu' 
        menu_button = driver.find_element(By.XPATH, '//*[@title="Menu"]')
        menu_button.click()

        # tunggu sampai tombol 'New group' ditemukan dan diklik
        new_group = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="New group"]'))
        )
        new_group.click()

        # Add contacts to the group
        for contact in contacts:
            # tunggu sampai tombol 'Search' ditemukan dan diklik
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
            )
            search_box.send_keys(contact)

            # tunggu sampai kontak ditemukan
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact}"]'))
            ).click()

            # hapus inputan
            search_box.clear()

        # klik tombol 'Next'
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-icon="arrow-forward"]'))
        )
        next_button.click()

        # masukkan nama grup
        group_name_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
        group_name_box.send_keys(group_name)

        # klik tombol 'Finalize'
        finalize_button = driver.find_element(By.XPATH, '//span[@data-icon="checkmark-medium"]')
        finalize_button.click()

        print(f'Grub "{group_name}" berhasil dibuat dengan {len(contacts)} members.')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # keluar dari browser
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    # Konfigurasi
    group_name = "Grup Belajar Python BOT"
    contacts = [
        "contact 1",
        "contact 2",
    ]  # taruh nama kontak atau nomor yang benar

    # buat grub whatsapp sesuai dengan konfigurasi
    create_whatsapp_group(group_name, contacts)
