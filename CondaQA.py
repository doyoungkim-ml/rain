from datasets import load_dataset
import json
file = load_dataset("lasha-nlp/CONDAQA")
def item2instruction(item):
    premise = item["sentence1"]
    hypothesis = item["sentence2"]
    return {
        "source": f"Given \"{premise}\" Should we assume that \"{hypothesis}\" is true?",
        "target": item["label"],
        "labels_list":["YES", "DON'T KNOW", "NO"],
        "config": "none",
        "task": "condaqa",
        "prompt": "condaqa"
    }
list_test = {"condaqa":{"condaqa":{}}}
list_val = {"condaqa":{"condaqa":{}}}
list_train = {"condaqa":{"condaqa":{}}}
test = load_dataset("lasha-nlp/CONDAQA", split="test")
val = load_dataset("lasha-nlp/CONDAQA", split="validation")
train = load_dataset("lasha-nlp/CONDAQA",split="train")
for item in test:
    list_test["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
with open("condaqa_test.json", 'w+') as fd:
    json.dump(list_test, fd, indent=4)
for item in val:
    list_val["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
with open("condaqa_dev.json", 'w+') as fd:
    json.dump(list_val, fd, indent=4)
for item in train:
    list_train["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
with open("condaqa_train.json", 'w+') as fd:
    json.dump(list_train, fd, indent=4)