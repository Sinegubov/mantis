from sys import maxsize


class ProjectForm:

    def __init__(self, id=None, project_name=None, project_description=None):
        self.id = id
        self.project_name = project_name
        self.project_description = project_description

    def __repr__(self):
        return "%s ; %s; %s" % (self.id, self.project_name, self.project_description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.project_name is None or other.project_name is None or self.project_name == other.project_name

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize
