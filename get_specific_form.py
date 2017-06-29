import json, requests
from config import account, token

gsf_fail = 0

###Get a specific form on the account

###Access the URL using GET
account_url = requests.request('GET', str(account + token))

###Set the account_json variable to the json output of the account_url
account_json = account_url.json()

###Check if there are forms on the account
if account_json['total'] > 0:
	###GET the specific form using it's ID in the URL
	form_id = account_json['forms'][0]['id']
	
	###Navigate to the URL for that specific form
	form_url = requests.request('GET', str(account + '/' + form_id + token))
	
	#Set the form_json variable to the json output of the form_url
	form_json = form_url.json()
	
	#If the form_url returns a status code of 200
	if form_url.status_code == 200:
		#Indicate a pass and print the form id and the name of the form
		print('PASS - The form id ' + form_id + ' for ' + account_json['forms'][0]['name'] + ' was found. See json_results/specific_form.json for more info')
		#Output the status code and json to a file located in the same directory as the script
		with open('json_results/specific_form.json', 'w') as outfile:
			json.dump(form_url.status_code, outfile)
		with open('json_results/specific_form.json', 'a') as outfile:
			json.dump(form_json, outfile)
	else:
		#Indicate a fail and state that the ID no longer exists
		print('FAIL - The requested form no longer exists.')
		gsf_fail += 1
		
###If no forms exist indicate a fail
else:
	print('FAIL - No forms exist on this account.')
	gsf_fail += 1
	
if gsf_fail == 0:
	print('Get Specific Form PASSED.')
else:
	print('Get Specific Form FAILED.')