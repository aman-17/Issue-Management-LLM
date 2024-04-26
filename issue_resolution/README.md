# Issue Resolution, Tagging and Prioritization


# SWE-bench Inference
In this package, we provide various tools to get started on SWE-bench inference.
In particular, we provide the following important scripts and sub-packages:

- `make_datasets`, this sub-package contains scripts to generate new datasets for SWE-bench inference with your own prompts and issues.
- `run_api.py`, this script is used to generate API model generations for a given dataset.


## `make_datasets`
For more information on how to use this sub-package, please refer to the [README](./make_datasets/README.md) in the sub-package.

## Run API inference on test datasets

This python script is designed to run inference on a dataset using either the OpenAI or Anthropic API, depending on the model specified. It sorts instances by length and continually writes the outputs to a specified file, so that the script can be stopped and restarted without losing progress.

For instance, to run this script on SWE-bench context and Anthropic's Claude 3 model, you can run the following command:
```bash
export ANTHROPIC_API_KEY=<your key>
python run_api.py --dataset_name_or_path princeton-nlp/SWE-bench_oracle --model_name_or_path claude-3 --output_dir ./outputs
```

## Run live inference on open GitHub issues

Follow instructions [here](https://github.com/castorini/pyserini/blob/master/docs/installation.md) to install [Pyserini](https://github.com/castorini/pyserini), to perform BM25 retrieval.

Then run `run_live.py` to try solving a new issue. For example, you can try solving [this issue](https://github.com/huggingface/transformers/issues/26706 ) by running the following command:

```bash
export OPENAI_API_KEY=<your key>
python run_live.py --model_name gpt-3.5-turbo-1106 \
    --issue_url https://github.com/huggingface/transformers/issues/26706 
```


# Issue Tagging and Prioritization
Here is the evaluation of all the datasets:

## MulDIC
Run the following files to evaluate the MulDIC datasets

- `lvlm_gemini_pro.py`, This Python script appears to utilize the google.generativeai library, specifically the GenAI module, to interact with Google's Generative AI models, particularly the gemini-pro-vision model.
  
- `lvlm_gpt_vision.py`, This Python script utilizes the OpenAI API to generate responses to issue titles and code snippets extracted from a dataset.

For more information ont his dataset, please refer to the [here](https://github.com/chang26/MulDIC) in the sub-package.

## Issue Ticket Tagger:
run the following files to evaluate the Issue Ticket Tagger datasets
- `llm_gemini_pro.py`, This Python script appears to utilize the Gemini Pro model to generate labels for a list of issue texts extracted from a file. The generated labels are then saved for further analysis or use.
  
- `llm_gpt3.py`, This Python script utilizes the GPT-3.5 Turbo model from OpenAI to generate labels for a list of issue texts extracted from a file.
The output of this script is a series of generated responses printed to the console and saved in the ticket_tagger_gpt3.json file.

## NLBSE'24:
run the following files to evaluate the nlbse datasets
- `issueclassificationgpt.ipynb`, This script uses Installation of Required Libraries along with that Importing Libraries and Loading Data.
  
- `nlbse_eval.py`, This code snippet performs several tasks related to data cleaning and interaction with the OpenAI GPT-3 API for generating responses.
The output of this script is a series of generated responses printed to the console and saved in the ticket_tagger_gpt3.json file.
- `requirements.txt`,  It provided lists specific versions of Python packages as dependencies. 
