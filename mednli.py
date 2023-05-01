from datasets import load_dataset
import json
def item2instruction(item):
    new = item
    new["config"]="none"
    new["task"]="mednli"
    new["prompt"]="mednli"
    return new
# # for item in file:
# print(file)
list_test = {"mednli":{"mednli":{}}}
list_val = {"mednli":{"mednli":{}}}
list_train = {"mednli":{"mednli":{}}}
test = load_dataset("bigbio/mednli","mednli_bigbio_te")
val = load_dataset("bigbio/mednli", "mednli_source")
print(test[0])
pritn(val[0])
# train = load_dataset("bigbio/mednli",split="train")
# for item in test:
    # list_test["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
# with open("condaqa_test.json", 'w+') as fd:
#     json.dump(list_test, fd, indent=4)
# for item in val:
#     list_val["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
# with open("condaqa_dev.json", 'w+') as fd:
#     json.dump(list_val, fd, indent=4)
# for item in train:
#     list_train["condaqa"]["condaqa"][item["SampleID"]]=(item2instruction(item))
# with open("condaqa_train.json", 'w+') as fd:
#     json.dump(list_train, fd, indent=4)