from scrapinghelp import htmlhelper
import requests
import os
import json
import datetime
from multiprocessing.pool import ThreadPool as Pool


mainlink_list = []
mainlink_list_withids = []

def mainlink(Cookie,_Date,_Zip,_JobNumber):

    url ='https://www.foodcity.com'
    Source = urlget(url,Cookie,)

    source = htmlhelper.returnformatedhtml(Source.text)
    #Store_Detail = htmlhelper.returnvalue(source,'<span class="street-address">','<')
    htmlhelper.logtxt(source,_Zip, _JobNumber)
    shortcontent=htmlhelper.returnvalue(source,"A-Z</span></span></a>","</ul></li></ul></li>")
    categorycollection=htmlhelper.collecturl(shortcontent,"","<li","</li>")
    _Count = 0
    for x in categorycollection:
        cat1_name=htmlhelper.returnvalue(x,"<span>","</span>")
        cat1_url="https://www.foodcity.com/"+htmlhelper.returnvalue(x,"href=\"","\"")
        try:
            cat1_source = urlget(cat1_url,Cookie)
            cat1_source_format = htmlhelper.returnformatedhtml(cat1_source.text)
            cat1_shortcontent = htmlhelper.returnvalue(cat1_source_format, '<div class="dept-categories-slider', '<div id="circularsContainer">')
            category1collection=htmlhelper.collecturl(cat1_shortcontent,"","<div","</div>")

            for y in category1collection:
                cat2_name = htmlhelper.returnvalue(y+"&&", "center\">", "&&")
                cat2_url = "https://www.foodcity.com/"+htmlhelper.returnvalue(y, "href='", "';")
                finalcategory=cat1_name+">"+cat2_name
                print(finalcategory)
                _Count = _Count + 1
                mainlink_list.append( htmlhelper.mainlinksinsert(_Count, _Date, _Zip, cat2_url, cat1_name, cat2_name, "", "", "", "Valid", "", "", "", ""))
                #print(mainlink_list)
        except Exception as e:
            print(e)
            pass

    mainlink_list.append(
        htmlhelper.mainlinksinsert(_Count, _Date, _Zip, 'https://www.foodcity.com/search/all/?searchType=All&Search=mayo&resetSearch=1', "mayo", "", "", "", "", "Valid", "", "", "",
                                   ""))
    _Count=_Count+1
    mainlink_list.append(
        htmlhelper.mainlinksinsert(_Count, _Date, _Zip, 'https://www.foodcity.com/search/all/?searchType=All&Search=oil&resetSearch=1', "oil", "", "", "", "", "Valid", "", "", "",
                                   ""))

    filename = "mainlink_" + _JobNumber
    directory = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/"
    try:
        if os.path.exists(directory):
            if os.path.exists(directory + filename + ".txt"):
                os.remove(directory + filename + ".txt")
        else:
            os.makedirs(directory)
    except OSError:
        print('Error: deleting. ' + directory)
    fileout = open(directory + filename + ".txt", 'w')
    json.dump(mainlink_list,fileout)  # The dump() method is used when the Python objects have to be stored in a file
    fileout.close()

#mainlink()


def urlget(url, Cookie):
    

    source=""
    while source=="" or source.status_code!=200:
        try:
            source = requests.get(url, headers={"Cookie": Cookie},verify=False)
            if source.status_code!=200:
                print(url)
        except Exception as e:
            print(e)
            source=""

    return source


