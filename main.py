import urllib.request as request
import urllib.parse as parse
import json
import pprint
from flask import Flask
import webbrowser

app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=2)

@app.route('/')
def present_forecast():
    place = "portland, or"
    # build the url
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"portland, or\")"
    yql_url = baseurl + parse.urlencode({'q': yql_query}) + "&format=json"

    # make request, retrieve response
    result = request.urlopen(yql_url).read()
    data = json.loads(result)
    forecast = data['query']['results']['channel']['item']['forecast']

    # present results
    outstring = '<html><body><h1> Five day forecast for ' + place
    for day in forecast[:5]:
        outstring += "<br><br>" + day['day'] + ", " + day['date'] + \
                     "<br>High: " + str(day['high']) + \
                     "<br>Low: " + str(day['low']) +\
                     "<br>" + str(day['text'])
    return outstring + '</body></html>'

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run()
