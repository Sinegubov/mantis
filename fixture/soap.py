from zeep import Client
from suds import WebFault
from model.project_form import ProjectForm


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_client(self):
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url + "/api/soap/mantisconnect.php?wsdl")
        return client

    def can_login(self, username, password):
        client = self.get_client()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        client = self.get_client()
        projects_list = []
        config = self.app.config['webadmin']
        projects_list_from_soap = client.service.mc_projects_get_user_accessible(
            username=config["username"], password=config["password"])
        for project in projects_list_from_soap:
            projects_list.append(ProjectForm(
                id=project.id,
                project_name=project.name,
                project_description=project.descriprion))
        return projects_list
