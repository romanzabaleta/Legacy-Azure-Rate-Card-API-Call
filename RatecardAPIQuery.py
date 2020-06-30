from jsoncommands import jsoncmd

def main():
    cdata = jsoncmd.loadjson('my_credentials.json')
    adata = jsoncmd.loadjson('accountinfo.json')
    clientId = cdata['clientId']
    clientSecret = cdata['clientSecret']
    tenantId = adata['tenantId']
    command = "curl https://login.microsoftonline.com/" + tenantId + "/oauth2/token \
    -F grant_type=client_credentials \
    -F resource=https://management.core.windows.net/ \
    -F client_id=" + clientId + "\
    -F client_secret=" + clientSecret
    btoken = jsoncmd.tojson(command)
    apicall = '''curl -L "https://management.azure.com/subscriptions/''' + adata["id"] + '''/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&%24filter=OfferDurableId+eq+'MS-AZR-0003P'+and+Currency+eq+'USD'+and+Locale+eq+'en-US'+and+RegionInfo+eq+'US'" -H "Authorization: Bearer ''' + btoken["access_token"]

    result = jsoncmd.json(apicall)
    with open('RateCardOutput.json', 'w') as outfile:
        outfile.write(result)
        outfile.close()
    print("RateCardOutput.json created")

if __name__ == "__main__":
    main()
