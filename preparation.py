import json
import os
from shared_funcs import delete_folder, create_folder, get_json_object
import csv

TEST_COUNT = 164


# Open HumanEval.jsonl file
def parse_human_eval_jsonl():
    with open('HumanEval.jsonl', 'r') as f:
        if os.path.exists('human-eval'):
            delete_folder('human-eval')

        create_folder('human-eval')
        for line in f:
            data = json.loads(line)

            # Create a json file with the name of data['task_id']
            with open(data['task_id'].split('/')[1] + '.json', 'w') as outfile:
                json.dump(data, outfile)
    os.chdir('..')


# Save the prompt to a python file for all json files
def save_prompt_for_generation():
    if os.path.exists('code_generation'):
        os.chdir('code_generation')
        files = os.listdir()
        for file in files:
            delete_folder(file)
        os.chdir('..')
        os.rmdir('code_generation')

    create_folder('code_generation')
    os.chdir('..')

    for i in range(TEST_COUNT):
        os.chdir('human-eval')
        json_obj = get_json_object(str(i))
        os.chdir('..')

        os.chdir('code_generation')
        create_folder(str(i))
        with open('prompt_' + str(i) + '.py', 'w', encoding='utf-8') as f:
            prompt_to_write = json_obj["prompt"]

            f.write(prompt_to_write)
            print("INIT Prompt file for " + str(i) + " created.")
        os.chdir('..')
        os.chdir('..')


def create_experiment_folders():
    if os.path.exists('experiment-code'):
        os.chdir('experiment-code')
        files = os.listdir()
        for file in files:
            delete_folder(file)
        os.chdir('..')
        os.rmdir('experiment-code')

    if os.path.exists('experiment-results'):
        os.chdir('experiment-results')
        files = os.listdir()
        for file in files:
            delete_folder(file)
        os.chdir('..')
        os.rmdir('experiment-results')

    create_folder('experiment-code')
    os.chdir('..')

    create_folder('experiment-results')
    os.chdir('..')

    for i in range(TEST_COUNT):
        os.chdir('human-eval')
        json_obj = get_json_object(str(i))
        os.chdir('..')

        os.chdir('experiment-code')
        create_folder(str(i))

        with open('test_' + str(i) + '.py', 'w') as f:
            f.write(json_obj['test'])
            print("Test file for " + str(i) + " created")

        os.chdir('..')
        os.chdir('..')
        os.chdir('code_generation')
        os.chdir(str(i))

        with open('canonical_solution_' + str(i) + '.py', 'w') as f:
            # Write the canonical solution to the file
            sltn = ""
            for j in json_obj['canonical_solution'].splitlines():
                # Remove 4 spaces in the beginning of the line
                sltn += j[4:] + '\n'
            f.write(sltn)
            print("Canonical solution file for " + str(i) + " created")

        os.chdir('..')
        os.chdir('..')

        os.chdir('experiment-results')
        create_folder(str(i))
        os.chdir('..')
        os.chdir('..')


# create csv file with columns for id, validity, Time Complexity Generated, Time Complexity Canonical, Space Complexity Generated, Space Complexity Canonical, security, maintainability, relability
def create_csv():
    if os.path.exists("results"):
        delete_folder("results")

    create_folder("results")
    with open("results.csv", "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        header = ["ID", "Correctness", "Validity", "Time Complexity Generated", "Time Complexity Canonical",
                "Space Complexity Generated", "Space Complexity Canonical", "Security", "Maintainability", "Reliability"]
        writer.writerow(header)

        for i in range(TEST_COUNT):
            init_data = [i, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
           # writer.writerow(str(i) + ", -1, -1, -1, -1, -1, -1, -1, -1, -1")
            writer.writerow(init_data)


'''
------------------ SCRIPT ------------------
'''
parse_human_eval_jsonl()
save_prompt_for_generation()
create_experiment_folders()
create_csv()
