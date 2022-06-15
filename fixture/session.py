from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # Open URL, insert credentials and submit login
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.capabilities['nativeEvents'] = False
        wd.find_element_by_xpath("//input[@value='Login']").send_keys(Keys.ENTER)

    def logout(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()
        wd.find_element(by=By.NAME, value="username")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(by=By.LINK_TEXT, value="Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_username() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(by=By.CSS_SELECTOR, value="td.login-info-left span").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
