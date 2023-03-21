
import json
import os
from scrapinghelp import htmlhelper
import requests
from datetime import datetime
from multiprocessing.pool import ThreadPool as Pool
import threading

session_obj = requests.session()
class data:

    def data(_Zip:str,_JobNumber:str):
        print("Data Started")
        filename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/mainlink_" + str(_JobNumber)+".txt"
        infile = open(filename,'r')
        mainlink_list = json.load(infile)
        infile.close()
        print("Mainlink Loaded to a list")

        pool_size = 200
        pool = Pool(pool_size)
        for link in mainlink_list:

            # data.getdatafromweb(link, _Zip,  _JobNumber,  mainlink_list)
            pool.apply_async(data.getdatafromweb, (link, _Zip,  _JobNumber,  mainlink_list))

        pool.close()
        pool.join()

        print("Data End")

    def getdatafromweb(link, _Zip,  _JobNumber,  mainlink_list):
        global session_obj
        id = link["id"]
        category1 = link["cat1"]
        main_link = link["cat2"]

        if main_link != "":
            totalcount =""
            noofpage=1
            startpage=1
            i=1
            
            proxies = given_proxies
            
            while i <= noofpage:
                outfilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Data_" + str(id) + "_" + str(i) + ".txt"
                print(outfilename)


                ProducturlJsonsource = ""
                while ProducturlJsonsource == "" or ProducturlJsonsource.status_code != 200 or 'Request Rejected' in ProducturlJsonsource.text:
                    try:
                        new_mainlink = main_link + '&Page=' + str(i)
                        ProducturlJsonsource = session_obj.get(new_mainlink,proxies=proxies,verify=False,timeout=100)

                        source = ProducturlJsonsource.text
                        #print(source)

                    except Exception as e:
                        session_obj = requests.session()
                        ProducturlJsonsource = ""
                        print(e)

                if i == 1:
                    formatted_content = htmlhelper.returnformatedhtml(source)
                    shortsrc = htmlhelper.returnvalue(formatted_content, "style='PADDING-BOTTOM:4px;PADDING-TOP:4px;'>", "</div>")
                    print(shortsrc)
                    totalcount = htmlhelper.returnvalue(shortsrc, "(of", ")").lstrip().rstrip()
                    if totalcount != "":
                        noofpage = htmlhelper.returnnumberofpages(int(totalcount), 12)  # print(noofpage)


                print("Scrapping: id-" + str(id) + "/" + str(len(mainlink_list)) + " - Time-" + str(
                    datetime.now()) + " - Page N.- " + str(i))

                fileout = open(outfilename, 'w')
                # DATE = "TIMESTAMP:[" + datetime.now(timezone('US/Eastern')).strftime("%m/%d/%Y %I:%M:%S %p") + "]"
                json.dump(source, fileout)
                fileout.close()
                i=i+1
