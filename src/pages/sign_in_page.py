from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.CLASS_NAME, "orangehrm-login-button")
        self.page_load_element = self.user_name  # Element to check for page load

    def select_username(self, username):
        user_name_element = self.driver.find_element(*self.user_name)
        user_name_element = self.wait_for_element_to_be_visible(self.user_name)
        user_name_element.send_keys(username)

    def select_password(self, password):
        password_element = self.driver.find_element(*self.password)
        password_element = self.wait_for_element_to_be_visible(self.password)
        password_element.send_keys(password)

    def click_login(self):
        login_btn_element = self.driver.find_element(*self.login_btn)
        login_btn_element = self.wait_for_element_to_be_visible(self.login_btn)
        login_btn_element.click()

    def wait_for_page_load(self, timeout=10):
        """
        Waits for the SignInPage to fully load by checking the presence of a key element.

        :param timeout: Maximum time to wait for the element to be present
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.page_load_element)
            )
            print("SignInPage has loaded successfully.")
        except Exception as e:
            print(f"Error waiting for SignInPage to load: {e}")
            raise

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """
        Waits for an element to be visible on the page.

        :param locator: A tuple containing the locator strategy and value (e.g., (By.ID, "username"))
        :param timeout: Maximum time to wait for the element to be visible
        :return: The WebElement if it is visible
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            print(f"Element with locator {locator} is visible.")
            return element
        except Exception as e:
            print(
                f"Error: Element with locator {locator} not visible within {timeout} seconds. {e}"
            )
            raise
