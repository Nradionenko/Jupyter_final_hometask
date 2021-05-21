import time
from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from configloader import Config

cnf = Config()
nb_name = cnf.get_value("jupyter_nb", "nb")


class JupyterLocators:
    LOCATOR_NOTEBOOK = (By.XPATH, f"//span[@class='item_name' and text()='{nb_name}']")
    LOCATOR_CELLS_BUTTON = (By.XPATH, ".//*[@id='celllink']")
    LOCATOR_RUN_ALL = (By.XPATH, ".//*[@id='run_all_cells']")


class JupyterNB(BasePage):

    def open_notebook(self):
        nb = self.find_element(JupyterLocators.LOCATOR_NOTEBOOK, time=5)
        nb.click()

    def expand_cells_menue(self):  # expand Cell dropdown on top navigation menue bar
        cells = self.find_element(JupyterLocators.LOCATOR_CELLS_BUTTON, time=5)
        time.sleep(2)
        cells.click()

    def run_all_cells(self):
        run_all = self.find_element(JupyterLocators.LOCATOR_RUN_ALL, time=5)
        time.sleep(2)
        run_all.click()
        time.sleep(50)
        self.driver.quit()
