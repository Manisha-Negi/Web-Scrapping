import os
import requests
import json
from unit_uom import uom_uom_pack
from requests.structures import CaseInsensitiveDict
from scrapinghelp import htmlhelper
from multiprocessing.pool import ThreadPool as Pool
from datetime import datetime
from datetime import date
import re

global count
_counter = 0
count = 0
sql_data = []
finaldatalist = []


class extractdata:

    def extractdata(_Zip: str, _JobNumber: str, _Date: str, dir_path):
        print("ExtractData Started : " + str(datetime.now()))

        filepath = os.path.dirname(__file__) + "/Psv/"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filepath = filepath + _JobNumber + ".PSV"

        if os.path.exists(filepath):
            os.remove(filepath)

        # this line add header in finaldatalist
        finaldatalist.append(htmlhelper.addheader(filepath))
        pool_size = 100
        pool = Pool(pool_size)
        all_file = dir_path
        value = len(os.listdir(all_file))
        for link in os.listdir(all_file):
            if re.findall("upc_", link):
                try:
                    # extractdata.extract(link,_Zip, _JobNumber, dir_path)
                    pool.apply_async(extractdata.extract, (link, _Zip, _JobNumber, dir_path,))
                except Exception as e:
                    print(e)
        pool.close()
        pool.join()

        f = open(filepath, "w")
        f.writelines(finaldatalist)
        f.close()
        htmlhelper.insert_data('Gothamwines_data', sql_data)
        print("ExtractData End : " + str(datetime.now()))


    def extract(product: str,  _Zip: str, _JobNumber: str,
                 dir_path):
        global _counter

        filename = dir_path + '/' + product
        infile = open(filename, 'r')
        variantData_list = json.load(infile)
        infile.close()
        Category = variantData_list[0]
        product = variantData_list[1]
        product_page = htmlhelper.returnformatedhtml(str(variantData_list[2])).replace('\\', '').replace('\\', '').replace("\n\t\t\t", "")
        try:
            ID = ""
            ZIP = _Zip
            today = date.today()
            DATE = today.strftime("%m/%d/%Y")
            SIZE = ""
            ALTPRICE = ""
            CATEGORY = Category
            PRICE = ""
            NOTE = htmlhelper.returnvalue(product_page, 'itemprop="brand" content="', '"/>')
            if NOTE == "":
                NOTE_COLLECTION = htmlhelper.returnvalue(product_page, "Varietal</td>", "/a>")
                NOTE_PART = htmlhelper.returnvalue(NOTE_COLLECTION, 'href="', "<")
                NOTE_List =  NOTE_PART.split(">")
                NOTE = NOTE_List[-1]
            src = ""
            UPC = ''
            # shortsource = htmlhelper.returnvalue(product, "<div class=\"catalog_item\">", "class='pagingBottom'")
            DESCRIPTION = htmlhelper.returnvalue(product, "title=\"", "\"").replace("<span>", "").replace("</span>",
                                                                                                          "").replace(
                'u00e9', 'e').replace('u00e8', 'e').replace('u00a0', ' ').replace('u00e0', 'a').replace('u00e3',
                                                                                                        'a').replace(
                'u00fa', 'u').replace('u00fc', 'u').replace('u00f1', 'n').replace('u00ed', 'i').replace('u00f3',
                                                                                                        'o').replace(
                'u00e2', 'a').replace('u00f4', 'o').replace('u00eb', 'e').replace('u00e7', 'c').replace('u00e1',
                                                                                                        'a').replace(
                'u00f6', 'o').replace('u00e4', 'a')


            PACK = "1"
            unit_uom = htmlhelper.returnvalue(product_page, '<td class="prodata_txt">', "</td>")
            if unit_uom != "":  # or "." in unit_uom:
                unit_uom_value = uom_uom_pack.get_unit_uom(unit_uom)
                UNIT = unit_uom_value['unit']
                UOM = unit_uom_value['uom']
                PACK = str(unit_uom_value["pack"]).strip()


            if unit_uom == "":
                unituomvalues = uom_uom_pack.get_unit_uom(DESCRIPTION)
                PACK = str(unituomvalues["pack"]).strip()
                UOM = str(unituomvalues["uom"]).strip()
                UNIT = str(unituomvalues["unit"]).strip()

            EPRICE = htmlhelper.returnvalue(product, "class='rd14'><b>$", "</b>")
            if EPRICE == "":
                EPRICE = htmlhelper.returnvalue(product, "class='rd14 sctxt'><b>$", "</b>")

            EALTPRICE = htmlhelper.returnvalue(product, "<strike>Original price:", "</strike>").replace("$", "")
            if (EPRICE != ""):
                PRICE = '$' + EPRICE
            if (EALTPRICE != ""):
                ALTPRICE = '$' + EALTPRICE
            IMAGE_LINK = "https://www.gothamwines.com" + htmlhelper.returnvalue(product,
                                                                                "src='/thumb/thumbme.html?src=", "&w")
            PAGEIMAGELINK = "https://www.gothamwines.com" + htmlhelper.returnvalue(product, "a href=\"", "\"")


            PRODUCT_ID = htmlhelper.returnvalue(product, "content_ids: ['", "'],")
            if PRODUCT_ID == "":
                PRODUCT_ID = htmlhelper.returnvalue(product, 'id="qty_', '"')

            SITE = "https://www.gothamwines.com"
            SALE_ENDDATE = ""
            PRICE_MULT = ""
            EINDICATOR = ""
            ALTPRICEMULT = ""
            ALTINDICATOR = ""
            ASIN = ""
            RATING = ""
            VALID = ""
            AISLE = ""
            SIZE = ""
            if (PRICE != "" and EPRICE != ""):
                PRICE_MULT = "1"
            if (ALTPRICE != "" and EALTPRICE != ""):
                ALTPRICEMULT = "1"
            if (PRICE != "" and ALTPRICE != ""):
                EINDICATOR = "*"


            ORIG_UPC = htmlhelper.returnvalue(product_page, 'itemprop="gtin8" content="', '"')
            SKU_Id = htmlhelper.returnvalue(product_page, "class='prodata_txt' content=\"", '"')

            if ORIG_UPC.isalpha() or ORIG_UPC == 'BARCODE_1219' or ORIG_UPC == 'BARCODE_2533':
                ORIG_UPC=""
            if ORIG_UPC!="":
                UPC = ORIG_UPC[0:-1]

            global count
            ID = count
            count = count + 1
            listdata = htmlhelper.createpsv(SITE, ZIP, DATE, IMAGE_LINK, PRICE, PRICE_MULT, EPRICE,
                                            EINDICATOR, ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK, UNIT,
                                            UOM,
                                            SIZE, PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING, VALID,
                                            PAGEIMAGELINK, SKU_Id, ORIG_UPC, _JobNumber, SALE_ENDDATE, '', '', '',
                                            '', '',
                                            '', '',
                                            '', '', '', '')

            print(listdata)
            data_tuple = htmlhelper.create_data_list(SITE, ZIP, DATE, IMAGE_LINK, PRICE, PRICE_MULT, EPRICE,
                                                     EINDICATOR, ALTPRICE, ALTPRICEMULT, EALTPRICE, ALTINDICATOR, PACK,
                                                     UNIT,
                                                     UOM,
                                                     SIZE, PRODUCT_ID, UPC, ASIN, CATEGORY, DESCRIPTION, NOTE, RATING,
                                                     VALID,
                                                     PAGEIMAGELINK, SKU_Id, ORIG_UPC, _JobNumber, SALE_ENDDATE, '', '',
                                                     '',
                                                     '', '',
                                                     '', '',
                                                     '', '', '', '')
            sql_data.append(data_tuple)
            finaldatalist.append(listdata)
        except Exception as e:
            print(e)
