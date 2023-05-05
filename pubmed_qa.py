from datasets import load_dataset
import json
import random
import os
import ast
def item2instruction(item):
    hypothesis = item["question"]
    context_dict = ast.literal_eval(str(item["context"]))
    premise = ('\n').join(context_dict["contexts"])
    context={}
    context["source"]= f"\"{premise}\"\nQuestion:\n\"{hypothesis}\"",
    context["target"]=item["final_decision"]
    context["list_label"]=["yes", "no", "maybe"]
    context["config"]="none"
    context["task"]="pubmed_qa"
    context["prompt"]="pubmed_qa"
    return context
list_test = {"pubmed_qa":{"pubmed_qa":{}}}
list_val = {"pubmed_qa":{"pubmed_qa":{}}}
list_train = {"pubmed_qa":{"pubmed_qa":{}}}
rnd_seed=84
data = load_dataset("pubmed_qa", "pqa_labeled", split="train")
split = data.train_test_split(test_size=0.5, seed=rnd_seed)
test = split['test']
# print(test)
for i in range(10):
    val_ds = split['train'].shard(num_shards=10, index=i)
    for item in val_ds:
        list_test["pubmed_qa"]["pubmed_qa"][item["pubid"]]=(item2instruction(item))
    with open(f"pub_med/{str(rnd_seed)}/pubmed_qa_val_{i}.json", 'w+') as fd:
        json.dump(list_test, fd, indent=4)
for item in test:
    list_train["pubmed_qa"]["pubmed_qa"][item["pubid"]]=(item2instruction(item))
with open(f"pub_med/{str(rnd_seed)}/pubmed_qa_test.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)