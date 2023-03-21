from scrapinghelp import htmlhelper
import requests
import os
import json
import datetime
from multiprocessing.pool import ThreadPool as Pool

mainlink_list1 = []
_Count = 1



def mainlink(_Zip, _JobNumber, _Date):
    mainlink_list = url = [[1, 'https://www.astorwines.com/hub.aspx?type=wine','Wine'],
                           [2, 'https://www.astorwines.com/hub.aspx?type=spirits','Spirits']]
    print("Mainlink Loaded to a list")
    # pool_size = 1
    # pool = Pool(pool_size)
    for link in mainlink_list:
        getdatafromweb(link, _JobNumber, mainlink_list, _Zip)
        # pool.apply_async(getdatafromweb,(link,_JobNumber, mainlink_list, _Zip))
    # pool.close()
    # pool.join()
    print("Data End")

def getdatafromweb(link, _JobNumber, mainlink_list, _Zip):


    global _Count
    id = link[0]
    Mainlink = link[1]
    Cat1 = link[2]
    if (Mainlink != ''):
        source = ""

        proxies = {'http': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959',
                   'https': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959'}

        while source == "" or source.status_code != 200:
            try:
                source = requests.get(Mainlink, proxies = proxies, verify=False)
                print(source)
            except Exception as e:
                print(e)

        html_source=htmlhelper.returnformatedhtml(source.text)
        short_source = htmlhelper.returnvalue(html_source, '<div class="classification__filter__grid margin-bottom-xl">', 'class="display-2 serif margin-bottom-sm"' )
        if short_source=='':
            short_source = htmlhelper.returnvalue(html_source,
                                                  '<div class="classification__filter__grid margin-bottom-xxl">',
                                                  'class="display-2 serif margin-bottom-sm"').replace(' svg"', "")

        # categorycollection=htmlhelper.collecturl(short_source,"",'class="classification__filter__item svg"', "</a>")
        categorycollection = htmlhelper.collecturl(short_source, "", 'class="classification__filter__item', "</a>")
        for cat in categorycollection:
            Cat2 = Cat1+">"+htmlhelper.returnvalue(cat, "Classification Filter - ", "'")
            cat_url = htmlhelper.returnvalue(cat, 'href=\"', '"' ).replace('..','https://www.astorwines.com')

            print(Cat2,cat_url)

            mainlink_list1.append(htmlhelper.mainlinksinsert(_Count, 'date', 'zip', "", Cat2, cat_url, "", "", "","Valid", "", "", "", ""))
            _Count += 1

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
        json.dump(mainlink_list1, fileout)  # The dump() method is used when the Python objects have to be stored in a file
        fileout.close()










