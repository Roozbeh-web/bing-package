#!/bin/python3

import json
import urllib.request
from datetime import datetime
import os
import sys


def chosenDay(day = 0):

    jsonRequest = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=" + str(day) + "&n=1&mkt=en-US")
    
    jsonData = jsonRequest.read()

    imageUrl ="https://www.bing.com" + json.loads(jsonData)["images"][0]["url"]

    return imageUrl

def rangedDay(start, end):

    urlArray = []

    for i in range(start, end+1):
        jsonRequest = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=" + str(i) + "&n=1&mkt=en-US")

        jsonData = jsonRequest.read()

        imageUrl ="https://www.bing.com" + json.loads(jsonData)["images"][0]["url"]

        urlArray.append(imageUrl)

    return urlArray

def setBackground(day = 0):

    userEnter = ""

    if len(sys.argv) == 2:
        userEnter = sys.argv[1]
    else:
        userEnter = day

    jsonRequest = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=" + str(userEnter) + "&n=1&mkt=en-US")
    
    jsonData = jsonRequest.read()

    imageUrl ="https://www.bing.com" + json.loads(jsonData)["images"][0]["url"]

    today = datetime.today().strftime("%Y-%m-%d")

    fullPath = "/home/wabbajack/Pictures/" + today + ".jpg"

    urllib.request.urlretrieve(imageUrl,fullPath)

    os.system("gsettings set org.gnome.desktop.background picture-uri file:///" + fullPath)

if __name__ == "__main__":

    setBackground()