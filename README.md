# Azure-Ratecard-REST-API-Calls
This program configures your Azure account to run rate card API calls and then runs the API call.

# Dependecies
The following dependecies are critical to running the program and cost free.
1. [Python](https://www.python.org/downloads/)
2. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
3. [Microsoft Azure Subscription](https://azure.microsoft.com/en-us/free/)

# Step 1: Run InitialAZConfig.py
Notes: This initial script requires the Azure CLI installed.
  You will be prompted to login to Azure through your browser. The script will then use your account IDs to create certain IAM user roles.
  The file where your script is located will now have JSON files with account information you will NOT want to share.

# Step 2: Run RatecardAPIQuery.py
Notes: This script does not require the Azure CLI installed, but it requires the JSON files form the previous script. 
  You will not have to do anything in between step one and two.
  The script will use your account secret credentials to request a bearer token and then initiate a defualt** Azure ratecard API call.

 ** The following are the selected filters for the ratecard API call: "RateCard?api-version=2016-08-31-preview&%24filter=OfferDurableId+eq+'MS-AZR-0003P'+and+Currency+eq+'USD'+and+Locale+eq+'en-US'+and+RegionInfo+eq+'US'"

# Sources
["How to query the Azure Rate Card API for cloud pricing"](https://medium.com/@dmaas/how-to-query-the-azure-rate-card-api-for-cloud-pricing-complete-step-by-step-guide-4498f8b75c2c) by Dan Maas

["Azure REST API Reference"](https://docs.microsoft.com/en-us/rest/api/azure/)
