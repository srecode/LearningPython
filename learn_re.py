import re

def learn_re_or(url):
    # if re.search(r"devel", url) or re.search(r"stage", url):
    if re.search(r"devel"|"stage", url):
        return url

url = "https://dataplatform-cluster-operator-stage-0001.qus1.twttr.net/v1/clusters/flags/hadoop-ietst@qus1"

print(learn_re_or(url))
    