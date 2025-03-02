"""
    utils.py : action helper umum yang bisa digunakan lebih luas.
                bisa digunakan pada layer : test class, pages, dan basemethod
"""
from datetime import datetime, timedelta
import random
import logging
import os
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import csv


def wait_for_element_to_be_visible(driver, locator, waitTime=10):
    """Menunggu hingga elemen terlihat."""
    try:
        element = WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located(locator))
        return element
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"Element belum terlihat: {e}")
        return None  # Mengembalikan None jika elemen tidak terlihat

def wait_for_element_to_be_presence(driver, locator, waitTime=10):
    """Menunggu hingga elemen sudah tersedia di dalam DOM"""
    try:
        element = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located(locator))
        return element
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"Element belum tersedia di DOM: {e}")
        return None  # Mengembalikan None jika elemen tidak ditemukan di DOM

def wait_for_element_to_be_clickable(driver, locator, waitTime=10):
    """Menunggu hingga elemen sudah bisa diclicked"""
    try:
        element = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable(locator))
        return element
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"Element belum dapat diclick: {e}")
        return None

def wait_for_frame_to_be_avail_and_switch_to_it(driver, locator, waitTime=10):
    try:
        element = WebDriverWait(driver, waitTime).until(EC.frame_to_be_available_and_switch_to_it(locator))
        return element
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"Element not visible: {e}")
        return None  # Mengembalikan None jika elemen tidak ditemukan

def take_screenshot(driver, name):
    """Mengambil screenshot dan menyimpannya dalam folder 'screenshots' """
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Tambahkan timestamp
    screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path  # Kembalikan path screenshot

def refresh_browser(driver):
    """Me-refresh halaman browser."""
    driver.refresh()

def click_back_browser(driver):
    driver.back()

def click_forward_browser(driver):
    driver.forward()

def accept_alert_prompt_browser(driver):
    alert_msg = driver.switch_to.alert
    alert_msg.accept()

def dismiss_alert_prompt_browser(driver):
    alert_msg = driver.switch_to.alert
    alert_msg.dismiss()

def press_enter_on_keyboard(driver):
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

def press_page_down_on_keyboard(driver):
    actions = ActionChains(driver).send_keys(Keys.PAGE_DOWN)
    actions.perform()

def press_page_up_on_keyboard(driver):
    actions = ActionChains(driver).send_keys(Keys.PAGE_UP)
    actions.perform()

def get_current_url(driver, url_contains_partial_text="", timeout=10):
    """
    Args:
        url_contains_partial_text: Bagian teks yang diharapkan ada dalam URL.
                                    Jika string kosong, maka hanya akan dicek apakah URL sudah ada
                                    (random text url apapun).
    """
    try:
        if url_contains_partial_text: # Periksa apakah string tidak kosong
            WebDriverWait(driver, timeout).until(
                EC.url_contains(url_contains_partial_text)
            )
        else: # Jika string kosong/tdk diinput argumentnya, tunggu sampai URL ada textnya apapun itu
             WebDriverWait(driver, timeout).until(EC.url_contains(""))

        actual_url = driver.current_url
        return actual_url

    except TimeoutException:
        logging.error(f"Timeout saat menunggu URL yang mengandung '{url_contains_partial_text}' setelah {timeout} detik")
        return None

"""--------------------Generate data random suc as email, name, phone number, etc---------------------------------"""

def generate_random_phone_number_plus62():
    return f"+62{random.randint(1000000000, 9999999999)}"

def generate_random_phone_number_62():
    return f"+62{random.randint(1000000000, 9999999999)}"

def generate_random_phone_number_0():
    return f"081{random.randint(1000000000, 9999999999)}"

def generate_new_email_visiprimaqa():
    # Path to the counter file
    counter_file = 'email_counter.txt'

    # Check if the file exists and is not empty
    if os.path.exists(counter_file) and os.path.getsize(counter_file) > 0:
        with open(counter_file, 'r') as file:
            try:
                counter = int(file.read().strip())  # Try reading the existing counter value
            except ValueError:
                counter = 1  # Default to 1 if the file is corrupted or empty
    else:
        counter = 1  # Start at 1 if file does not exist or is empty

    email_prefix = "visiprimaqa+"
    domain = "@gmail.com"

    # Generate the next email
    next_email = f"{email_prefix}{counter}{domain}"

    # Increment the counter and save it back to the file
    with open(counter_file, 'w') as file:
        file.write(str(counter + 1))

    return next_email

def generate_random_number():
    counter_file = "name_counter.txt"

    if not os.path.exists(counter_file):
        with open(counter_file, "w") as file:
            file.write("1")

    # Baca counter saat ini dari file
    with open(counter_file, "r") as file:
        counter = int(file.read().strip())

    # Generate name
    number = f"{counter}"

    # Increment counter
    with open(counter_file, "w") as file:
        file.write(str(counter + 1))

    return number

"""------------------------------------ DATE HANDLING -------------------------------------------------"""
class DateHandling:
    def get_current_date(self, format="%Y-%m-%d"):
        return datetime.now().strftime(format)

    def adding_current_date(self, days, format="%d-%m-%Y"):
        """days = jumlah hari yang ingin ditambah, misal 5 --> maka akan tambah 5 hari kedepan dari hari ini"""
        return (datetime.now() + timedelta(days=days)).strftime(format)

    def minus_current_date(self, days, format="%d-%m-%Y"):
        """days = jumlah hari yang ingin dikurangi, misal 5 --> maka akan mundur 5 hari kebelakang dari hari ini"""
        return (datetime.now() - timedelta(days=days)).strftime(format)


"""----------------------------------- FILE HANDLING ---------------------------------------------------"""
class FileHandling:
    """
    Note :
        - Beberapa fungsi file handling dibawah ini masih dalam tahap research dan pengujian, belum fully works sepenuhnya.
    """

    # 1. Function to read a text file and return its content
    def read_text_file(self, file_path):
        """Reads and returns content of a text file."""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist")

    # 2. Function to write content to a text file
    def write_text_file(self, file_path, content):
        """Writes content to a text file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    # 3. Function to read a JSON file
    def read_json_file(self, file_path):
        """Reads and returns the content of a JSON file."""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist")

    # 4. Function to write data to a JSON file
    def write_json_file(self, file_path, data):
        """Writes data to a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    # 5. Function to read CSV file and return it as a list of dictionaries
    def read_csv_file(self, file_path):
        """Reads a CSV file and returns a list of dictionaries."""
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist")

    # 6. Function to write data to CSV file (list of dictionaries)
    def write_csv_file(self, file_path, data, fieldnames):
        """Writes data (list of dictionaries) to a CSV file."""
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    # 7. Function to check if a file exists
    def check_file_exists(self, file_path):
        """Checks if a file exists and returns True or False."""
        return os.path.exists(file_path)

    # 8. Function to delete a file
    def delete_file(self, file_path):
        """Deletes a file."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist")