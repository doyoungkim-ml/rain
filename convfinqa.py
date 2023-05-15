from datasets import load_dataset
import json
def item2instruction(item):
    pre_text = ('\n').join(item["pre_text"])
    post_text = ('\n').join(item["post_text"])
    rows = [(' | ').join(item) for item in item["table"]]
    table = ('----').join(rows)
    if "qa" not in item.keys():
        q="qa_0"
    else:
        q="qa"

    question = item[q]["question"]
    return {
        "source": f"{pre_text}\n{table}\n{post_text}\n{question}",
        "target": item[q]["answer"],
        "config": "none",
        "task": "convfinqa",
        "prompt": "convfinqa"
    }
list_test = {"convfinqa":{"convfinqa":{}}}
list_val = {"convfinqa":{"convfinqa":{}}}
list_train = {"convfinqa":{"convfinqa":{}}}


with open("ConvFinQA/data/dev.json", "r") as fd:
    input_file = json.load(fd)
    cnt=0
    for line in input_file:
        list_val["convfinqa"]["convfinqa"][cnt]=item2instruction(line)
        cnt+=1
with open("ConvFinQA/data/train.json", "r") as fd:
    input_file = json.load(fd)
    cnt=0
    for line in input_file:
        list_train["convfinqa"]["convfinqa"][cnt]=item2instruction(line)
        cnt+=1

with open("convfinqa_val.json", 'w+') as fd:
    json.dump(list_val, fd, indent=4)
with open("convfinqa_train.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)
