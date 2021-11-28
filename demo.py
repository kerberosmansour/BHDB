# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key.
subscription_key = "Secret token"

# Instantiate the client and replace with your endpoint.
client = WebSearchClient(endpoint="https://api.cognitive.microsoft.com/", credentials=CognitiveServicesCredentials(subscription_key))

# Make a request. Show me all PDF files on CNN.com
domain = "site:cnn.com"
dork = "filetype:pdf"
querystring = domain + ' ' + dork
web_data = client.web.search(query=querystring)
print("\r\nSearched for Query# \" PDF Files in cnn.com \"")

'''
Web pages
If the search response contains web pages, the first result's name and url
are printed.
'''
if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))
else:
    print("Didn't find any web pages...")

# Loop which lists all the URLS
for i in range(len(web_data.web_pages.value)):
    result = web_data.web_pages.value[i]
    print("Web page name: {} ".format(result.name))
    print("Web page URL: {} ".format(result.url))
