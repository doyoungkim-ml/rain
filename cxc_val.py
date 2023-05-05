import json
import csv
import random
path = "./Crisscrossed-Captions/sts_val.json"
cxc_path = "./Crisscrossed-Captions/data/sts_val.csv"
data = json.load(open(path, "r"))
sentids={}
dict_train = {"cxc":{"cxc":{}}}
list_train=[]
dict_val = {"cxc":{"cxc":{}}}
for example in data["images"]:
    for item in example["sentences"]:
        sentence = item["raw"]
        sentid = str(item["sentid"])
        if sentid not in sentids.keys():
            sentids[sentid]=sentence
# with open("sentids_train.json", 'w+') as fd:
#     json.dump(sentids, fd, indent=4)
    
reader = csv.reader(open(cxc_path, "r"), delimiter=",")
next(reader)  # Skip header.
for row in reader:
    caption1,caption2,agg_score,sampling_method = row
    sent1=sentids[str(caption1.split(":")[-1])]
    sent2=sentids[str(caption2.split(":")[-1])]
    # print(sent1)
    
    # print(caption1.split(":")[-1])
    score = float(agg_score)
    if sent1!="" and sent2!="":
        if score<2.0:
            answer = "No"
        elif score<3.5:
            answer = "Maybe"
        else:
            answer = "Yes"
        list_train.append({
            "source": f"Given \"{sent1}\" Can we say that \"{sent2}\" is correct? Yes, No, or Maybe?",
            "target": answer,
            "labels_list":["Yes", "No", "Maybe"],
            "config": "none",
            "task": "cxc",
            "prompt": "cxc"
        })

random.shuffle(list_train)
val = list_train[:1024]
train = list_train[1024:]
cnt=0
for item in train:
    dict_train["cxc"]["cxc"][str(cnt)]=item
    cnt+=1
with open("cxc_train.json", 'w+') as fd:
    json.dump(dict_train, fd, indent=4)
cnt=0
for item in val:
    dict_val["cxc"]["cxc"][str(cnt)]=item
    cnt+=1
with open("cxc_val.json", 'w+') as fd:
    json.dump(dict_val, fd, indent=4)
    


            
