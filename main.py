from configloader import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.Login import LoginHelper
from pages.RunJupyterNB import JupyterNB

cnf = Config()

# driver
opts = Options()
opts.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
driver = webdriver.Chrome(executable_path=cnf.get_value("driver", "driver_path"), options=opts)


def main():
    datalab_login = LoginHelper(driver)
    datalab_login.go_to_site()
    datalab_login.epam_sso()
    datalab_login.enter_login(cnf.get_value("credentials", "username"))
    datalab_login.enter_password(cnf.get_value("credentials", "password"))
    datalab_login.click_on_submit_button()
    datalab_nb = JupyterNB(driver)
    datalab_nb.open_notebook()
    datalab_nb.switch_to_new_tab()
    datalab_nb.expand_cells_menue()
    datalab_nb.run_all_cells()


if __name__ == "__main__":
    main()
