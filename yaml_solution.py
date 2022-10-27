import yaml

output = {}
host_set = []

# get list of hosts to exclude
with open(r'host.list') as file:
    hosts = yaml.load(file, Loader=yaml.FullLoader)
    host_set = set(hosts.split(" "))

# read host.yaml
with open(r'host.yaml') as file:
    documents = yaml.full_load(file)

    for l, hosts in documents.items():
        output[l] = list(set(hosts) - host_set)

# write to file
with open(r'output.yaml', 'w') as file:
    documents = yaml.dump(output, file)