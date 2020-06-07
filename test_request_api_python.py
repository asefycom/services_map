from urllib.request import Request, urlopen
import json

key = "YourApiKeyFromMAP.IR"

req = Request('https://map.ir/search/v2?text=Alamut')
req.add_header('x-api-key', key)
content = urlopen(req).read()
# print(content)

y = json.loads(content)
print(y["value"][0]["geom"]["coordinates"])

