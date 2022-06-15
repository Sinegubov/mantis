from sys import maxsize


class ProjectForm:

    def __init__(self, project_name=None, project_description=None):
        self.project_name = project_name
        self.project_description = project_description

    def __repr__(self):
        return "%s ; %s" % (self.project_name, self.project_description)

    def __eq__(self, other):
        return self.project_name == other.project_name

    def id_or_max(self):
        if self.project_name:
            return int(self.project_name)
        else:
            return maxsize