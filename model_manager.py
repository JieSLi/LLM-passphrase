from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig)
import os
import torch


def load_model_and_tokenizer(args_model):

    if args_model == "Llama-2-7b":
        model_path = "meta-llama/Llama-2-7b-chat-hf"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.float16
        )
    elif args_model == "Llama-2-13b":
        model_path = "meta-llama/Llama-2-13b-chat-hf"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.float16
        )
    elif args_model == "Llama-2-70b":
        model_path = "meta-llama/Llama-2-70b-chat-hf"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        quantization_config = BitsAndBytesConfig(
            llm_int4_threshold=200.0,
            bnb_4bit_compute_dtype=torch.float16,
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.float16,
            quantization_config=quantization_config,
        ).eval()
    elif args_model == "Llama-3-8B":
        model_path = "meta-llama/Meta-Llama-3-8B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.bfloat16
        )
    elif args_model == "Llama-3-70B":
        model_path = "meta-llama/Meta-Llama-3-70B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.bfloat16
        )
    elif args_model == "gemma-7b":
        model_path = "google/gemma-7b-it"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.bfloat16
        )
    elif args_model == "Mistral-7B":
        model_path = "mistralai/Mistral-7B-Instruct-v0.2"  
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map="auto", torch_dtype=torch.float16
        )
    elif args_model == "Mixtral-8x7B":
        model_path = "mistralai/Mixtral-8x7B-Instruct-v0.1" 
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        quantization_config = BitsAndBytesConfig(
            llm_int4_threshold=200.0,
            bnb_4bit_compute_dtype=torch.float16,
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.float16,
            quantization_config=quantization_config,
        ).eval()
    else:
        raise ValueError(f"Unknown model: {args_model}")

    model_name = os.path.basename(model_path.rstrip("/"))

    return model_name, model, tokenizer
