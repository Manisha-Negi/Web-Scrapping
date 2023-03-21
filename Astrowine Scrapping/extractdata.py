import os
import requests
import json
from unit_uom import uom_uom_pack
#from unit_uom import uom_uom_pack
#from eprice_pricemult import pricecols
from scrapinghelp import htmlhelper
from multiprocessing.pool import ThreadPool as Pool
import datetime

_counter = 0
finaldatalist = []
sql_data = []
removeduplicate=[]




class extractdata:

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
            #extractdata.readdatafromfile(link, start, _Zip,_JobNumber,  filepath)
            pool.apply_async(extractdata.readdatafromfile, (link, start, _Zip, _JobNumber, filepath))
        pool.close()
        pool.join()
        f = open(filepath, "w")
        f.writelines(finaldatalist)
        f.close()
        htmlhelper.insert_data('FoodCity_Data', sql_data)
        print("ExtractData End : " + str(datetime.datetime.now()))

    def readdatafromfile(link, start: int, _Zip: str,  _JobNumber: str, filepath: str):
        id = link["id"]
        cat1 = link["cat1"]
        cat2 = link["cat2"]
        category=''
        if cat2 != "":
            category = cat1 + ">"+cat2

        datafilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Data_" + str(id) + "_" + str(
            start) + ".txt"
        if os.path.exists(datafilename):
            infile = open(datafilename, 'r')
            datafromfile = str(infile.read()).replace('\\', '')

        datafilename1 = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/" + str(_Zip) + ".txt"
        if os.path.exists(datafilename1):
            infile1 = open(datafilename1, 'r')
            datafromfile1 = str(infile1.read()).replace('\\', '')
            Store_Detail_line = htmlhelper.returnvalue(datafromfile1, '<span class="street-address"', '/span>')
            Store_Detail = htmlhelper.returnvalue(Store_Detail_line, '>', '<')

            _Date = htmlhelper.returnvalue(datafromfile, "TIMESTAMP:[", "]")
            ProductArr = htmlhelper.collecturl(datafromfile,"","class=\"product-module-wrap item","</section>")

            for i in range(len(ProductArr)):
                extractdata.extract(ProductArr[i], category, _Zip, _JobNumber,datafilename, filepath, Store_Detail)
            infile.close()
            start = start + 1
            extractdata.readdatafromfile(link, start, _Zip, _JobNumber, filepath)

    def extract(Product: str, category: str, _Zip: str, _JobNumber: str, datafilename:str,filepath: str, Store_Detail:str):
        global _counter
        global sql_data
        ID = ""
        SITE = "www.foodcity.com"
        ZIP = _Zip
        DATE = datetime.date.today().strftime("%m/%d/%Y")
        IMAGELINK = htmlhelper.returnvalue(Product, 'src="', '"')
        PRICE_Line = htmlhelper.returnvalue(Product, 'data-price="', '"').replace("#8201;", " ").replace("&", "")
        PRICE = PRICE_Line
        PRICE_VALUE = PRICE_Line.replace("$", "").replace("w/Card", "").split(" ")
        PRICE_MULT = "1"
        EPRICE = htmlhelper.returnvalue(Product, 'data-price="$', '"')
        EINDICATOR = ""
        ALTPRICE = ""
        ALTPRICEMULT = ""
        EALTPRICE = ""
        ALTINDICATOR = ""
        PRODUCT_ID=''
        PACK = ""


        UNIT_Line = htmlhelper.returnvalue(Product, '<span class="clearfix tile-item__product__size">', '/span>')
        if 'title' in UNIT_Line:
            UNIT = htmlhelper.returnvalue(Product, '<span class="clearfix tile-item__product__size">', ';<').replace("&nbsp", "")
            UOM = htmlhelper.returnvalue(UNIT_Line, 'abbr title=\'', '</abbr>').replace("fluid ounce\'>", "").replace("pound\'>","").replace("ounce\'>","").replace("gallon\'>","").replace("count\'>","").replace("pack\'>","").replace("quart\'>","").replace("pint\'>","").replace("inch\'>","")
            if UNIT == "":
                UOM = ""
        if 'title' not in UNIT_Line:
            UNIT = htmlhelper.returnvalue(Product, '<span class="clearfix tile-item__product__size">', '&nbsp;')
            UOM = htmlhelper.returnvalue(UNIT_Line, '&nbsp;', '<')
            if UNIT == "":
                UOM = ""
        if 'pk' in UOM.lower() or 'pack' in UOM.lower():
            PACK = UNIT
            UNIT=""
            UOM=''

        # if 'per' in UNIT:
        #     UNIT = "1"

        if PRICE == "$0.00":
            PRICE = ""
            EPRICE = ""
            PRICE_MULT = ""


        SIZE = ""
        PAGEIMAGE = htmlhelper.returnvalue(Product, '(event, \'', "'")
        UPC_Line = PAGEIMAGE.split("/")
        UPC = UPC_Line[-1]

        # if UPC=='0007218056624':
        #       t=''
        ASIN = ""
        CATEGORY = category
        Description_First_line = htmlhelper.returnvalue(Product, 'class="d-none d-sm-inline d-slider-none">', '</span>').replace("u00ae", "").replace("u00c3u00", "e").replace("u00e9", "e").replace("eu00", "n").replace("u00c3u00b1", "n").replace("u00e8", "e").replace("u00e2u20acu2122s", "e").replace("u00f6", "e").replace("&nbsp;", "").replace("amp;", "")
        Description_Second_line = htmlhelper.returnvalue(Product, '<div class="clearfix tile-item__product__title d-block" title="', '"').replace("u00ae", "").replace("u00c3u00", "e").replace("u00e9", "e").replace("eu00", "n").replace("u00c3u00b1", "n").replace("u00e8", "e").replace("u00e2u20acu2122s", "e").replace("u00f6", "e").replace("&nbsp;", "").replace("amp;", "")
        DESCRIPTION = (Description_First_line+" "+Description_Second_line)
        if UPC == '0020695000000':
            DESCRIPTION = htmlhelper.returnvalue(Product, '<div class="clearfix tile-item__product__title d-block" title="', '">n').replace("u00ae", "").replace("u00c3u00", "e").replace("u00e9", "e").replace("eu00", "n").replace("u00c3u00b1", "n").replace("u00e8", "e").replace("u00e2u20acu2122s", "e").replace("u00f6", "e").replace("&nbsp;", "")

        NOTE = Description_First_line
        RATING = ""
        PAGEIMAGE = "https://www.foodcity.com"+PAGEIMAGE
        VALID = ""
        AISLE = ""
        ORIG_UPC = UPC_Line[-1]
        JOB_NUMBER = _JobNumber
        SALE_ENDDATE = ""

        if PACK=="":
            unituomvalues = uom_uom_pack.get_unit_uom(DESCRIPTION)
            PACK = str(unituomvalues["pack"]).strip()

        if 'per' in UNIT:
            EINDICATOR = "W"
            PRICE = PRICE_Line+" "+UNIT+" "+UOM
            UNIT = "1"

        if 'w/Card' in PRICE_Line:
            EINDICATOR = "V"
            PRICE = PRICE_Line
            EPRICE = PRICE_VALUE[-2]
            PRICE_MULT = PRICE_VALUE[0]

        if 'for' in PRICE_Line and 'w/Card' not in PRICE_Line:

            PRICE = PRICE_Line
            EPRICE = PRICE_VALUE[-1]
            PRICE_MULT = PRICE_VALUE[0]


        if ORIG_UPC not in removeduplicate and ORIG_UPC!= "":
            removeduplicate.append(ORIG_UPC)
            _counter = _counter + 1
            ID = str(_counter)

            listdata_ = htmlhelper.createpsv(SITE, ZIP, DATE, IMAGELINK, PRICE, PRICE_MULT, EPRICE, EINDICATOR,
                                             ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK, UNIT, UOM, SIZE,
                                             PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING, VALID,
                                             PAGEIMAGE, AISLE, ORIG_UPC, JOB_NUMBER, SALE_ENDDATE, '', Store_Detail, '',
                                             '', '',
                                             '', '',
                                             '', '', '',datafilename)
            print(listdata_)
            data_tuple = htmlhelper.create_data_list(SITE, ZIP, DATE, IMAGELINK, PRICE, PRICE_MULT, EPRICE, EINDICATOR,
                                                     ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK, UNIT, UOM,
                                                     SIZE, PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING,
                                                     VALID, PAGEIMAGE, AISLE, ORIG_UPC, JOB_NUMBER, SALE_ENDDATE, '',
                                                     Store_Detail, '',
                                                     '', '',
                                                     '', '',
                                                  '', '', '', datafilename)
            sql_data.append(data_tuple)

            finaldatalist.append(listdata_)
