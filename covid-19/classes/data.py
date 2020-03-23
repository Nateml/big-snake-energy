import urllib.request
import re

class Summary(object):
    
    def __init__(self):
        with urllib.request.urlopen("https://www.worldometers.info/coronavirus/") as source: #opens covid-19 stat page
            html = source.read().decode() # read, convert bytes to string

            self.deaths = re.findall("([0-9,]+)(?= Deaths)", html)[0] #deaths
            self.tot_cases = re.findall("([0-9,]+)(?= Cases)", html)[0] #total cases

            active_case_index = html.find("Active Cases") #index where string "Active Cases" is found
            ac_patch = html[active_case_index:]
            self.active_cases = re.findall("(?<=\"number-table-main\">)[0-9,]+", ac_patch)[0]

    def __str__(self):
        return ("%s DEATHS \n%s ACTIVE CASES \n%s TOTAL CASES" % (self.deaths, self.active_cases, self.tot_cases))
        
        