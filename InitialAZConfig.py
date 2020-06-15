import os
import json


os.system('cmd /c "az login > AZLoginOutput.txt')
print("Created AZLoginOutput.txt")
os.system('cmd /c "az provider register --namespace Microsoft.Compute"')
os.system('cmd /c "az provider register --namespace Microsoft.Resources"')
os.system('cmd /c "az provider register --namespace Microsoft.ContainerService"')
os.system('cmd /c "az provider register --namespace Microsoft.Commerce"')


subID = input("Enter id as written in AZLoginOutput.txt: ")

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

os.system('cmd /c "az ad sp create-for-rbac --name "MyServicePrincipal" --role "MyRateCardRole" --sdk-auth true \
> my_credentials.json"')













