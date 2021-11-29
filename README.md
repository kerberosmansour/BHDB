# BHDB Bing Hacking DB
Bing Hacking DB
Unlike Google, Bing has an API that allows you to programatically search, which is really useful for recon and can help with the detection of security issues quickly. Obviously bing doesn't have the depth and breadth of Google, but it's API means it can be more useful to security researchers. The example queries AKA "Dorks" were copied from the various GHDB the most prominent is https://www.exploit-db.com/ghdb/

# Current Status
Right now there is just a simple python demo and some example queries in the dorks folder
The following video goes through what is possible https://youtu.be/mlZFRHIr5WI

# Future State
I'm looking to flesh this out similar to other tooling in this area, but I would like to turn this into a python library so that other tools (such as OWASP nettacker are able to leverage the methods for other tools as well.

# Demo of Bing API
https://dev.cognitive.microsoft.com/docs/services/f40197291cd14401b93a478716e818bf/operations/56b4447dcf5ff8098cef380d/console

# Bing Python SDK
https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/quickstarts/client-libraries?pivots=programming-language-python


# Bing's advanced operators
https://docs.microsoft.com/en-us/previous-versions/bing/search/ff795625(v=msdn.10)


# Bing Vs Google Operators - Note an error Googles Inurl: == url: in Bing
https://www.bruceclay.com/blog/bing-google-advanced-search-operators/
Main differences I found are:
inurl: is url:
intext: is inbody:
ext: is filetype:
