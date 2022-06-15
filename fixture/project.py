from selenium.webdriver.common.by import By


class ProjectHelper:

    def __init__(self,app):
        self.app = app

    def open_add_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswitch("/manage_proj_create_page.php") and
                len(wd.find_elements(by=By.NAME, value="//input[@type='submit']")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="Manage Projects").click()

    def create_new_project(self):
        wd = self.app.wd
        self.open_add_project_page()
        # Press button to add project

