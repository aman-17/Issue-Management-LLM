# NLBSE’24 Dataset
In this package, we provide various tools to get started on NLBSE’24 inference.
The NLBSE'24 Tool Competition Dataset is a collection of 3,000 labeled issue reports 
extracted from five open-source projects. These issue reports were collected over a 
period of 21 months, from January 2022 to September 2023, ensuring a diverse range of 
issues and scenarios are covered. Each issue report in the dataset is labeled with one
of three categories: bug, feature, or question.
-'Dataset Information'
Size: 3,000 labeled issue reports.
Source Projects: The issue reports are extracted from five open-source projects.
Collection Period: January 2022 to September 2023 (21 months).

Run test and train files for the dataset. Click here to view the [issues-test](./datasets/nlbse24/issues_test.csv)
and [issues-train](./datasets/nlbse24/issues_train.csv)
# Issue Ticket Tagger Dataset
The Issue Ticket Tagger dataset comprises 30,000 labeled issues categorized into three distinct
groups based on their assigned labels. Approximately 10,000 issues are labeled as 'bug,' denoting 
code errors or malfunctions; another 10,000 are labeled as 'enhancement,' suggesting potential project
improvements and new feature additions; and the remaining 10,000 are labeled as 'question,' which
represents inquiries or uncertainties raised by users or developers.

For more information on how to use this dataset, please refer to the [file](./datasets/issue_ticket_tagger/issue_ticket_tagger.txt) in the sub-package.

# MulDIC dataset
The MulDIC dataset is a multimodal dataset comprising issues sourced from four popular projects: VS Code, Kubernetes, Flutter, and Roslyn. The dataset includes a total of 460,293 issue reports from these projects, with each issue categorized as either 'bug' or 'feature'.

# evaluation
Here is the evaluation of all the datasets:

#MulDIC
Run the following files to evaluate the MulDIC datasets
- `lvlm_gemini_pro.py`, This Python script appears to utilize the google.generativeai library, specifically the GenAI module, to interact with Google's Generative AI models, particularly the gemini-pro-vision model.
  
- `lvlm_gpt_vision.py`, This Python script utilizes the OpenAI API to generate responses to issue titles and code snippets extracted from a dataset.
For more information onthis dataset, please refer to the [here](https://github.com/chang26/MulDIC) in the sub-package.

#Issue Ticket Tagger:
run the following files to evaluate the Issue Ticket Tagger datasets
- `llm_gemini_pro.py`, This Python script appears to utilize the Gemini Pro model to generate labels for a list of issue texts extracted from a file. The generated labels are then saved for further analysis or use.
  
- `llm_gpt3.py`, This Python script utilizes the GPT-3.5 Turbo model from OpenAI to generate labels for a list of issue texts extracted from a file.
The output of this script is a series of generated responses printed to the console and saved in the ticket_tagger_gpt3.json file.

#nlbse:
run the following files to evaluate the nlbse datasets
- `issueclassificationgpt.ipynb`, This script uses Installation of Required Libraries along with that Importing Libraries and Loading Data.
  
- `nlbse_eval.py`, This code snippet performs several tasks related to data cleaning and interaction with the OpenAI GPT-3 API for generating responses.
The output of this script is a series of generated responses printed to the console and saved in the ticket_tagger_gpt3.json file.
- `requirements.txt`,  It provided lists specific versions of Python packages as dependencies. 
