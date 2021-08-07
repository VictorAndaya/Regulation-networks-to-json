import json
import inflect

# the file to be converted
filename = './network_tf_gene.txt'

# resultant list
nodes = list()
edges = list()
description = list()

dictonary = {}

count = 1
already_exist_node = set()
already_exist_edge = set()

with open(filename) as fh:

    for line in fh:
        if line[0] == "#":
            continue
        # reading line by line from the text file
        description.append(line.strip().split("\t"))

    for inner_list in description:
        if not inner_list[0] in already_exist_node:
            nodes.append(
                {'data': {'id': inner_list[0], 'label': inner_list[1], 'network': "TF", 'effect': inner_list[4]}})
        if not inner_list[2] in already_exist_node:
            nodes.append(
                {'data': {'id': inner_list[2], 'label': inner_list[3], 'network': "GENE", 'effect': inner_list[4]}})
        if not inner_list[2] in already_exist_node:
            edges.append(
                {'data': {'id': count, 'source': inner_list[0], 'target': inner_list[2]}})
        count += 1
        already_exist_node.add(inner_list[0])
        already_exist_node.add(inner_list[2])

    dictonary['nodes'] = nodes
    dictonary['edges'] = edges
# creating json file
out_file = open("test2.json", "w")
json.dump(dictonary, out_file, indent=4)
out_file.close()
