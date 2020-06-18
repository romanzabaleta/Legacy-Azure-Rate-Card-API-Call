import os
import json
import subprocess

class az():
    def tojson(input, filename):
        output = str(subprocess.check_output(input,stderr=subprocess.STDOUT, shell=True))
        output = output[output.find("{"):]
        output = output[:output.rfind("}")+1]
        output = output.replace("\\r\\n", "")
        output = output.replace(" ", "")
        output = output.replace(",", ", ")
        output = json.loads(output)
        with open(filename+'.json', 'w') as outfile:
            json.dump(output, outfile)
        return output


loginfo = az.tojson("az login","accountinfo")
print("accountinfo.json created")

os.system('cmd /c "az provider register --namespace Microsoft.Compute"')
os.system('cmd /c "az provider register --namespace Microsoft.Resources"')
os.system('cmd /c "az provider register --namespace Microsoft.ContainerService"')
os.system('cmd /c "az provider register --namespace Microsoft.Commerce"')

subID = loginfo["id"]

data = {"Name": "MyRateCardRole", "IsCustom": "true", "Description": "Rate Card query role",
       "Actions": ["Microsoft.Compute/virtualMachines/vmSizes/read",
                    "Microsoft.Resources/subscriptions/locations/read",
                    "Microsoft.Resources/providers/read",
                    "Microsoft.ContainerService/containerServices/read",
                    "Microsoft.Commerce/RateCard/read"],
        "AssignableScopes": ["/subscriptions/" + subID + ""]}

with open('myrole.json', 'w') as outfile:
    json.dump(data, outfile)

os.system('cmd /c "az role definition create --verbose --role-definition @myrole.json"')

az.tojson('''az ad sp create-for-rbac --name "MyServicePrincipal" --role "MyRateCardRole" --sdk-auth true''',"my_credentials")




