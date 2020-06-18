import os
import json
import subprocess

class az():
    def usejson(input):
        output = str(subprocess.check_output(input, stderr=subprocess.STDOUT, shell=True))
        output = output[output.find("{"):]
        output = output[:output.rfind("}") + 1]
        output = output.replace("\\r\\n", "")
        output = output.replace(" ", "")
        output = output.replace(",", ", ")
        output = json.loads(output)
        return output

    def savejson(input, filename):
        output = str(subprocess.check_output(input,stderr=subprocess.STDOUT, shell=True))
        output = output[output.find("{"):]
        output = output[:output.rfind("}")+1]
        output = output.replace("\\r\\n", "")
        output = output.replace(" ", "")
        output = output.replace(",", ", ")
        with open(filename+'.json', 'w') as outfile:
            outfile.write(output)
            outfile.close()


cred = open('my_credentials.json', 'r')
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

btoken = az.usejson(command)["access_token"]

subid = adata["id"]

apicall = '''curl -L "https://management.azure.com/subscriptions/''' + subid +'''/providers/Microsoft.Compute/skus?api-version=2019-04-01" -H "Authorization: Bearer '''+btoken

az.savejson(apicall,"SKUOutput")