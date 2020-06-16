import os
import json

cred = open('my_credentials.json', 'r')
act = open('accountinfo.json','r')

cdata = json.load(cred)
adata = json.load(cred)

clientId = cdata['clientId']
clientSecret = cdata['clientSecret']
tenantId = adata['tenantId']

act.close()
cred.close()

command = "curl https://login.microsoftonline.com/"+tenantId+"/oauth2/token \ -F grant_type=client_credentials \
-F resource=https://management.core.windows.net/ \
-F client_id="+clientId+" \
-F client_secret="+clientSecret

os.system('cmd /c '+command)

btoken = input("\nEnter the output of the last command: ")

subid = adata["id"]

apicall = '''curl -L "https://management.azure.com/subscriptions/''' + subid +'''/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&%24filter=OfferDurableId+eq+'MS-AZR-0003P'+and+Currency+eq+'USD'+and+Locale+eq+'en-US'+and+RegionInfo+eq+'US'" -H "Authorization: Bearer '''+btoken+''' "'''

os.system('cmd /c '+apicall+'> output.json')
