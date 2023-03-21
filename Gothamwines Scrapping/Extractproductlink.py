import os
import requests
import json
from unit_uom import uom_uom_pack
from requests.structures import CaseInsensitiveDict
from scrapinghelp import htmlhelper
from multiprocessing.pool import ThreadPool as Pool
from datetime import datetime
from datetime import date

global count

count = 1
mainlink_list = []


class Extractdata:

    def extractdata(_Zip: str, _JobNumber: str, _Date: str, dir_path):
        print("ExtractData Started : " + str(datetime.now()))

        mainlink_list = [[1, "https://www.gothamwines.com/wines/", "Wines"],
                         [2, "https://www.gothamwines.com/spirits/", "Spirits"]]
        print("Data extracted")

        pool_size = 100
        pool = Pool(pool_size)
        for link in mainlink_list:
            start = 1
            try:
                # extractdata.readdatafromfile(link, start,_Zip, _JobNumber,dir_path)

                pool.apply_async(Extractdata.readdatafromfile, (link, start, _Zip, _JobNumber,  dir_path,))
            except Exception as e:
                print(e)
        pool.close()
        pool.join()
        Extractdata.get_prod(dir_path)

    def readdatafromfile(link, start: int, _Zip: str, _JobNumber: str, dir_path: str):

        id = link[0]
        Mainlink = link[1]
        Category = link[2]
        datafilename = dir_path + "/Data" + str(id) + "_" + str(start) + ".txt"

        if os.path.exists(datafilename):
            infile = open(datafilename, 'r')
            datafromfile = str(infile.read()).replace('\\', '').replace('\\', '').replace("\n\t\t\t", "")
            today = date.today()
            _Date = today.strftime("%m/%d/%Y")

            ProductArr = htmlhelper.collecturl(datafromfile, "", "class='rimgaw'>", "<div class='lnotif'")
            print(datafilename)
            for i in range(len(ProductArr)):
                Extractdata.extract(ProductArr[i], id, Category, _Zip, _Date, _JobNumber, dir_path)
            infile.close()
            start = start + 1
            Extractdata.readdatafromfile(link, start, _Zip, _JobNumber, dir_path)


    def extract(product: str, id: int, Category: str, _Zip: str, _Date: str, _JobNumber: str,
                 dir_path):

        global count
        PAGEIMAGELINK = "https://www.gothamwines.com" + htmlhelper.returnvalue(product, "a href=\"", "\"")
        mainlink_list.append([count, Category, PAGEIMAGELINK, product])
        count +=1


    def get_prod(dir_path):

        pool_size = 100
        pool = Pool(pool_size)
        for link in mainlink_list:
            try:
                # Extractdata.get_prdo_source(link,dir_path)

                pool.apply_async(Extractdata.get_prod_source, (link, dir_path))
            except Exception as e:
                print(e)
        pool.close()
        pool.join()


    def get_prod_source(link,dir_path):
        global _counter
        id = link[0]
        Category = link[1]
        url = link[2]
        product = link[3]

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "text/plain;charset=UTF-8",
            "origin": "https://www.gothamwines.com",
            "referer": "https://www.gothamwines.com",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }


        proxies = {
            'http': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959',
            'https': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959'}

        outfilename = dir_path + "/upc" + "_" + str(id) + ".txt"
        if not os.path.exists(outfilename):
            source = ""
            while source == "" or source.status_code != 200:
                try:
                    source = requests.get(url, headers=headers, proxies=proxies, verify=False)
                    if source.status_code != 200:
                        print(str(source) + " : " + source)
                except Exception as e:
                    source = ""
                    print(e)

        else:
            print("Already exist")
        formatted_content = htmlhelper.returnformatedhtml(source.text)
        # ORIG_UPC = htmlhelper.returnvalue(formatted_content, 'itemprop="gtin8" content="', '"')
        print(outfilename)
        fileout = open(outfilename, 'w')
        json.dump([Category, product, source.text], fileout)
        fileout.close()
