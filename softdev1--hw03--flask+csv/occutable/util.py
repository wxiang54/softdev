import random
import json
import urllib

'''
Parses csv file and returns dict of values
Input: String of path to CSV file
Output: dictionary of key/value pairs
'''
def parseCSV( f ):
    jobfile = open(f, 'r')
    jobsDict = {}
    for line in jobfile.readlines()[1:-1]: #skip first and last line
        splitIndex = line.rfind(",") #find last occurance of comma
        jobsDict[line[:splitIndex].strip('"')] = float(line[splitIndex+1:]) #split line accordingly
    return jobsDict


'''
Returns random key in dictionary
Input: dictionary of key/value pairs
Output: randomly chosen key based on chance (value)
'''
def randKey( d ):
    randnum = random.randrange(1000)/10.
    curr = 0
    for occupation, chance in d.items():
        curr += chance
        if randnum < curr:
            return occupation
            return "Unemployed"

'''
Returns dictionary representing JSON data of gSearch request
Input: query string to search
Output: dict of data
'''
def gSearch(query):
    key = "AIzaSyCo_tjQPjnuhvVvYl3Ww2qBdf__H7Nd8C8" #no steal plis
    engine = "006364323019142257526:6ekppwbngni"
    url = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s' % (key, engine, query)
    response = urllib.urlopen(url).read()
    return json.loads(response)
