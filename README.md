# LLM-passphrase

This repository provides code for generating passphrases and examples using large language models (LLMs). 

## Setup

1. **Download Hugging Face Models**

   You will need to download the appropriate Hugging Face models before running the code. Please follow the model provider’s instructions for downloading and saving the models locally.

2. **Set the `HF_HOME` Environment Variable**

   After downloading, set the `HF_HOME` environment variable to the directory where your Hugging Face models are stored. For example:

   ```bash
   export HF_HOME=/path/to/your/huggingface/models
   ```

   You may want to add this line to your `.bashrc` or `.zshrc` to set it automatically in future sessions.

## Running the Examples

To run the econ examples using the Gemma-7B model, use the following command:

```bash
python main_sample.py --model "gemma-7b" --out_subdir "econ_exs" --bsz 4 --N 32 --in_prompt 806 
```

Here:

- `--model` specifies the model to use.
- `--out_subdir` sets the output directory for generated examples.
- `--bsz` defines the batch size.
- `--N` sets the number of generations.
- `--in_prompt` provides the prompt ID. 

## Folder Structure

- `pp/` — Source code for passphrase generation.
- `main_sample.py` — Main script to run sample generations.

## License

This project is open-source under the MIT License.
