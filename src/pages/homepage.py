from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module")
        self.user_name = (By.CSS_SELECTOR, ".username")
        self.page_load_element = self.user_name  # Element to check for page load

    def get_dashboard(self):
        user_name_element = self.driver.find_element(*self.dashboard)
        return user_name_element.text

    def wait_for_page_load(self, timeout=10):
        """
        Waits for the SignInPage to fully load by checking the presence of a key element.

        :param timeout: Maximum time to wait for the element to be present
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.page_load_element)
            )
            print("HomePage has loaded successfully.")
        except Exception as e:
            print(f"Error waiting for SignInPage to load: {e}")
            raise
