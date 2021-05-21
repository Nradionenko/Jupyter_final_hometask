import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configloader import Config


cnf = Config()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = cnf.get_value("env", "env_link")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

    def go_to_site(self):
        return self.driver.get(self.base_url)
