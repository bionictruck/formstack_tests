import json, requests

account = 'https://<account url>/api/v2/form'
token = '.json?oauth_token=<token>'

###Get all forms on the account, shows how many forms there are and the response code returned

###Access the URL using GET
account_url = requests.request('GET', str(account + token))

###Set the account_json variable to the json output of the account_url
account_json = account_url.json()

###Determine if forms exist on the account
if account_json['total'] > 0:
#If forms exist print the message indicating how many
	print('PASS')
	print('The account contains ' + str(account_json['total']) + ' forms')
	#Output the json to a file located in the same directory as the script
	with open('json_results/all_forms.json', 'w') as outfile:
		json.dump(account_json, outfile)
else:
#If no forms exist, print the message and quit the script
	print('FAIL')
	print('No forms were found on this account.')
	
###Determine if the Response Code was 200
if account_url.status_code == 200:
#If it is print the messages indicating a Pass
	print('PASS')
	print('A Response code of ' + str(account_url.status_code) + ' was passed')
else:
#If not print the message incating a fail and what response code was passed
	print('FAIL')
	print('A Response code of ' + str(account_url.status_code) + ' was passed, a 200 was expected.')