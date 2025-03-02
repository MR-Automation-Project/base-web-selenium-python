"""
    basemethod.py : action method yang bisa dilakukan pada halaman(page object)
                        digunakan pada layer pages
"""
import logging
import os
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils import *
from selenium.webdriver.common.by import By

class Basemethod:

    def __init__(self, driver):
        self.driver = driver

    def _click_on(self, locator):
        try:
            if isinstance(locator, tuple):
                wait_for_element_to_be_visible(self.driver, locator).click()
            elif isinstance(locator, WebElement):
                locator.click()
            else:
                raise ValueError("Invalid input locator. please give tuple format or WebElement instance")
                # Handling Tuple --> (By.Xpath, '//div[@class="user"]'
                # Handling WebElement  --> driver.find_element(By.ID, 'login-button')
        except(TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error while clicking element: {e}")
        except Exception as e:
            logging.error(f"Error saat mengklik elemen: {e}")

    def _input(self, locator, input_text):
        element = wait_for_element_to_be_visible(self.driver, locator)
        element.clear()
        element.send_keys(input_text)

    def _clear_on_textbox(self, locator):
        wait_for_element_to_be_visible(self.driver, locator).clear()

    def _is_element_visible(self, locator):
        return bool(wait_for_element_to_be_visible(self.driver, locator))

    def _get_text_element(self, locator):
        return wait_for_element_to_be_visible(self.driver, locator).text

    def _get_attribute_element(self, locator, attribute):
        return wait_for_element_to_be_visible(self.driver, locator).get_attribute(attribute)

    def _drag_and_drop(self, source_locator, target_locator):
        source = wait_for_element_to_be_visible(self.driver, source_locator)
        target = wait_for_element_to_be_visible(self.driver, target_locator)
        action = ActionChains(self.driver).drag_and_drop(source, target)
        action.perform()

    def _switch_to_frame(self, locator):
        wait_for_frame_to_be_avail_and_switch_to_it(self.driver, locator)

    def _switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    def _get_length_all_elements(self, locator):
        return len(wait_for_element_to_be_visible(self.driver, locator))

    def _hover_over_element(self, locator):
        target_element = wait_for_element_to_be_visible(self.driver, locator)
        actions = ActionChains(self.driver).move_to_element(target_element)
        actions.perform()

    def _capture_evidence(self, name):
        # Make sure the folder exists in the root of project directory,
        # jika tidak maka buat folder "screenshots"
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        #Tentukan path dan nama file+formatnya utk wadah screenshot
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)

    """-----------------------Handling DROPDOWN AREA - Select and non-select---------------------------"""

    def _select_dropdown_by_index(self, locator, index, timeout=10):
        """Memilih option list dalam dropdown berdasarkan index."""
        element = wait_for_element_to_be_presence(self.driver, locator)
        select = Select(element) #Buat object select
        text_of_index = select.options[index].text
        select.select_by_index(index)
        selected_option_text = select.first_selected_option.text
        assert selected_option_text == text_of_index, f"Opsi yang dipilih seharusnya {text_of_index}, tetapi yang terpilih adalah {selected_option_text}"

    def _select_dropdown_by_value(self, locator, value, timeout=10):
        """Memilih option list dalam dropdown berdasarkan value."""
        element = wait_for_element_to_be_visible(self.driver, locator)
        select = Select(element)  # Buat objek Select
        select.select_by_value(value)
        selected_option_text = select.first_selected_option.text
        assert selected_option_text == value, f"Opsi yang dipilih seharusnya {value}, tetapi yang terpilih adalah {selected_option_text}"

    def _select_dropdown_by_visible_text(self, locator, option_text, timeout=10):
        """Memilih option list dalam dropdown berdasarkan visible option text."""
        element = wait_for_element_to_be_presence(self.driver, locator)
        select = Select(element)
        select.select_by_visible_text(option_text)
        selected_option_text = select.first_selected_option.text
        assert selected_option_text == option_text, f"Opsi yang dipilih seharusnya {option_text}, tetapi yang terpilih adalah {selected_option_text}"

    def _select_dropdown_by_text_partial(self, locator, partial_text, timeout=10):
        """Memilih opsi dropdown berdasarkan sebagian teks yang terlihat."""
        element = wait_for_element_to_be_presence(self.driver, locator)
        options = element.find_elements(By.TAG_NAME, "option")  # ambil semua option yang menggunakan tag "option"
        for option in options:
            if partial_text in option.text:
                option.click()
                break
        select = Select(element)
        selected_option_text = select.first_selected_option.text
        assert partial_text in selected_option_text, f"Opsi yang dipilih tidak mengandung partial text: {partial_text}, tetapi yang terpilih adalah {selected_option_text}"