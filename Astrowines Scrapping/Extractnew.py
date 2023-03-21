import os
import requests
import json
from unit_uom import uom_uom_pack
import re
#from eprice_pricemult import pricecols
from scrapinghelp import htmlhelper
from multiprocessing.pool import ThreadPool as Pool
import datetime

_counter = 0
finaldatalist = []
sql_data = []
product_list = []




class Extractdata:

    def extractdata(_Zip: str, _JobNumber: str):
        print("ExtractData Started : " + str(datetime.datetime.now()))

        filepath = os.path.dirname(__file__) + "/Psv/"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filepath = filepath + _JobNumber + ".PSV"

        if os.path.exists(filepath):
            os.remove(filepath)

        # this line add header in finaldatalist
        finaldatalist.append(htmlhelper.addheader(filepath))

        filename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/mainlink_" + str(_JobNumber) + ".txt"
        infile = open(filename, 'r')
        mainlink_list = json.load(infile)
        infile.close()

        pool_size = 100
        pool = Pool(pool_size)

        for link in mainlink_list:
            start = 1
            Extractdata.readdatafromfile(link, start, _Zip,_JobNumber,  filepath)
            # pool.apply_async(Extractdata.readdatafromfile, (link, start, _Zip, _JobNumber, filepath))
        pool.close()
        pool.join()
        Extractdata.get_prod()


    def readdatafromfile(link, start: int, _Zip: str,  _JobNumber: str, filepath: str):
        id = link["id"]
        category = link["cat1"]
        cat2 = link["cat2"]


        datafilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Data_" + str(id) + "_" + str(start) + ".txt"
        if os.path.exists(datafilename):
            infile = open(datafilename, 'r')
            datafromfile = str(infile.read()).replace('\\', '')

            ProductArr = htmlhelper.collecturl(datafromfile,"",'<div class="item-teaser">','<div class="add-to-cart-container">')

            for i in range(len(ProductArr)):
                Extractdata.extract(ProductArr[i], category, _Zip, _JobNumber,datafilename, filepath)
            infile.close()
            start = start + 1
            Extractdata.readdatafromfile(link, start, _Zip, _JobNumber, filepath)

    def extract(product: str, id: int, Category: str, _Zip: str, _Date: str, _JobNumber: str,
                 dir_path):

        global count
        PAGEIMAGELINK= 'https://www.astorwines.com/' + htmlhelper.returnvalue(product, 'href="', '"').replace("&amp;", "$")
        product_list.append([count, Category, PAGEIMAGELINK, product])
        count +=1


    def get_prod():

        pool_size = 100
        pool = Pool(pool_size)
        for link in product_list:
            try:
                # Extractdata.get_prdo_source(link,dir_path)

                pool.apply_async(Extractdata.get_prdo_source, (link)
            except Exception as e:
                print(e)
        pool.close()
        pool.join()


    def get_prdo_source(link):
        global _counter
        id = link[0]
        Category = link[1]
        url = link[2]
        product = link[3]

        proxies = {'http': 'http://us.proxymesh.com:31280',
                   'https': 'http://us.proxymesh.com:31280'}

        outfilename = os.path.dirname(__file__) + "/product" + "_" + str(id) + ".txt"
        if not os.path.exists(outfilename):
            r = ""
            while r == "" or r.status_code != 200:
                try:
                    r = requests.get(url, proxies=proxies, verify=False)
                    if r.status_code != 200:
                        print(str(r) + " : " + r)
                except Exception as e:
                    r = ""
                    print(e)

        else:
            print("Already exist")
        formatted_content = htmlhelper.returnformatedhtml(r.text)
        ORIG_UPC = htmlhelper.returnvalue(formatted_content, 'itemprop="gtin8" content="', '"')
        print(outfilename)
        fileout = open(outfilename, 'w')
        json.dump([Category, product, r.text], fileout)
        fileout.close()