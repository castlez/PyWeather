'''
Five day Forecast
copyright (c) 2017 by Jonathan Castle

This is a small python app that queries
weather information from a REST api
presented by Yahoo.com, and presents it
to the user.

'''

# imports
import urllib.request as request
import urllib.parse as parse
import json
import tkinter as tk

# execute query and present results
class WeatherGUI():
    def __init__(self, master):
        place = str(input("enter a place (<city>,<space><state abbreviation>) > "))
        # build the url
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast \
                     where woeid in (select woeid from geo.places(1) where text=\""+place+"\")"
        yql_url = baseurl + parse.urlencode({'q': yql_query}) + "&format=json"

        items = []
        # make request, retrieve response
        result = request.urlopen(yql_url).read()
        data = json.loads(result)
        forecast = data['query']['results']['channel']['item']['forecast']

        # present results
        items.append(tk.Label(master, text="Weather for " + place.title() + "\n"))
        for day in forecast[:5]:
            st = day['day'] + ", " + day['date'] + \
                     "\nHigh: " + str(day['high']) + \
                     "\nLow: " + str(day['low']) +\
                     "\nForecast: " + str(day['text']) + "\n"
            items.append(tk.Label(master, text=st))
        for i in items:
            i.pack()

# run
if __name__ == '__main__':
    root = tk.Tk()
    root.title("PyWeather")
    my_gui = WeatherGUI(root)
    root.mainloop()
