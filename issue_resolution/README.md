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
