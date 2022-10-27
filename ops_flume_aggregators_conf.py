from importlib.abc import Loader
from os import remove
import yaml
import copy
import sys
import ruamel.yaml

# with open('/tmp/sample', 'r') as flume_remove_file:
#     open_hosts_file = flume_remove_file.read()
#     flume_remove_list = open_hosts_file.split()

# yaml = ruamel.yaml.YAML()
# with open('/tmp/aggregators-conf.yaml') as fp:
#     data = yaml.load(fp)
#     print(f"data {data}")
#     for hosts in data.values():
#         print(hosts)
#         if flume_remove_list in hosts:
#             print(data[1])
#             del data[1][flume_remove_list]
#             yaml.dump(data, sys.stdout)
# del data[1]['misc_props']
# yaml.dump(data, sys.stdout)

# flume_hosts = []
# with open('/tmp/aggregators-conf.yaml') as file:
#     host_list = yaml.load(file, Loader=yaml.FullLoader)
#     # print(list(host_list.values()))
#     for host in host_list.values():
#         flume_hosts.append(host)
#     print(f"{flume_hosts}")

# remove_hosts  = []


# with open('/tmp/sample', 'r') as flume_remove_file:
#     open_hosts_file = flume_remove_file.read()
#     flume_remove_list = open_hosts_file.split()
#     print(content_list)
#     print(type(content_list))

# with open('/tmp/aggregators-conf.yaml', 'r') as stream:
#     yaml_data = yaml.load(stream, Loader=yaml.FullLoader)

# hosts_by_tier = dict()
# tiers = sorted(yaml_data.keys())
# for tier in tiers:
#     hosts_by_tier[tier] = list(sorted(yaml_data[tier]))

# for tier in tiers:
#     hosts = hosts_by_tier[tier]
#     original_hosts = copy.deepcopy(hosts)

# # print(f"hosts_by_tier {hosts_by_tier}")
# print(f"original_hosts {original_hosts}")