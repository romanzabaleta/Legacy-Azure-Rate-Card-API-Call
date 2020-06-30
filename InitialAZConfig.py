import os
import json
from jsoncommands import jsoncmd

class az():
    def configuration(loginfo): #Configures Azure account to make ratecard API calls
        os.system('cmd /c "az provider register --namespace Microsoft.Compute"')
        os.system('cmd /c "az provider register --namespace Microsoft.Resources"')
        os.system('cmd /c "az provider register --namespace Microsoft.ContainerService"')
        os.system('cmd /c "az provider register --namespace Microsoft.Commerce"')
        subid = loginfo["id"]
        data = {"Name": "MyRateCardRole",
                "IsCustom": "true",
                "Description": "Rate Card query role",
                "Actions": ["Microsoft.Compute/virtualMachines/vmSizes/read",
                            "Microsoft.Resources/subscriptions/locations/read",
                            "Microsoft.Resources/providers/read",
                            "Microsoft.ContainerService/containerServices/read",
                            "Microsoft.Commerce/RateCard/read"],
                "AssignableScopes": ["/subscriptions/" + subid + ""]}
        with open('myrole.json', 'w') as outfile:
            json.dump(data, outfile)
            print("myrole.json created/updated")
        os.system('cmd /c "az role definition create --verbose --role-definition @myrole.json"')
        jsoncmd.savejson('''az ad sp create-for-rbac --name "MyServicePrincipal" --role "MyRateCardRole" --sdk-auth true''',"my_credentials")

def main():
    loginfo = jsoncmd.savejson("az login", "accountinfo")
    az.configuration(loginfo)

if __name__ == "__main__":
    main()









