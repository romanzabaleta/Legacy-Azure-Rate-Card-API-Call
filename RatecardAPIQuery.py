import os
import json
import subprocess

class az():
    def token(input):
        output = str(subprocess.check_output(input, shell=True))
        output = output.replace("\\x1b[0m'", '')
        output = output.replace('\\r\\n', '')
        output = output.replace("b'", "")
        output = output.replace(' ', '')
        output = output.replace(",", ", ")
        output = output.replace("'", "")
        output = json.loads(output)
        return output["access_token"]


cred= open('my_credentials.json', 'r')
act = open('accountinfo.json', 'r')

cdata = json.load(cred)
adata = json.load(act)

clientId = cdata['clientId']
clientSecret = cdata['clientSecret']
tenantId = adata['tenantId']

act.close()
cred.close()

command = "curl https://login.microsoftonline.com/"+tenantId+"/oauth2/token \
-F grant_type=client_credentials \
-F resource=https://management.core.windows.net/ \
-F client_id="+clientId+" \
-F client_secret="+clientSecret

btoken = az.token(command)

subid = adata["id"]

apicall = '''curl -L "https://management.azure.com/subscriptions/''' + subid +'''/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&%24filter=OfferDurableId+eq+'MS-AZR-0003P'+and+Currency+eq+'USD'+and+Locale+eq+'en-US'+and+RegionInfo+eq+'US'" -H "Authorization: Bearer '''+btoken+''' ">output.json'''



subprocess.check_output(apicall, shell=True)
