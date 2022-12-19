#response = requests.get('https://sonarqube.com/api/user_tokens/search', auth=('52af95004cfcb0faaa3adc42f8648f7606d94d2a', ''))

import json , requests, pprint
import os
from requests.sessions import session
import subprocess, sys
from decouple import config


url = 'http://localhost:9000/'
TEST_COUNT = 164


# Authenticate
def authenticate(url):
    session = requests.Session()
    #authenticate session with token
    session.auth = (config("SONAR_TOKEN"), '')

    auth = session.post(url + 'api/user_tokens/search')
    response = session.get(url + 'api')

    return session


# Create a sonarqube project
def create_project(session, project_name, project_key):
    obj = {'name': project_name, 'project': project_key}
    response = session.post(url + 'api/projects/create', data = obj)

    return response


# create projects
def create_projects(session):
    for i in range(TEST_COUNT):
        project_name = "humaneval_" + str(i)
        project_key = "humaneval_" + str(i)
        print('SONARQUBE Creating project: ' + project_name)
        create_project(session, project_name, project_key)


def run_sonarqube():
    for i in range(TEST_COUNT):
        project_key = "humaneval_" + str(i)
        py_file_name = "/prompt_" + str(i) + ".py"
        cmd = "sonar-scanner.bat -D'sonar.projectKey=" + project_key + "' -D'sonar.sources=code_generation/" + str(i) + py_file_name + "'"
        cmd += " -D'sonar.host.url=http://localhost:9000' -D'sonar.login=" + config("SONAR_TOKEN") + "'"
        p = subprocess.Popen(["powershell.exe", cmd], stdout=sys.stdout)
        p.communicate()


# Delete a sonarqube project
def delete_projects(session):
    projects = ""
    for i in range(TEST_COUNT):
        projects += "humaneval_" + str(i) + ","
        
    obj = {'projects': projects}
    print('SONARQUBE Deleting projects...')
    response = session.post(url + 'api/projects/bulk_delete', data = obj)
    return response


# get measures
def get_measures(session, project_key):
    obj = {'component': project_key, 'metricKeys': 'code_smells,bugs,security_rating'}
    measures_response = session.get(url + 'api/measures/component', params=obj)

    return measures_response


# save all measures
def save_measures_to_json(session):
    os.chdir('experiment-results')

    for i in range(TEST_COUNT):
        os.chdir(str(i))
        project_key = "humaneval_" + str(i)
        measures_response = get_measures(session, project_key)
        measures = json.loads(measures_response.text)
        with open('sonar_' + str(i) + '.json', 'w') as outfile:
            json.dump(measures, outfile)
        os.chdir('..')
    os.chdir('..')


# Extract metrics for one problem
def extract_metrics(idx):
    metrics = []
    with open('sonar_' + str(idx) + '.json') as json_file:
        data = json.load(json_file)
        metric = []
        print(data)
        for p in data['component']['measures']:
            metric.append(p['metric'])
            metric.append(p['value'])
            metric_key_value = {}
            metric_key_value[p['metric']] = p['value']
            metrics.append(metric_key_value)
            metric = []
    return metrics


# Save all metrics
def extract_all_metrics_to_csv():
    from csv import reader, writer

    allMetrics = []
    os.chdir('experiment-results')
    for i in range(TEST_COUNT):
        os.chdir(str(i))
        allMetrics.append(extract_metrics(i))
        os.chdir('..')
    os.chdir('..')

    matrix = []
    with open("results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            if row != []:
                matrix.append(row)

    for i in range(TEST_COUNT):
        for j in range(3):
            if allMetrics[i] == []:
                break
            if 'security_rating' in allMetrics[i][j]:
                matrix[i+1][7] = allMetrics[i][j]['security_rating']
            if 'bugs' in allMetrics[i][j]:
                matrix[i+1][8] = allMetrics[i][j]['bugs']
            if 'code_smells' in allMetrics[i][j]:
                matrix[i+1][9] = allMetrics[i][j]['code_smells']

    with open("results/results.csv", "w", newline='') as f:
        writer = writer(f)
        writer.writerows(matrix)


def run_sonarqube_eval():
    session = authenticate(url)
    delete_projects(session)
    create_projects(session)
    run_sonarqube()
    save_measures_to_json(session)
    extract_all_metrics_to_csv()
