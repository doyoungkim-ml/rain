from datasets import load_dataset
import json
def item2instruction(item):
    premise = item["sentence1"]
    hypothesis = item["sentence2"]
    return {
        "source": f"Classify the relation between the following two sentences as one of entailment, neutral, or contradiction:\n\nSentence 1: {premise}\n\nSentence 2: {hypothesis}",
        "target": item["gold_label"],
        "labels_list":["entailment", "contradiction", "neutral"],
        "config": "none",
        "task": "mednli",
        "prompt": "mednli"
    }
# # for item in file:
# print(file)
list_test = {"mednli":{"mednli":{}}}
list_val = {"mednli":{"mednli":{}}}
list_train = {"mednli":{"mednli":{}}}


with open("mednli-a-natural-language-inference-dataset-for-the-clinical-domain-1.0.0/mli_test_v1.jsonl", "r") as input_file:
    cnt=0
    for line in input_file:
        list_test["mednli"]["mednli"][cnt]=item2instruction(json.loads(line))
        cnt+=1
with open("mednli-a-natural-language-inference-dataset-for-the-clinical-domain-1.0.0/mli_dev_v1.jsonl", "r") as input_file:
    cnt=0
    for line in input_file:
        list_val["mednli"]["mednli"][cnt]=item2instruction(json.loads(line))
        cnt+=1
with open("mednli-a-natural-language-inference-dataset-for-the-clinical-domain-1.0.0/mli_train_v1.jsonl", "r") as input_file:
    cnt=0
    for line in input_file:
        list_train["mednli"]["mednli"][cnt]=item2instruction(json.loads(line))
        cnt+=1
with open("mednli_test.json", 'w+') as fd:
    json.dump(list_test, fd, indent=4)
with open("mednli_val.json", 'w+') as fd:
    json.dump(list_val, fd, indent=4)
with open("mednli_train.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)
