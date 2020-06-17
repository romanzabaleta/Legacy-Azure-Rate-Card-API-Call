import os
import json
import subprocess

class az():
    def login(input, filename):
        output = str(subprocess.check_output(input, shell=True))
        output = output.replace('\\r\\n','')
        output = output.replace(' ','')
        output = output.replace("b'[","")
        output = output.replace("]\\x1b[0m'","")
        output = output.replace(",",", ")
        output = json.loads(output)
        with open(filename+'.json', 'w') as outfile:
            json.dump(output, outfile)
        return output
    def cred(input, filename):
        output = str(subprocess.check_output(input, shell=True))
        output = output.replace("\\x1b[0m'",'')
        output = output.replace('\\r\\n', '')
        output = output.replace("b'", "")
        output = output.replace(' ', '')
        output = output.replace(",", ", ")
        print(output)
        output = json.loads(output)
        with open(filename+'.json', 'w') as outfile:
            json.dump(output, outfile)
        return output


loginfo = az.login("az login","accountinfo")
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

az.cred('''az ad sp create-for-rbac --name "MyServicePrincipal" --role "MyRateCardRole" --sdk-auth true''',"my_credentials")




