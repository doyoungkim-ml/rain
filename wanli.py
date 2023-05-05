from datasets import load_dataset
import json
file = load_dataset("alisawuffles/WANLI")
def item2instruction(item):
    premise = item["premise"]
    hypothesis = item["hypothesis"]
    return {
        "source": f"Given \"{premise}\" Should we assume that \"{hypothesis}\" is true?",
        "target": item["gold"],
        "labels_list": ["entailment", "contradiction", "neutral"],
        "config": "none",
        "task": "wanli",
        "prompt": "wanli"
    }
# # for item in file:
# print(file)
list_test = {"wanli":{"wanli":{}}}
list_val = {"wanli":{"wanli":{}}}
list_train = {"wanli":{"wanli":{}}}
test = load_dataset("alisawuffles/WANLI", split="test")
train = load_dataset("alisawuffles/WANLI", split="train[1024:]")
val = load_dataset("alisawuffles/WANLI", split="train[:1024]")
for item in test:
    list_test["wanli"]["wanli"][item["id"]]=(item2instruction(item))
with open("wanli_test.json", 'w+') as fd:
    json.dump(list_test, fd, indent=4)
for item in val:
    list_val["wanli"]["wanli"][item["id"]]=(item2instruction(item))
with open("wanli_dev.json", 'w+') as fd:
    json.dump(list_val, fd, indent=4)
for item in train:
    list_train["wanli"]["wanli"][item["id"]]=(item2instruction(item))
with open("wanli_train.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)