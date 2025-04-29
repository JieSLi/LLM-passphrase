""" utils for main_sample.py
"""

import argparse
import datetime
import json
import os

import torch
import torch.nn.functional as F


def pw_sample_top_p(probs, q, p, eos_tok_id, end_token_ids):

    probs_sort, probs_idx = torch.sort(probs, dim=-1, descending=True)

    probs_sum = torch.cumsum(probs_sort, dim=-1)

    # for p
    mask = probs_sum - probs_sort > p

    # for q:
    if q > 0.0:
        l_mask = probs_sum < q
        ind = (probs_sum >= q).int().argmax(dim=-1, keepdim=True)
        ind_diff = q - torch.sum(probs_sort * l_mask, dim=-1, keepdim=True)
        probs_sort[torch.arange(probs_sort.size(0)).unsqueeze(1), ind] -= ind_diff

        probs_sort[l_mask] = 0.0

    # for p
    probs_sort[mask] = 0.0

    probs_sort.div_(probs_sort.sum(dim=-1, keepdim=True))

    next_token = torch.multinomial(probs_sort, num_samples=1)
    token_ent = -torch.log2(torch.gather(probs_sort, -1, next_token))
    next_token = torch.gather(probs_idx, -1, next_token)

    if end_token_ids:

        sums_end_probs = torch.zeros(probs.size(0), device=probs_sort.device)

        for row in range(probs.size(0)):
            if next_token[row].item() in end_token_ids:
                for token in end_token_ids:
                    token_pos = (probs_idx[row] == token).nonzero(as_tuple=True)
                    sums_end_probs[row] += probs_sort[row, token_pos].sum()
                token_ent[row] = -torch.log2(sums_end_probs[row])

        mask = torch.isin(
            next_token, torch.tensor(end_token_ids, device=next_token.device)
        )
        next_token[mask] = eos_tok_id

    return next_token, token_ent


def logger(
    tokenizer, out_dir, model_name, in_str, toks_ents_str, temperature, top_p, bot_q
):
    """log each batch (input, output toks, output_ents, sum_ents)"""

    bsz = len(toks_ents_str)
    batch_log = [dict(model=model_name, quote=in_str) for ind in range(bsz)]

    for a_dict, (out_tokens, out_tokens_ent, a_str) in zip(batch_log, toks_ents_str):
        a_dict["out_tokens"] = out_tokens
        a_dict["out_tokens_ent"] = [round(it, 2) for it in out_tokens_ent]
        a_dict["sent_ent"] = round(sum(out_tokens_ent), 2)
        a_dict["out_sent"] = a_str
        a_dict["num_words"] = len(a_str.split())
        a_dict["temp"] = temperature
        a_dict["top_p"] = top_p
        a_dict["bot_q"] = bot_q
        a_dict["id_tok_ent"] = [
            (tid, tokenizer.convert_ids_to_tokens(tid), round(t_ent, 2))
            for tid, t_ent in zip(out_tokens, out_tokens_ent)
        ]

    log_file = "_".join(in_str[:80].replace(".", "").replace("?", "").split()) + ".json"
    log_file = model_name + "_" + log_file

    write_json(batch_log, out_dir=out_dir, log_file=log_file)


def log_args(out_dir, model_name, quote_label, args, temp_list, top_p_list):
    """write to out_dir args, temp_list and top_p list"""

    current_datetime = datetime.datetime.now()
    date_str = current_datetime.strftime("%Y_%m_%d")
    fname = os.path.join(
        out_dir, f"{model_name}_{quote_label}__args_log_{date_str}.txt"
    )
    with open(fname, "w") as file:
        print(args, file=file)
        print("temp:", temp_list, file=file)
        print("top_p:", top_p_list, file=file)


def write_json(batch_log, out_dir="./output_dir", log_file="test_stats.json"):
    """
    write output json files
    """

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    if isinstance(batch_log, dict):
        data_from_json = {"num_entries": 1, 0: batch_log}
    elif isinstance(batch_log, list):
        data_from_json = {
            "num_entries": 0,
        }
        for i in range(len(batch_log)):
            data_from_json[i] = batch_log[i]
        data_from_json["num_entries"] += len(batch_log)
    else:
        raise ValueError("Invalid data format for to_json")

    fname = os.path.join(out_dir, log_file)
    base_name = os.path.splitext(fname)[0]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    fname = base_name + "_" + timestamp + ".json"

    with open(fname, "w") as fp:
        json.dump(data_from_json, fp)


def main(args):

    print(f"running main() of {os.path.basename(__file__)}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="utilities functions")
    args = parser.parse_args()
    print(f"running {os.path.basename(__file__)} with args:\n{args}")

    main(args)
