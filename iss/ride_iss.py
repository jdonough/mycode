#!/usr/bin/python3
"""Alta3 || Tracking ISS"""
import urllib.request
import json
## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'
def main():
## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
## put fileobject into helmet
    helmet = groundctrl.read()
## decode json to python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
## display our pythonic data
    print("\n\nConverted python data")
    print(helmetson)
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    print ( people [0] ['name'] )
    print ( people [0] ['craft'] )
    print( people[0]['name'], " on the " + people[0]['craft'] )
    print( people[1]['name'], " on the " + people[1]['craft'] )
    print( people[2]['name'], " on the " + people[2]['craft'] )
    print( people[3]['name'], " on the " + people[3]['craft'] )
    print( people[4]['name'], " on the " + people[4]['craft'] )
    print( people[5]['name'], " on the " + people[5]['craft'] )
    for x in people:
        print ( x['name'], "is on the "  + x['craft'])

main()
