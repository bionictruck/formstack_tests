import json, requests
from config import account, token

cdf_fail = 0

###Copy and Delete Forms

###Access the URL using GET
account_url = requests.request('GET', str(account + token))

###Set the account_json variable to the json output of the account_url
account_json = account_url.json()

###Check if there are forms on the account
if account_json['total'] > 0:
	#GET the specific form using it's ID in the URL
	form_id = account_json['forms'][0]['id']
	
	###Submit a POST to copy that form
	form_url = requests.request('POST', str(account + '/' + form_id + '/copy' + token))
	
	#Set the form_json variable to the json output of the form_url
	form_json = form_url.json()

	#If the form_url returns a status code of 201
	if form_url.status_code == 201:
		#Indicate a pass and print the form id and the name of the form
		print('PASS - The form with ID ' + form_json['id'] + ' and name ' + form_json['name'] + ' was found. JSON output written to json_results/copy_form.json')

		#Output the status code and JSON to copy_form.json
		with open('json_results/copy_form.json', 'w') as outfile:
			json.dump(form_url.status_code, outfile)
		with open('json_results/copy_form.json', 'a') as outfile:
			json.dump(form_json, outfile)

	else:
		#Indicate a fail and which status code was passed
		print('FAIL - A Status Code of ' + form_url.status_code + ' was passed. Expect 201')
		cdf_fail += 1
		
#If no forms exist indicate a fail
else:
	print('FAIL - No forms exist on this account.')
	cdf_fail += 1
	
###Attempt to copy a URL with an invalid form ID in it
invalid_url = requests.request('POST', str(account + '/aaaaaaa/copy' + token))

if invalid_url.status_code	== 404:
	print('PASS - URL with an invalid id could not be copied')
else:
	print('FAIL - A status code of ' + invalid_url.status_code + ' was passed. Expected 404.')
	cdf_fail += 1
	
###Delete the newly copied form
delete_url = requests.request('DELETE', str(account + '/' + form_json['id'] + token))

#Set the delete_json variable to the JSON output of the delete_url
delete_json = delete_url.json()

#If the status code returns 200
if delete_url.status_code == 200:
	#Indicate a pass and output the JSON to delete_form.json
	print('PASS - A Status Code of 200 was received, indicating the form was deleted. See json_results/delete_form.json for more info.')
	with open('json_results/delete_form.json', 'w') as outfile:
		json.dump(delete_url.status_code, outfile)
	with open('json_results/delete_form.json', 'a') as outfile:
		json.dump(delete_json, outfile)
else:
	#Indicate a fail
	print('FAIL - A Status Code of ' + delete_url.status_code + ' was received. Expected 200.')
	cdf_fail += 1

###Attempt to Delete a URL with an invalid form ID in it
invalid_delete_url = requests.request('DELETE', str(account + '/aaaaaaa' + token))

if invalid_url.status_code	== 404:
	print('PASS - A Status Code of 404 was returned, indicating a URL with an invalid id could not be deleted.')
else:
	print('FAIL - A Status Code of ' + invalid_url.status_code + ' was returned. Expected 404.')
	cdf_fail += 1
	
if cdf_fail == 0:
	print('Get Specific Form PASSED.')
else:
	print('Get Specific Form FAILED.')
