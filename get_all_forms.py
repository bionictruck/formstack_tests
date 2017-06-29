import json, requests
from config import account, token

gaf_fail = 0

###Get all forms on the account, shows how many forms there are and the response code returned

###Access the URL using GET
account_url = requests.request('GET', str(account + token))

###Set the account_json variable to the json output of the account_url
account_json = account_url.json()

###Determine if forms exist on the account
if account_json['total'] > 0:
#If forms exist print a PASS message
	print('PASS - Forms found. See json_results/all_forms.json for more info')
	#Output the json to a file located in the same directory as the script
	with open('json_results/all_forms.json', 'w') as outfile:
		json.dump(account_json, outfile)
else:
#If no forms exist, print the message
	print('FAIL - No forms exist on this account.')
	gaf_fail += 1
	
	
###Determine if the Response Code was 200
if account_url.status_code == 200:
#If it is print the messages indicating a Pass
	print('PASS - A Status Code of 200 was received.')
else:
#If not print the message incating a fail and what response code was passed
	print('FAIL - A Status Code of ' + account_url.status_code + ' was received. 200 was expected.')
	gaf_fail += 1
	
if gaf_fail == 0:
	print('Get All Forms PASSED.')
else:
	print('Get All Forms FAILED.')