import json;
from urllib.request import urlopen
import pdb

citizen = open('data/citizen.json').read()
citizens = json.loads(citizen)

newlist = []

for cobj in citizens:
	citizen = {}
	citizen['model'] = cobj['model']
	citizen['pk'] = cobj['fields']['citizen_uid']
	citizen['fields'] = {}
	citizen['fields']['name_bangla'] = cobj['fields']['name_bangla']
	citizen['fields']['name'] = cobj['fields']['name']
	citizen['fields']['nid'] = cobj['fields']['nid']
	citizen['fields']['dob'] = cobj['fields']['dob']
	citizen['fields']['gender'] = cobj['fields']['gender']
	citizen['fields']['post_office'] = cobj['fields']['post_office']
	citizen['fields']['post_code'] = cobj['fields']['post_code']
	citizen['fields']['father_name'] = cobj['fields']['father_name']
	citizen['fields']['mother_name'] = cobj['fields']['mother_name']
	citizen['fields']['spouse_name'] = cobj['fields']['spouse_name']

	citizen['fields']['village'] = cobj['fields']['citizen_uid'][:12]
	citizen['fields']['word'] = cobj['fields']['citizen_uid'][:10]
	citizen['fields']['union'] = cobj['fields']['citizen_uid'][:8]
	

	newlist.append(citizen)

newcitizen = open('data/newcitizen.json', 'w')
json.dump(newlist, newcitizen, indent=2)
