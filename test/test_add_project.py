

def test_add_project(app, json_projects):
    old_projects_list = app.soap.get_projects_list()
    project = json_projects
    app.project.add_new_project(project)
    new_projects_list = app.soap.get_projects_list()
    assert len(old_projects_list) + 1 == len(new_projects_list)
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=(lambda x: x.project_name)) == \
           sorted(new_projects_list, key=(lambda x: x.project_name))
