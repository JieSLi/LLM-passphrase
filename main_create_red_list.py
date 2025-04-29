import argparse
import os
import pickle

from transformers import AutoTokenizer


def create_red_list(tokenizer, tok_dir, model_name):
    """create red_list, green_list and end_token_list"""

    # list of unicodes to keep
    keep_list = [32, 39, 45] + list(range(65, 91)) + list(range(97, 123))

    # list of unicodes to keep but to be replaced by eos
    end_list = [10, 33, 46, 63]  # (10, newline), (33, !),  (46, .)  (63, ?)

    allowed_unic = keep_list + end_list

    green_list = {}
    end_token_list = {}
    red_list = {}

    with open(
        os.path.join(tok_dir, model_name + "_red_end_green_list.txt"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write("green\t\t\tend\t\t\tred\n")

        for token_id in range(tokenizer.vocab_size):
            token = tokenizer.convert_ids_to_tokens(token_id)

            if (
                "gemma-7b" in model_name
                or "Llama-2" in model_name
                or "Mistral" in model_name
                or "Mixtral" in model_name
            ):
                token = token.lstrip("▁")

            elif "Llama-3" in model_name:
                token = token.lstrip("Ġ")

            # alt_token, alternative decoding as sometimes decode() differs from
            # convert_ids_to_tokens
            alt_token = tokenizer.decode([token_id])

            if all(ord(char) in allowed_unic for char in token) or all(
                ord(char) in allowed_unic for char in alt_token
            ) or token_id == tokenizer.eos_token_id:

                if (any(ord(char) in end_list for char in token) or any(
                    ord(char) in end_list for char in alt_token
                )) and token_id != tokenizer.eos_token_id:
                    end_token_list[token_id] = token
                    f.write(f"\t\t\t{token_id} {token}\t\t\t\n")
                else:
                    green_list[token_id] = token
                    f.write(f"{token_id} {token}\t\t\t\t\t\t\n")
            else:
                red_list[token_id] = token
                f.write(f"\t\t\t\t\t\t{token_id} {token}\n")

    with open(os.path.join(tok_dir, model_name + "_end_token_list.pkl"), "wb") as f:
        pickle.dump(list(end_token_list.keys()), f)

    with open(os.path.join(tok_dir, model_name + "_green_list.pkl"), "wb") as f:
        pickle.dump(list(green_list.keys()), f)

    with open(os.path.join(tok_dir, model_name + "_red_list.pkl"), "wb") as f:
        pickle.dump(list(red_list.keys()), f)


def main():

    parser = argparse.ArgumentParser(description="create token lists")

    parser.add_argument(
        "--tok_dir",
        type=str,
        help="directory of red_lists and related. defaults to './red_lists/'",
    )
    parser.add_argument(
        "--model",
        type=str,
        choices=[
            "Llama-2-7b",
            "Llama-2-13b",
            "Llama-2-70b",
            "Llama-3-8B",
            "Llama-3-70B",
            "gemma-7b",
            "Mistral-7B",
            "Mixtral-8x7B",
        ],
        default="Llama-2-7b",
        help="Choose a model (Llama-2-7b, Llama-2-13b, Llama-2-70b, ..., ) for tokenizer. Default is 'Llama-2-7b' when no arg is provided.",
    )

    parser.add_argument(
        "--function",
        default="create_red_list",
        choices=["create_red_list"],
        help="The function to run",
    )

    args = parser.parse_args()

    if args.tok_dir is None:
        tok_dir = "./red_lists/"

    if args.model == "Llama-2-7b":
        model_path = "meta-llama/Llama-2-7b-chat-hf"
    elif args.model == "Llama-2-13b":
        model_path = "meta-llama/Llama-2-13b-chat-hf"
    elif args.model == "Llama-2-70b":
        model_path = "meta-llama/Llama-2-70b-chat-hf"
    elif args.model == "Llama-3-8B":
        model_path = "meta-llama/Meta-Llama-3-8B-Instruct"
    elif args.model == "Llama-3-70B":
        model_path = "meta-llama/Meta-Llama-3-70B-Instruct"
    elif args.model == "gemma-7b":
        model_path = "google/gemma-7b-it"
    elif args.model == "Mistral-7B":
        model_path = "mistralai/Mistral-7B-Instruct-v0.2"
    elif args.model == "Mixtral-8x7B":
        model_path = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model_name = os.path.basename(model_path.rstrip("/"))
    print("---- using model", model_name)

    if args.function == "create_red_list":
        create_red_list(tokenizer, tok_dir, model_name)


if __name__ == "__main__":
    main()

# python main_create_red_list.py --model gemma-7b --function create_red_list
# one A4000 is enough for all tokenizers
