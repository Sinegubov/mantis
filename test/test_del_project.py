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
    assert sorted(old_projects_list, key=ProjectForm.id_or_max) == \
           sorted(new_projects_list, key=ProjectForm.id_or_max)


# -*- coding: utf-8 -*-
from fixture.application import Application
from gen import  genereate
import pytest
import json
import jsonpickle
import os.path
import importlib







# Load test data from JSON file
def pytest_generate_tests(metafunc):
    # To load test data - form fixture, use parameters with prefix "data_", but remove the prefix (first 5 symbols)
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            genereate()
            testdata = load_from_json(fixture[10:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata


def load_from_json(file):
    file_target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{}.json".format(file))
    with open(file_target) as file_in_use:
        return jsonpickle.decode(file_in_use.read())

