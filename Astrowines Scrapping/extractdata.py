import os
import requests
import json
from UnitUom import GetUomUnitSize
from unit_uom import uom_uom_pack
import re
#from eprice_pricemult import pricecols
from scrapinghelp import htmlhelper
from multiprocessing.pool import ThreadPool as Pool
import datetime

_counter = 0
finaldatalist = []
sql_data = []
removeduplicate=[]




class extractdata:

    def product_source(PAGEIMAGE,outfilename):
        source_html_format=''
        ProducturlJsonsource = ""
        proxies = {'http': 'http://us.proxymesh.com:31280',
                   'https': 'http://us.proxymesh.com:31280'}
        while ProducturlJsonsource == "" or ProducturlJsonsource.status_code != 200 or 'Request Rejected' in ProducturlJsonsource.text:
            try:

                ProducturlJsonsource = requests.get(PAGEIMAGE, proxies=proxies, verify=False, timeout=100)
                source = ProducturlJsonsource.text
                # print(source)
                source_html_format = htmlhelper.returnformatedhtml(source)
                short_source = htmlhelper.returnvalue(source_html_format,
                                                      "<script type=\"text/javascript\">gtag('config', 'UA-2355059-3');gtag('config', 'G-3PNZZ7ZXJL');</script>",
                                                      '<script type="application/ld+json">')
                # coll_source = htmlhelper.collecturl(short_source, '', '<script type="text/javascript">gtag', '</script>')
                if ProducturlJsonsource.status_code == 200:
                    fileout = open(outfilename, 'w')
                    json.dump(source_html_format, fileout)
                    fileout.close()
            except Exception as e:
                session_obj = requests.session()
                ProducturlJsonsource = ""
                print(e)
        return source_html_format
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
            # extractdata.readdatafromfile(link, start, _Zip,_JobNumber,  filepath)
            pool.apply_async(extractdata.readdatafromfile, (link, start, _Zip, _JobNumber, filepath))
        pool.close()
        pool.join()
        f = open(filepath, "w")
        f.writelines(finaldatalist)
        f.close()
        htmlhelper.insert_data('Astrowine_Data', sql_data)
        print("ExtractData End : " + str(datetime.datetime.now()))

    def readdatafromfile(link, start: int, _Zip: str,  _JobNumber: str, filepath: str):
        id = link["id"]
        category = link["cat1"]
        cat2 = link["cat2"]

        # id=8
        # start=13
        datafilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Data_" + str(id) + "_" + str(start) + ".txt"
        if os.path.exists(datafilename):
            infile = open(datafilename, 'r')
            datafromfile =htmlhelper.returnformatedhtml( str(infile.read()).replace('\\', ''))

            ProductArr = htmlhelper.collecturl(datafromfile,"",'<div class="item-teaser">','<div class="add-to-cart-container">')

            for i in range(len(ProductArr)):
                extractdata.extract(ProductArr[i], category, _Zip, _JobNumber,datafilename, filepath)
            infile.close()
            start = start + 1
            extractdata.readdatafromfile(link, start, _Zip, _JobNumber, filepath)

    def extract(Product: str, category: str, _Zip: str, _JobNumber: str, datafilename:str,filepath: str):
        try:
            global _counter
            global sql_data
            ID = ""
            SITE = "www.astorwines.com"
            ZIP = _Zip
            DATE = datetime.date.today().strftime("%m/%d/%Y")
            IMAGELINK = 'https://www.astorwines.com' + htmlhelper.returnvalue(Product, 'src="', '"')
            # PRICE = PRICE_Line
            # PRICE_VALUE = PRICE_Line.replace("$", "").replace("w/Card", "").split(" ")
            ALTPRICE = ""
            PRICE_MULT = ""
            PRICE = htmlhelper.returnvalue(Product, 'class="price-value price-bottle display-2"><span class="price-sale">','</span>')
            EPRICE = htmlhelper.returnvalue(Product, 'class="price-value price-bottle display-2"><span class="price-sale">$','</span>')
            EINDICATOR = ""
            if EPRICE == "":
                EPRICE = htmlhelper.returnvalue(Product, 'class="price-value price-bottle display-2">$','</span>')
                if EPRICE != "":
                    PRICE = "$" + EPRICE
            EALTPRICE = htmlhelper.returnvalue(Product, 'class="price-value price-old price-bottle">$', '</span>')
            if EALTPRICE != "":
                ALTPRICE = "$"+EALTPRICE

            ALTPRICEMULT = ""
            ALTINDICATOR = ""
            PRODUCT_ID= htmlhelper.returnvalue(Product, '<span class="itemNumber text-muted small">Item #', '</span')
            PACK = ""
            Store_Detail = ''
            SIZE = ""
            PAGEIMAGE = 'https://www.astorwines.com/' + htmlhelper.returnvalue(Product, 'href="', '"').replace("&amp;", "&")
            NOTE = ''

            # if PRODUCT_ID == '34381':
            #     t = ''
            outfilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Product_" + str(PRODUCT_ID) + ".txt"
            # print(outfilename)

            source_html_format=''
            if not os.path.exists(outfilename):
                source_html_format=extractdata.product_source(PAGEIMAGE,outfilename)
            else:
                infile = open(outfilename, 'r')
                source_html_format = htmlhelper.returnformatedhtml(str(infile.read()).replace('\\', ''))
                short_source = htmlhelper.returnvalue(source_html_format, "<script type=\"text/javascript\">gtag('config', 'UA-2355059-3');gtag('config', 'G-3PNZZ7ZXJL');</script>",'<script type="application/ld+json">')

            try:
                NOTE_SHORTSOURCE=htmlhelper.returnvalue(source_html_format,"items': [{'id':'"+str(PRODUCT_ID)+"'","</script>")
                NOTE = htmlhelper.returnvalue(NOTE_SHORTSOURCE, "'brand':'", "',")

            except Exception as e:
                print(e)

            if NOTE == '':
                try:
                    source_html_format = extractdata.product_source(PAGEIMAGE,outfilename)
                    NOTE_SHORTSOURCE = htmlhelper.returnvalue(source_html_format,"items': [{'id':'" + str(PRODUCT_ID) + "'", "</script>")
                    NOTE = htmlhelper.returnvalue(NOTE_SHORTSOURCE, "'brand':'", "',")

                except Exception as e:
                    print(e)

            ASIN = ""
            CATEGORY = category
            Description_First_line = htmlhelper.returnvalue(Product, '<h2', '</h2').replace("u00ae", "").replace("u00c3u00", "e").replace("u00e9", "e").replace("eu00", "n").replace("u00c3u00b1", "n").replace("u00e8", "e").replace("u00e2u20acu2122s", "e").replace("u00f6", "e").replace("&nbsp;", "").replace("amp;", "")
            Description_Second_line = htmlhelper.returnvalue(Description_First_line, 'href="', '</a>').replace("u00ae", "").replace("u00c3u00", "e").replace("u00e9", "e").replace("eu00", "n").replace("u00c3u00b1", "n").replace("u00e8", "e").replace("u00e2u20acu2122s", "e").replace("u00f6", "e").replace("&nbsp;", "").replace("amp;", "")
            DESCRIPTION = htmlhelper.returnvalue(Description_Second_line+'}', '">', '}')
            UPC = ''
            Product_htmlformat =  htmlhelper.returnformatedhtml(Product)
            UNIT_First_line = htmlhelper.returnvalue(Product_htmlformat, '<div class="teaser__item__meta__2">', '<div id="" class="item-description supporting-text hidden-xs">')
            UNIT_Second_line = htmlhelper.returnvalue(UNIT_First_line,'rn <span class="small"', '</div>rnrn rn rn')
            unit_uom = htmlhelper.returnvalue(UNIT_Second_line, 'class="small">', '</span')
            UNIT = ''
            UOM = ''
            if unit_uom != "": #or "." in unit_uom:
                unit_uom_value = GetUomUnitSize(unit_uom)
                UNIT = unit_uom_value[2]
                UOM = unit_uom_value[1]
            # if unit_uom != "":
            #     UNIT = htmlhelper.returnvalue(coll_source[1], "'variant': '", "'")


            RATING = ""
            VALID = ""
            AISLE = ""
            ORIG_UPC = ''
            JOB_NUMBER = _JobNumber
            SALE_ENDDATE = ""


            if (PRICE != "" and EPRICE != ""):
                PRICE_MULT = "1"

            if (ALTPRICE != "" and EALTPRICE != ""):
                ALTPRICEMULT = "1"

            if (PRICE != "" and ALTPRICE != ""):
                EINDICATOR = "*"

            unituomvalues = uom_uom_pack.get_unit_uom(DESCRIPTION)
            PACK = str(unituomvalues["pack"]).strip()

            # if ORIG_UPC not in removeduplicate and ORIG_UPC!= "": #and ORIG_UPC.isdigit():


            _counter = _counter + 1
            ID = str(_counter)

            listdata_ = htmlhelper.createpsv(SITE, ZIP, DATE, IMAGELINK, PRICE, PRICE_MULT, EPRICE, EINDICATOR,
                                             ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK, UNIT, UOM, SIZE,
                                             PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING, VALID,
                                             PAGEIMAGE, AISLE, ORIG_UPC, JOB_NUMBER, SALE_ENDDATE, '', '', '',
                                             '', '',
                                             '', '',
                                             '', '', '',datafilename)
            print(ID,listdata_)
            data_tuple = htmlhelper.create_data_list(SITE, ZIP, DATE, IMAGELINK, PRICE, PRICE_MULT, EPRICE, EINDICATOR,
                                                     ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK, UNIT, UOM,
                                                     SIZE, PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING,
                                                     VALID, PAGEIMAGE, AISLE, ORIG_UPC, JOB_NUMBER, SALE_ENDDATE, '',
                                                     '', '',
                                                     '', '',
                                                     '', '',
                                                  '', '', '', datafilename)
            sql_data.append(data_tuple)

            finaldatalist.append(listdata_)

        except Exception as a:
            print(a)