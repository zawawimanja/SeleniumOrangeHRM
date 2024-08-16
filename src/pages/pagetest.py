from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver


class ExamplePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "sign_in_button": ("ID", "signin"),
        }

    def click_sign_in(self):
        self.sign_in_button.click()


# Setup WebDriver (Assuming you're using ChromeDriver)
driver = webdriver.Chrome(executable_path="path_to_chromedriver")
driver.get("https://example.com")

page = ExamplePage(driver)
page.click_sign_in()
