## ChatGPT vs. GitHub Copilot vs. Amazon CodeWhisperer: A Comparison of the Code Quality of State-of-the-Art Code Generators
*Requirements:*
- [python-decouple package](https://pypi.org/project/python-decouple/) (Can be installed with Pyhton Package Installer, pip using command: *pip install python-decouple*)
- [Sonarqube API](https://docs.sonarqube.org/latest/extend/web-api/) and [OpenAI API](https://openai.com/api/) keys

*Experiment Steps:*
- Create an .env file using .env.example file for Sonarqube API key
- Run [preparation.py](https://github.com/mirayayerdem/Github-Copilot-Amazon-Whisperer/blob/main/preparation.py)
  --> *python preparation.py*
- Generate code manually using the prompt_i.py files under the code-generation folder
- Run [experiment.py](https://github.com/mirayayerdem/Github-Copilot-Amazon-Whisperer/blob/main/experiment.py)
 --> *python experiment.py*
##
The results for all of our experiments can be viewed [here](https://github.com/mirayayerdem/Github-Copilot-Amazon-Whisperer-ChatGPT/blob/main/misc/All_Experiment_Results.xlsx).

##
The generated code for each of our experiments can be found [here](https://github.com/mirayayerdem/Github-Copilot-Amazon-Whisperer/tree/main/misc/Experiment%20results)

##
For the comparison results of code correctness and code validity metrics:
- Record the code correctness and code validity scores for the experiments to be compared in a file called 'comparison_data.csv'.
- Run [compare_results.py](https://github.com/mirayayerdem/Github-Copilot-Amazon-Whisperer/blob/main/compare_results.py)
--> *python compare_results.py*
