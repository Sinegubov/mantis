import time
from model.project_form import ProjectForm


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.open_projects_page()
            self.project_cache = []
            # Find rows in table
            table_rows = wd.find_elements_by_xpath("//table[3]/tbody/tr[contains(@class,'row')]")
            for row in table_rows[1:]:
                cells = row.find_elements_by_tag_name("td")
                id = int(row.find_element_by_xpath("./td[1]/a").get_attribute('href').split("=")[1])
                project_name = cells[0].text
                project_description = cells[4].text
                self.project_cache.append(ProjectForm(
                    id=id,
                    project_name=project_name,
                    project_description=project_description))
        projects_list = list(self.project_cache)
        return projects_list

    def add_new_project(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_in_project_info(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        time.sleep(3)
        self.project_cache = None

    def fill_in_project_info(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.project_name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.project_description)

    def del_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text("%s" % project.project_name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # Accept alert
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None
