import urllib.request as request
import urllib.parse as parse
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

# build the url
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"portland, or\")"
yql_url = baseurl + parse.urlencode({'q':yql_query}) + "&format=json"

# make request, retrieve response
result = request.urlopen(yql_url).read()
data = json.loads(result)
forecast = data['query']['results']['channel']['item']['forecast']

# present results
pp.pprint(forecast)