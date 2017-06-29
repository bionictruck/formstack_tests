import json, requests

account = 'https://<account url>/api/v2/form'
token = '.json?oauth_token=<token>'

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

	#If the form_url returns a status code of 200
	if form_url.status_code == 201:
		#Indicate a pass and print the form id and the name of the form
		print('PASS')
		print('The form with ID ' + form_json['id'] + ' and name ' + form_json['name'] + ' was found. JSON output written to specific_form.json')

		#Output the status code and JSON to copy_form.json
		with open('json_results/copy_form.json', 'w') as outfile:
			json.dump(form_url.status_code, outfile)
		with open('json_results/copy_form.json', 'a') as outfile:
			json.dump(form_json, outfile)

	else:
		#Indicate a fail and which status code was passed
		print('FAIL')
		print('The status code ' + str(form_url.status_code) + ' was returned')
		
#If no forms exist indicate a fail
else:
	print('FAIL')
	print('No forms are found on the account.')
	
###Attempt to copy a URL with an invalid form ID in it
invalid_url = requests.request('POST', str(account + '/aaaaaaa/copy' + token))

if invalid_url.status_code	== 404:
	print('PASS')
	print('The ID aaaaaaa is not a valid form to copy and returns a ' + str(invalid_url.status_code) + ' status code')
else:
	print('FAIL')
	print('A status code of ' + str(invalid_url.status_code) + ' was returned')
	
###Delete the newly copied form
delete_url = requests.request('DELETE', str(account + '/' + form_json['id'] + token))

#Set the delete_json variable to the JSON output of the delete_url
delete_json = delete_url.json()

#If the status code returns 200
if delete_url.status_code == 200:
	#Indicate a pass and output the JSON to delete_form.json
	print('PASS')
	print('A 200 status code was returned after delete')
	with open('json_results/delete_form.json', 'w') as outfile:
		json.dump(delete_url.status_code, outfile)
	with open('json_results/delete_form.json', 'a') as outfile:
		json.dump(delete_json, outfile)
else:
	#Indicate a fail
	print('FAIL')
	print('A status code of ' + str(delete_url.status_code) + ' was returned')

###Attempt to Delete a URL with an invalid form ID in it
invalid_delete_url = requests.request('DELETE', str(account + '/aaaaaaa' + token))

if invalid_url.status_code	== 404:
	print('PASS')
	print('The ID aaaaaaa is not a valid form to delete and returns a ' + str(invalid_url.status_code) + ' status code')
else:
	print('FAIL')
	print('A status code of ' + str(invalid_url.status_code) + ' was returned')