import json
import csv
path = "./Crisscrossed-Captions/sts_test.json"
cxc_path = "./Crisscrossed-Captions/data/sts_test.csv"
data = json.load(open(path, "r"))
sentids={}
list_test = {"cxc":{"cxc":{}}}
for example in data["images"]:
    for item in example["sentences"]:
        sentence = item["raw"]
        sentid = str(item["sentid"])
        if sentid not in sentids.keys():
            sentids[sentid]=sentence
# with open("sentids_test.json", 'w+') as fd:
#     json.dump(sentids, fd, indent=4)
    
reader = csv.reader(open(cxc_path, "r"), delimiter=",")
next(reader)  # Skip header.
cnt = 0
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
        list_test["cxc"]["cxc"][str(cnt)]={
            "source": f"Given \"{sent1}\" Can we say that \"{sent2}\" is correct? Yes, No, or Maybe?",
            "target": answer,
            "labels_list":["Yes", "No", "Maybe"],
            "config": "none",
            "task": "cxc",
            "prompt": "cxc"
        }
        cnt+=1
with open("cxc_test.json", 'w+') as fd:
    json.dump(list_test, fd, indent=4)
    

            
