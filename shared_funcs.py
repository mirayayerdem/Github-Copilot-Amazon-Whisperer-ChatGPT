import os
import json


# Delete all the folders with name of the folder
def delete_folder(folder_name):
    if(os.path.exists(folder_name)):
        # Delete the contents of the folder
        os.chdir(folder_name)
        files = os.listdir()
        for file in files:
            if file == "__pycache__":
                delete_folder(file)
            else:
                os.remove(file)

        os.chdir('..')
        os.rmdir(folder_name)


# Define a function creates a folder with id as the name of the folder
def create_folder(folder_name):
    # Create a folder with the name of id
    os.mkdir(folder_name)
    # Change the current directory to the folder
    os.chdir(folder_name)


# Define a function given a json file index open the json file and return the json object
def get_json_object(index):
    # Open the json file
    with open(index + '.json', 'r') as f:
        data = json.load(f)
        
        return data
