from model.project_form import ProjectForm
import random


def test_del_project(app):
    old_projects_list = app.project.get_projects_list()
    if not old_projects_list:
        app.project.add_new_project(ProjectForm(project_name="New Project",
                                                project_description="New Project Description"))
        old_projects_list = app.project.get_projects_list()
    project = random.choice(old_projects_list)
    app.project.del_project(project)
    new_projects_list = app.project.get_projects_list()
    assert len(old_projects_list) - 1 == len(new_projects_list)
    old_projects_list.remove(project)
    assert sorted(old_projects_list, key=(lambda x: x.project_name)) == \
           sorted(new_projects_list, key=(lambda x: x.project_name))

    def logout(self):
        wd = self.app.wd
        # Just logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("username")

    # Checks
    def ensure_login(self, username, password):
        wd = self.app.wd
        # Check if logged in
        if self.is_logged_in():
            # Check if logged in with correct username, if not - logout.
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        # Check which credentials are used for login
        return self.get_logged_username() == username

    def get_logged_username(self):
        wd = self.app.wd
        # Get username from inside the brackets, like (admin)
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def is_logged_in(self):
        wd = self.app.wd
        # Check if logged in - if there are elements with text Logout on the current page
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_logout(self):
        wd = self.app.wd
        # If logged in, do logout
        if self.is_logged_in():
            self.logout()

© 2022
GitHub, Inc.
Terms
Privacy
Security
Statu