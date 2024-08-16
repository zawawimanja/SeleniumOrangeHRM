from selenium import webdriver
from src.pages.homepage import HomePage
from src.pages.sign_in_page import SignInPage


def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    home_page = HomePage(driver)
    sign_in_page = SignInPage(driver)

    # homepage.click_sign_in()
    sign_in_page.wait_for_page_load()
    # if sign_in_page.wait_for_page_load():
    #     print("Username field exists")
    # else:
    #     print("Username field does not exist")
    # Pass the username and password as arguments
    sign_in_page.select_username("Admin")
    sign_in_page.select_password("admin123")
    sign_in_page.click_login()

    # # Get the username from the homepage and validate it
    # retrieved_username = homepage.get_username()
    # assert (
    #     retrieved_username == "demouser"
    # ), f"Expected 'demouser' but got '{retrieved_username}'"

    home_page.wait_for_page_load()

    driver.quit()


# Example usage
if __name__ == "__main__":
    test_browserstack()
