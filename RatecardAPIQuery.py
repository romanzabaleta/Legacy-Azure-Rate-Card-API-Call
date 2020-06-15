import os
import json

f = open('my_credentials.json', 'r')

cdata = json.load(f)

clientid = cdata['clientId']
clientsecret = cdata['clientSecret']
tenantid = input("Enter the tenantId in the AZLoginOutput.txt: ")

f.close()
command = "curl https://login.microsoftonline.com/"+tenantid+"/oauth2/token \ -F grant_type=client_credentials \
-F resource=https://management.core.windows.net/ \
-F client_id="+clientid+" \
-F client_secret="+clientsecret

os.system('cmd /c '+command)

btoken = input("\nEnter the output of the last command: ")

subid = input("\nEnter the id (subscription id) in the AZLoginOutput.txt: ")

apicall = '''curl -L "https://management.azure.com/subscriptions/''' + subid +'''/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&%24filter=OfferDurableId+eq+'MS-AZR-0003P'+and+Currency+eq+'USD'+and+Locale+eq+'en-US'+and+RegionInfo+eq+'US'" -H "Authorization: Bearer '''+btoken+''' "'''

os.system('cmd /c '+apicall+'> output.json')
