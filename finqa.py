from datasets import load_dataset
import json
def item2instruction(item):
    pre_text = ('\n').join(item["pre_text"])
    post_text = ('\n').join(item["post_text"])
    rows = [(' | ').join(item) for item in item["table"]]
    table = ('----').join(rows)
    question = item["qa"]["question"]
    return {
        "source": f"{pre_text}\n{table}\n{post_text}\n{question}",
        "target": item["qa"]["answer"],
        "config": "none",
        "task": "finqa",
        "prompt": "finqa"
    }
list_test = {"finqa":{"finqa":{}}}
list_val = {"finqa":{"finqa":{}}}
list_train = {"finqa":{"finqa":{}}}


with open("FinQA/dataset/test.json", "r") as fd:
    input_file = json.load(fd)
    cnt=0
    for line in input_file:
        list_test["finqa"]["finqa"][cnt]=item2instruction(line)
        cnt+=1
with open("FinQA/dataset/dev.json", "r") as fd:
    input_file = json.load(fd)
    cnt=0
    for line in input_file:
        list_val["finqa"]["finqa"][cnt]=item2instruction(line)
        cnt+=1
with open("FinQA/dataset/train.json", "r") as fd:
    input_file = json.load(fd)
    cnt=0
    for line in input_file:
        list_train["finqa"]["finqa"][cnt]=item2instruction(line)
        cnt+=1
with open("finqa_test.json", 'w+') as fd:
    json.dump(list_test, fd, indent=4)
with open("finqa_val.json", 'w+') as fd:
    json.dump(list_val, fd, indent=4)
with open("finqa_train.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)
