#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os

'''
Create a couple galaxy/cluster with cti's courses-of-action 
Must be in the mitre/cti/ATTACK/course-of-action folder
'''

values = []

for element in os.listdir('.'):
    if element.endswith('.json'):
        with open(element) as json_data:
            d = json.load(json_data)
            json_data.close()

            temp = d['objects'][0]

            value = {}
            value['description'] = temp['description']
            value['value'] = temp['name']
            value['meta'] = {}
            value['meta']['uuid'] = re.search('--(.*)$', temp['id']).group(0)[2:]
            values.append(value)

galaxy = {}
galaxy['name'] = "Course of Action"
galaxy['type'] = "course-of-action"
galaxy['description'] = "ATT&CK Mitigation"
galaxy['uuid' ] = "6fcb4472-6de4-11e7-b5f7-37771619e14e"
galaxy['version'] = 1

cluster = {} 
cluster['name'] = "Course of Action"
cluster['type'] = "course-of-action"
cluster['description'] = "ATT&CK Mitigation"
cluster['version'] = 1
cluster['source'] = "https://github.com/mitre/cti"
cluster['uuid' ] = "a8825ae8-6dea-11e7-8d57-7728f3cfe086"
cluster['authors'] = ["MITRE"]
cluster['values'] = values

with open('generate/galaxies/mitre_course-of-action.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre_course-of-action.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
