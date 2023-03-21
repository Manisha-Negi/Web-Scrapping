from multiprocessing.pool import ThreadPool as Pool
import requests
from requests.structures import CaseInsensitiveDict
from scrapinghelp import htmlhelper
from datetime import datetime
from pytz import timezone
import os
import json


class data:
    def data(_Zip, _JobNumber, _Date, dir_path):
        mainlink_list = [[1, "https://www.gothamwines.com/wines/", "Wines"],
                         [2, "https://www.gothamwines.com/spirits/", "Spirits"]]
        print("Mainlink Loaded to a list")
        pool_size = 100
        pool = Pool(pool_size)
        for link in mainlink_list:
            #data.getdatafromweb(link, _JobNumber, mainlink_list, _Zip, dir_path)
            pool.apply_async(data.getdatafromweb,(link,_JobNumber, mainlink_list, _Zip,dir_path))
        pool.close()
        pool.join()
        print("Data End")

    def getdatafromweb(link, _JobNumber, mainlink_list, _Zip, dir_path):
        id = link[0]
        Mainlink = link[1]
        Category = link[2]
        if (Mainlink != ''):
            totalcount = ""
            noofpage = 1
            startpage = 1
            i = 1
            proxies = given_proxies
            
            headers ={
            "accept": "*/*",
            "accept-encoding":"gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            #"content-length": " 1459",
            # "content-type": "text/plain;charset=UTF-8",
            # "origin": "https://www.gothamwines.com",
            # "referer": "https://www.gothamwines.com",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            }
            while i <=noofpage:

                ProducturlJson = Mainlink + "?page=" + str(startpage) + "&sortby=winery&l=100"
                ProducturlJsonsource = ""
                while ProducturlJsonsource == "" or (
                        ProducturlJsonsource.status_code != 200 and ProducturlJsonsource.status_code != 204):
                    try:
                        ProducturlJsonsource = requests.get(ProducturlJson, headers=headers,verify=False,proxies=proxies)
                        if ProducturlJsonsource.status_code != 200:
                            print(str(ProducturlJsonsource) + " : " + ProducturlJson)
                    except Exception as e:
                        ProducturlJsonsource = ""
                        print(e)

                if i == 1:
                    formatted_content = htmlhelper.returnformatedhtml(ProducturlJsonsource.text)
                    shortsrc=htmlhelper.returnvalue(formatted_content,"<li class=\"txt\">","/li>")
                    print(shortsrc)
                    noofpage = htmlhelper.returnvalue(shortsrc,"of","<").lstrip().rstrip()

                    try:
                        print(noofpage)
                        noofpage=int(noofpage)
                    except Exception as e:
                        print(e)

                print("Scrapping: id-" + str(id) + "/" + str(len(mainlink_list)) + " pages-" + str(i) + "/" + str(
                    noofpage) + " - Time-" + str(datetime.now()))
                outfilename = dir_path + "/Data" + str(id) + "_" + str(i) + ".txt"
                fileout = open(outfilename, 'w')
                DATE = "TIMESTAMP:[" + datetime.now(timezone('US/Eastern')).strftime("%m/%d/%Y %I:%M:%S %p") + "]"
                json.dump(DATE + ProducturlJsonsource.text, fileout)
                fileout.close()
                startpage = startpage + 1
                i = i + 1
